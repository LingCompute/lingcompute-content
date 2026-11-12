import http.client
import json
import tempfile
import threading
import unittest
from pathlib import Path

from tools import build, dev


class DevTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.content = self.root / "content/photon/example"
        self.content.mkdir(parents=True)
        self.manuscript = self.content / "one.md"
        self.manuscript.write_text("# original")

    def test_watcher_detects_edits_additions_and_deletions_but_ignores_production(self):
        original = dev.fingerprint(self.root)
        self.manuscript.write_text("# modified")
        changed = dev.fingerprint(self.root)
        self.assertNotEqual(changed, original)
        evidence = self.content / "SOURCES.md"
        evidence.write_text("source")
        self.assertNotEqual(dev.fingerprint(self.root), changed)
        evidence.unlink()
        self.assertEqual(dev.fingerprint(self.root), changed)
        (self.root / "production").mkdir()
        (self.root / "production/private.md").write_text("private")
        self.assertEqual(dev.fingerprint(self.root), changed)

    def test_brand_assets_trigger_rebuild(self):
        original = dev.fingerprint(self.root)
        brand = self.root / "assets/brand"
        brand.mkdir(parents=True)
        (brand / "wechat-signature.png").write_bytes(b"png")
        self.assertNotEqual(dev.fingerprint(self.root), original)
        (brand / "wechat-signature.png").write_bytes(b"png2")
        self.assertNotEqual(dev.fingerprint(self.root), original)

    def test_only_local_responses_receive_live_reload_script_and_csp(self):
        document = build.document("test", "<article>body</article>", "")
        live = dev.live_document(document, 7)
        self.assertIn("script-src 'self'; connect-src 'self';", live)
        self.assertIn('/__preview__/live.js?v=7', live)
        self.assertIn('role="status"', live)
        self.assertNotIn("script-src", document)
        self.assertNotIn("live.js", document)

    def test_working_tree_source_links_do_not_point_to_uncommitted_github_paths(self):
        (self.content / "SOURCES.md").write_text("current draft evidence")
        body, _ = build.render_body(
            "[source](SOURCES.md)", self.content, self.root,
            "working-tree", "/__preview__/source",
        )
        self.assertIn("/__preview__/source/content/photon/example/SOURCES.md", body)
        self.assertNotIn("github.com", body)

    def start_server(self):
        output = self.root / "output"
        output.mkdir()
        site = output / "generation-1"
        site.mkdir()
        (site / "index.html").write_text(build.document("test", "<article>current draft</article>", ""))
        server = dev.PreviewServer(self.root, output, 0)
        server.site = site
        server.building = False
        server.version = 1
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        return server

    def request(self, server, path, host=None):
        connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=3)
        connection.request("GET", path, headers={"Host": host} if host else {})
        response = connection.getresponse()
        result = response.status, dict(response.getheaders()), response.read()
        connection.close()
        return result

    def test_server_serves_generated_html_state_and_plain_text_local_sources(self):
        server = self.start_server()
        status, headers, body = self.request(server, "/")
        self.assertEqual(status, 200)
        self.assertIn(b"live.js?v=1", body)
        self.assertEqual(headers["Cache-Control"], "no-store")
        status, _, body = self.request(server, "/__preview__/state")
        self.assertEqual(json.loads(body), {"version": 1, "error": "", "building": False})
        status, headers, body = self.request(server, "/__preview__/source/content/photon/example/one.md")
        self.assertEqual(status, 200)
        self.assertEqual(body, b"# original")
        self.assertIn("text/plain", headers["Content-Type"])
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")

    def test_server_rejects_directory_listing_secrets_traversal_and_foreign_hosts(self):
        server = self.start_server()
        (self.root / ".env").write_text("secret")
        (server.site / "empty").mkdir()
        (server.site / "escape").symlink_to(self.root)
        for path in (
            "/.env", "/.git/config", "/empty/", "/escape/.env",
            "/__preview__/source/content/../../../.env",
            "/__preview__/source/content/%2e%2e/%2e%2e/.env",
        ):
            with self.subTest(path=path):
                self.assertEqual(self.request(server, path)[0], 404)
        self.assertEqual(self.request(server, "/", "attacker.example")[0], 403)

    def test_svg_source_is_watched_and_served_as_inert_text(self):
        original = dev.fingerprint(self.root)
        image = self.content / "figure.svg"
        image.write_text('<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>')
        self.assertNotEqual(original, dev.fingerprint(self.root))
        server = self.start_server()
        status, headers, body = self.request(server, "/__preview__/source/content/photon/example/figure.svg")
        self.assertEqual(status, 200)
        self.assertIn("text/plain", headers["Content-Type"])
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(body, image.read_bytes())

    def test_last_successful_page_remains_available_after_a_build_error(self):
        server = self.start_server()
        with server.lock:
            server.error = "missing image"
            server.version = 2
        status, _, body = self.request(server, "/")
        self.assertEqual(status, 200)
        self.assertIn(b"current draft", body)
        status, _, body = self.request(server, "/__preview__/state")
        self.assertEqual(json.loads(body)["error"], "missing image")


if __name__ == "__main__":
    unittest.main()
