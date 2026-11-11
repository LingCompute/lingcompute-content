import argparse
import json
import mimetypes
import shutil
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from . import preview
except ImportError:
    import preview

ROOT = Path(__file__).resolve().parents[1]
LIVE_SCRIPT = """
const version = Number(new URL(document.currentScript.src).searchParams.get("v"));
const banner = document.getElementById("preview-status");
async function update() {
    try {
        const response = await fetch("/__preview__/state", {cache: "no-store"});
        if (!response.ok) throw new Error("Preview server unavailable");
        const state = await response.json();
        banner.hidden = !state.error && !state.building;
        banner.textContent = state.error
            ? "构建失败，修复保存后会自动恢复：" + state.error
            : "正在重新生成预览…";
        if (!state.error && !state.building && state.version !== version) {
            location.reload();
            return;
        }
    } catch (error) {
        banner.hidden = false;
        banner.textContent = "本地预览服务已断开，重新启动后将自动恢复。";
    }
    setTimeout(update, 500);
}
update();
"""


def fingerprint(root):
    paths = list((root / "content").rglob("*")) + list((root / ".cache/fonts").glob("*.woff2"))
    paths += [root / name for name in (
        "tools/style.css", "config/products.json", "reviews/legacy.json",
        "assets/brand/lingcompute-horizontal.svg",
    )]
    return tuple(
        (path.relative_to(root).as_posix(), stat.st_mtime_ns, stat.st_size, stat.st_ino)
        for path in sorted(paths) if path.is_file() for stat in [path.stat()]
    )


def live_document(document, version):
    document = document.replace(
        "default-src 'none';", "default-src 'none'; script-src 'self'; connect-src 'self';", 1,
    )
    document = document.replace(
        "<body>", '<body><div id="preview-status" role="status" class="meta" hidden></div>', 1,
    )
    return document.replace("</body>", f'<script defer src="/__preview__/live.js?v={version}"></script></body>', 1)


class PreviewServer(ThreadingHTTPServer):
    def __init__(self, root, output, port=8000):
        self.root = root
        self.output = output
        self.assets = output / "assets"
        self.site = None
        self.version = 0
        self.error = ""
        self.building = True
        self.lock = threading.Lock()
        self.stop = threading.Event()
        super().__init__(("127.0.0.1", port), PreviewHandler)

    def state(self):
        with self.lock:
            return {"version": self.version, "error": self.error, "building": self.building}


class PreviewHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *arguments):
        pass

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        try:
            host = urlsplit("//" + self.headers.get("Host", "")).hostname
        except ValueError:
            host = None
        if host not in {"127.0.0.1", "localhost"}:
            self.send_error(403)
            return
        requested = unquote(urlsplit(self.path).path).lstrip("/")
        if requested == "__preview__/state":
            self.respond(json.dumps(self.server.state()).encode(), "application/json")
            return
        if requested == "__preview__/live.js":
            self.respond(LIVE_SCRIPT.encode(), "text/javascript")
            return
        with self.server.lock:
            site, version = self.server.site, self.server.version
        if requested.startswith("__preview__/source/"):
            base = self.server.root / "content"
            relative = requested.removeprefix("__preview__/source/content/")
            if relative == requested:
                self.send_error(404)
                return
            path = (base / relative).resolve()
            if path.suffix.lower() not in {".md", ".json", ".png", ".jpg", ".jpeg", ".gif", ".webp"}:
                self.send_error(404)
                return
        else:
            if site is None:
                document = (
                    '<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
                    '<meta name="viewport" content="width=device-width,initial-scale=1">'
                    '<body><h1>本地实时预览</h1><p>等待首次构建…</p></body></html>'
                )
                self.respond(live_document(document, version).encode(), "text/html")
                return
            base = self.server.output if requested.startswith("assets/") else site
            path = (base / requested).resolve()
            if path.is_dir():
                path = path / "index.html"
        if (not path.is_relative_to(base) or not path.is_file()
                or any(part.startswith(".") for part in path.relative_to(base).parts)):
            self.send_error(404)
            return
        if path.suffix == ".html":
            self.respond(live_document(path.read_text(), version).encode(), "text/html")
            return
        media = "text/plain" if path.suffix in {".md", ".json"} else mimetypes.guess_type(path.name)[0]
        self.respond(path.read_bytes(), media or "application/octet-stream", requested.startswith("assets/"))

    def respond(self, data, media, immutable=False):
        self.send_response(200)
        self.send_header("Content-Type", media + ("; charset=utf-8" if media.startswith("text/") else ""))
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "public, max-age=31536000, immutable" if immutable else "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        try:
            if self.command != "HEAD":
                self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass


def render_loop(server):
    from playwright.sync_api import sync_playwright

    previous = None
    attempt = 0
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel="chromium")
            page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
            while not server.stop.is_set():
                current = fingerprint(server.root)
                if current != previous:
                    attempt += 1
                    site = server.output / f"generation-{attempt}"
                    site.mkdir()
                    with server.lock:
                        server.building = True
                    try:
                        style, logo = preview.prepare_assets(site, page, server.root)
                        count = preview.render_articles(
                            server.root, site, Path("."), "working-tree", "local",
                            page, style, logo, local=True,
                        )
                        server.assets.mkdir(exist_ok=True)
                        for asset in (site / "assets").iterdir():
                            if not (server.assets / asset.name).exists():
                                shutil.copyfile(asset, server.assets / asset.name)
                        shutil.rmtree(site / "assets")
                        with server.lock:
                            server.site = site
                            server.error = ""
                            server.version += 1
                        print(f"Preview updated: {count} articles", flush=True)
                    except Exception as error:
                        with server.lock:
                            server.error = str(error)
                            server.version += 1
                        shutil.rmtree(site)
                        print(f"Preview build failed: {error}", flush=True)
                    finally:
                        with server.lock:
                            server.building = False
                    previous = current
                server.stop.wait(0.5)
            browser.close()
    except Exception as error:
        with server.lock:
            server.error = str(error)
            server.building = False
        print(f"Preview server failed to render: {error}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preview the local working tree; rebuild and reload on save")
    parser.add_argument("--port", type=int, default=8000)
    options = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="lingcompute-preview-") as temporary:
        try:
            server = PreviewServer(ROOT, Path(temporary).resolve(), options.port)
        except OSError as error:
            parser.error(f"{error}; choose another port with --port")
        worker = threading.Thread(target=render_loop, args=(server,), daemon=True)
        worker.start()
        print(f"Local HTML preview: http://127.0.0.1:{server.server_port}/", flush=True)
        print("Watching content, images, sources, product metadata and styles; Ctrl+C to stop.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.stop.set()
            server.server_close()
            worker.join(timeout=15)
