import argparse
import base64
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path, PurePosixPath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPO = "LingCompute/lingcompute-content"
REPOSITORY = f"https://github.com/{REPO}"
SITE_URL = "https://lingcompute.github.io/lingcompute-content"
MAX_SOURCE_BYTES = 300 * 1024 * 1024
SHA = re.compile(r"[0-9a-f]{40}")
CREDITS = (
    '<footer class="brand">默认系统字体；备用字体：'
    '<a href="https://hyperos.mi.com/font/en/download/">MiSans（小米）</a>，按其字体许可使用。</footer>'
)


def command(*arguments, cwd=ROOT, data=None):
    return subprocess.check_output(arguments, cwd=cwd, input=data)


def api(path, data=None):
    arguments = ["gh", "api", f"repos/{REPO}/{path}"]
    if data is not None:
        arguments += ["--method", "POST", "--input", "-"]
    return json.loads(command(*arguments, data=json.dumps(data).encode() if data is not None else None))


def pulls():
    result = []
    page = 1
    while True:
        batch = api(f"pulls?state=open&base=main&per_page=100&page={page}")
        result.extend(batch)
        if len(batch) < 100:
            return result
        page += 1


def source_file(mode, kind, name):
    path = PurePosixPath(name)
    if (mode != "100644" or kind != "blob" or path.is_absolute()
            or ".." in path.parts or not path.parts or path.parts[0] != "content"):
        raise ValueError(f"Unsafe content entry: {name}")
    return path.suffix.lower() in {".md", ".json", ".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"}


def snapshot(commit, destination):
    if not SHA.fullmatch(commit):
        raise ValueError("Expected a full source commit SHA")
    entries = command("git", "ls-tree", "-rlz", commit, "--", "content").split(b"\0")
    selected = []
    total = 0
    for entry in filter(None, entries):
        metadata, name = entry.decode().split("\t", 1)
        mode, kind, object_id, size = metadata.split()
        if source_file(mode, kind, name):
            total += int(size)
            selected.append((object_id, name))
    if total > MAX_SOURCE_BYTES:
        raise ValueError("Content snapshot exceeds the 300 MiB preview limit")
    for object_id, name in selected:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(command("git", "cat-file", "blob", object_id))
    (destination / "config").mkdir()
    shutil.copyfile(ROOT / "config/products.json", destination / "config/products.json")


def pull_files(pull):
    detail = api(f"pulls/{pull['number']}")
    if detail["head"]["sha"] != pull["head"]["sha"]:
        raise ValueError("PR changed while loading its file list")
    files = []
    page = 1
    while True:
        batch = api(f"pulls/{pull['number']}/files?per_page=100&page={page}")
        files.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    if len(files) != detail["changed_files"]:
        raise ValueError("Incomplete PR file list")
    return files


def affected_articles(articles, changes, root):
    paths = {
        name for change in changes
        for name in (change["filename"], change.get("previous_filename", change["filename"]))
    }
    selected = []
    for article in articles:
        series = PurePosixPath(article["key"]).parent
        dependencies = {
            article["key"], str(series / "series.json"), str(series / "SOURCES.md"),
            *(path.relative_to(root).as_posix() for path in article["assets"]),
        }
        if paths.intersection(dependencies) or any(PurePosixPath(path).parent == PurePosixPath("content") for path in paths):
            selected.append(article)
    return sorted(selected, key=lambda article: (article["key"] not in paths, article["key"]))


def removed_articles(changes):
    removed = set()
    for change in changes:
        names = [change["filename"]] if change["status"] == "removed" else []
        if change["status"] == "renamed":
            names.append(change["previous_filename"])
        for name in names:
            path = PurePosixPath(name)
            if (len(path.parts) == 4 and path.parts[0] == "content" and path.suffix == ".md"
                    and path.name not in {"README.md", "SOURCES.md"}):
                removed.add(name)
    return sorted(removed)


def asset(site, data, suffix):
    name = hashlib.sha256(data).hexdigest() + suffix
    target = site / "assets" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_bytes(data)
    return target


def web_document(output, destination, site, style_path, draft):
    prefix = os.path.relpath(site, destination.parent).replace(os.sep, "/")
    stylesheet = f"{prefix}/assets/{style_path.name}"
    output = re.sub(r"<style>.*?</style>",
                    f'<link rel="stylesheet" href="{stylesheet}">', output, count=1, flags=re.S)
    output = output.replace("img-src data:;", "img-src 'self' data:;")
    output = output.replace("style-src 'unsafe-inline'", "style-src 'self' 'unsafe-inline'; base-uri 'none'; form-action 'none'")

    def image(match):
        media, encoded = match.groups()
        data = base64.b64decode(encoded, validate=True)
        target = asset(site, data, "." + ("jpg" if media == "jpeg" else media))
        return f'src="{prefix}/assets/{target.name}"'

    output = re.sub(r'src="data:image/(png|jpeg|gif|webp);base64,([^"]+)"', image, output)
    if draft:
        output = output.replace("</head>", '<meta name="robots" content="noindex,nofollow"></head>')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output)


def notice(commit, renderer, number=None, local=False):
    if local:
        return '<aside class="meta"><strong>本地实时预览 · 未提交工作区</strong><p>保存后自动重建；此页面不是人审或发布记录。</p></aside>'
    title = f"待审预览 · PR #{number}" if number else "正式内容 · 主分支"
    target = f"{REPOSITORY}/pull/{number}" if number else f"{REPOSITORY}/tree/{commit}"
    warning = "此版本尚待人审，不能作为发布批准。" if number else "正式收录不等于已经在公众号发送。"
    return (
        f'<aside class="meta"><p><strong>{title}</strong> · <a href="{target}">GitHub 记录</a></p>'
        f'<p>{warning}</p><details><summary>版本信息 · 源稿 {commit[:7]}</summary>'
        f'<p>源稿版本：<code>{commit}</code></p>'
        f'<p>排版工具版本：<code>{renderer}</code>。工具改动合并后生效。</p></details></aside>'
    )


def prepare_assets(site, page, root=ROOT):
    try:
        from . import build
    except ImportError:
        import build

    style = build.font_style(root / ".cache/fonts") + "\n" + (root / "tools/style.css").read_text()
    style_path = asset(site, style.encode(), ".css")
    svg = base64.b64encode((root / "assets/brand/lingcompute-horizontal.svg").read_bytes()).decode()
    page.set_content(f'<img src="data:image/svg+xml;base64,{svg}" style="width:720px;height:auto">')
    logo = "data:image/png;base64," + base64.b64encode(page.locator("img").screenshot(omit_background=True)).decode()
    return style_path, logo


def render_snapshot(site, directory, commit, renderer, page, style_path, logo, number=None, changes=None):
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary).resolve()
        snapshot(commit, root)
        return render_articles(root, site, directory, commit, renderer, page, style_path, logo, number, changes)


def render_articles(root, site, directory, commit, renderer, page, style_path, logo,
                    number=None, changes=None, local=False):
    try:
        from . import build
    except ImportError:
        import build

    source_base = "/__preview__/source" if local else f"{REPOSITORY}/blob/{commit}"
    products, articles = build.read_articles(root, commit, source_base)
    if changes is not None:
        articles = affected_articles(articles, changes, root)
    ledger = json.loads((ROOT / "reviews/legacy.json").read_text())
    banner = notice(commit, renderer, number, local)
    cards = []
    direct = {change["filename"] for change in changes or []}
    for article in articles:
        relative = article["path"].relative_to(root / "content").with_suffix(".html")
        destination = site / directory / relative
        back = os.path.relpath(site / directory / "index.html", destination.parent).replace(os.sep, "/")
        navigation = f'<a href="{back}">返回文章目录</a>'

        def render(screens=None):
            output = build.article_html(
                article, products, "", logo, build.legacy_review(article, ledger, root),
                screens, navigation, root, commit, banner, source_base,
            )
            web_document(output, destination, site, style_path, number is not None or local)

        render()
        page.goto(destination.as_uri(), wait_until="load")
        page.evaluate("async () => { await document.fonts.ready; await Promise.all(Array.from(document.images, image => image.decode())); }")
        screens = page.locator("#article-body").evaluate("element => element.getBoundingClientRect().height / 844")
        render(screens)
        page.goto(destination.as_uri(), wait_until="load")
        page.evaluate("async () => { await document.fonts.ready; await Promise.all(Array.from(document.images, image => image.decode())); }")
        if page.evaluate("document.documentElement.scrollWidth > innerWidth + 1"):
            raise ValueError(f"Horizontal overflow: {article['key']}")
        screenshot_link = ""
        if not local:
            screenshot = asset(site, page.screenshot(full_page=True, animations="disabled"), ".png")
            screen_link = os.path.relpath(screenshot, site / directory).replace(os.sep, "/")
            screenshot_link = f'<a href="{screen_link}">手机长图</a> · '
        lower, upper = article["minutes"]
        warning = " · 长文提示：超过10参考屏，建议分段阅读" if screens > 10 else ""
        source = f"{source_base}/{quote(article['key'])}"
        relation = ("正文变更 · " if article["key"] in direct else "关联文章 · ") if number else ""
        cards.append(
            f'<section class="card"><h2><a href="{quote(relative.as_posix())}">{html.escape(article["title"])}</a></h2>'
            f'<p>{relation}{html.escape(article["series"])} · {html.escape(article["summary"])}</p>'
            f'<p>预计 {lower}–{upper} 分钟 · {screens:.1f} 参考屏{warning}</p>'
            f'<p>{screenshot_link}<a href="{source}">Markdown 源稿</a></p></section>'
        )
    removed = removed_articles(changes or [])
    if removed:
        cards.append("<section><h2>此 PR 删除或移走的文章</h2><ul>"
                     + "".join(f"<li>{html.escape(key)}</li>" for key in removed) + "</ul></section>")
    title = "本地实时预览" if local else f"PR #{number} · 待审文章" if number else "灵算技术内容库"
    message = "" if cards else "<p>此 PR 未改动文章或关联素材。工具和样式改动请查看 Content CI 附件。</p>"
    if number:
        changed_content = [change for change in changes or [] if any(
            name.startswith("content/") for name in (change["filename"], change.get("previous_filename", ""))
        )]
        scope = "".join(f'<li>{html.escape(change["status"])} · {html.escape(change["filename"])}</li>'
                        for change in changed_content)
        message += (f'<p>按此 PR 的实际文件差异生成，包含正文及受图片、来源或目录变更影响的关联文章。'
                    f'<a href="{REPOSITORY}/pull/{number}/files">查看文件差异</a></p>'
                    f'<details><summary>内容改动范围（{len(changed_content)} 个文件）</summary><ul>{scope}</ul></details>')
    home = os.path.relpath(site / "index.html", site / directory).replace(os.sep, "/")
    output = build.document(
        title, f'<article>{banner}<h1>{title}</h1>{message}{"".join(cards)}'
        f'<nav><a href="{home}">{"本地目录" if local else "正式内容首页"}</a></nav>{CREDITS}</article>', "",
    )
    web_document(output, site / directory / "index.html", site, style_path, number is not None or local)
    return len(articles)


def generate(site):
    from playwright.sync_api import Error, sync_playwright
    try:
        from . import build
    except ImportError:
        import build

    if site.exists():
        raise ValueError("Preview output must be a new directory")
    site.mkdir(parents=True)
    renderer = command("git", "rev-parse", "HEAD").decode().strip()
    main = api("commits/main")["sha"]
    pending = pulls()
    command("git", "fetch", "--no-tags", "origin", "main",
            *(f"refs/pull/{pull['number']}/head" for pull in pending))
    records = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chromium")
        page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
        style_path, logo = prepare_assets(site, page)
        count = render_snapshot(site, Path("."), main, renderer, page, style_path, logo)
        print(f"main {main[:7]}: {count} articles", flush=True)
        for pull in pending:
            number, commit = pull["number"], pull["head"]["sha"]
            if not isinstance(number, int) or number < 1 or not SHA.fullmatch(commit):
                raise ValueError("Invalid PR identity")
            directory = Path("previews") / str(number) / commit
            record = {"number": number, "sha": commit, "path": directory.as_posix() + "/"}
            try:
                changes = pull_files(pull)
                count = render_snapshot(site, directory, commit, renderer, page, style_path, logo, number, changes)
                record["state"] = "success"
                record["articles"] = count
                print(f"PR #{number} {commit[:7]}: {count} changed articles", flush=True)
            except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError, Error) as error:
                shutil.rmtree(site / directory, ignore_errors=True)
                record["state"] = "failure"
                record["error"] = str(error)[:500]
                print(f"PR #{number}: preview failed: {error}", flush=True)
            records.append(record)
        browser.close()
    cards = []
    for record in records:
        title = f"PR #{record['number']} · {record['sha'][:7]}"
        if record["state"] == "success":
            cards.append(f'<li><a href="{record["path"].removeprefix("previews/")}">{title}</a> · {record["articles"]} 篇变更</li>')
        else:
            cards.append(f'<li>{title} · 构建失败：{html.escape(record["error"])}</li>')
    output = build.document(
        "待审预览目录", '<article><h1>待审预览目录</h1><p>以下版本尚待人审；预览生成不代表批准。'
        '只保留开放 PR 的当前快照，旧链接可能失效。</p><ul>' + "".join(cards)
        + f'</ul><nav><a href="../">正式内容首页</a></nav>{CREDITS}</article>', "",
    )
    web_document(output, site / "previews/index.html", site, style_path, True)
    index = site / "index.html"
    index.write_text(index.read_text().replace("</nav>", '<a href="previews/">待审 PR 预览</a></nav>'))
    (site / "previews.json").write_text(json.dumps({"main": main, "renderer": renderer, "pulls": records}, ensure_ascii=False, indent=2) + "\n")
    (site / ".nojekyll").touch()
    (site / "robots.txt").write_text("User-agent: *\nDisallow: /lingcompute-content/previews/\n")
    size = sum(path.stat().st_size for path in site.rglob("*") if path.is_file())
    if size > 900 * 1024 * 1024:
        raise ValueError("Generated site exceeds the 900 MiB budget")
    print(f"Site: {size / 1024 ** 2:.1f} MiB", flush=True)


def current_records(records):
    current = {pull["number"]: pull["head"]["sha"] for pull in pulls()}
    return [record for record in records if current.get(record["number"]) == record["sha"]]


def validate_site(site, manifest):
    for key in ("main", "renderer"):
        if not SHA.fullmatch(manifest[key]):
            raise ValueError("Invalid site source identity")
    numbers = set()
    for record in manifest["pulls"]:
        number, commit = record["number"], record["sha"]
        if (type(number) is not int or number < 1 or number in numbers or not SHA.fullmatch(commit)
                or record["path"] != f"previews/{number}/{commit}/"
                or record["state"] not in {"success", "failure"}):
            raise ValueError("Invalid preview manifest")
        numbers.add(number)
    for path in site.rglob("*"):
        if path.is_symlink() or any(part.startswith(".") for part in path.relative_to(site).parts):
            if path == site / ".nojekyll" and path.is_file() and not path.is_symlink():
                continue
            raise ValueError("Links and hidden paths are not allowed in a Pages artifact")
        if path.is_file() and path.suffix not in {".html", ".css", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".json", ".txt"}:
            raise ValueError(f"Unexpected Pages asset: {path.name}")


def publish(site):
    manifest = json.loads((site / "previews.json").read_text())
    validate_site(site, manifest)
    if api("commits/main")["sha"] != manifest["main"]:
        raise ValueError("Main advanced during the build; rerun the preview workflow")
    records = current_records(manifest["pulls"])
    if len(records) != len(manifest["pulls"]):
        raise ValueError("A PR changed or closed during the build; rerun the preview workflow")
    with tempfile.TemporaryDirectory() as temporary:
        checkout = Path(temporary)

        def git(*arguments):
            return command("git", "-c", "credential.helper=", "-c",
                           "credential.helper=!gh auth git-credential", *arguments, cwd=checkout)

        git("init", "--initial-branch=gh-pages")
        git("remote", "add", "origin", REPOSITORY + ".git")
        exists = git("ls-remote", "--heads", "origin", "gh-pages").strip()
        if exists:
            git("fetch", "--depth=1", "origin", "gh-pages")
            git("checkout", "-B", "gh-pages", "FETCH_HEAD")
            for path in checkout.iterdir():
                if path.name != ".git":
                    if path.is_dir() and not path.is_symlink():
                        shutil.rmtree(path)
                    else:
                        path.unlink()
        shutil.copytree(site, checkout, dirs_exist_ok=True)
        git("add", "--all")
        git("-c", "user.name=github-actions[bot]", "-c",
            "user.email=41898282+github-actions[bot]@users.noreply.github.com",
            "commit", "--allow-empty", "-m", f"Publish HTML previews for {manifest['main'][:7]}")
        commit = git("rev-parse", "HEAD").decode().strip()
        git("push", "origin", "HEAD:gh-pages")
    api("pages/builds", {})
    for attempt in range(90):
        result = api("pages/builds/latest")
        if result.get("commit") == commit:
            if result["status"] == "built":
                break
            if result["status"] == "errored":
                raise ValueError(f"Pages build failed: {result.get('error')}")
        time.sleep(10)
    else:
        raise TimeoutError("Pages deployment did not finish in 15 minutes")
    for record in current_records(records):
        target = SITE_URL + "/" + (record["path"] if record["state"] == "success" else "previews/")
        api(f"statuses/{record['sha']}", {
            "state": record["state"], "context": "html-preview", "target_url": target,
            "description": (f"HTML 预览：{record['articles']} 篇正文或关联文章（待审）"
                            if record["state"] == "success" else "HTML preview failed · see preview index"),
        })
    print(f"Published {SITE_URL}/ and {len(records)} PR preview statuses", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["build", "publish"])
    parser.add_argument("--output", type=Path, default=ROOT / "build/site")
    options = parser.parse_args()
    (generate if options.operation == "build" else publish)(options.output.resolve())
