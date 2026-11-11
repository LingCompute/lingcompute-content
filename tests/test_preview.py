import base64
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import build, preview


class PreviewTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def test_snapshot_accepts_only_content_data_and_rejects_links(self):
        self.assertTrue(preview.source_file("100644", "blob", "content/photon/series/one.md"))
        self.assertTrue(preview.source_file("100644", "blob", "content/photon/series/figure.png"))
        self.assertFalse(preview.source_file("100644", "blob", "content/photon/series/run.py"))
        for mode, kind, path in (
            ("120000", "blob", "content/linked.png"),
            ("160000", "commit", "content/submodule"),
            ("100755", "blob", "content/run.md"),
            ("100644", "blob", "content/../../secret.md"),
            ("100644", "blob", "production/private.md"),
            ("100644", "blob", "/content/private.md"),
        ):
            with self.subTest(path=path), self.assertRaises(ValueError):
                preview.source_file(mode, kind, path)

    def test_snapshot_never_extracts_pr_tools_or_configuration(self):
        entries = (
            b"100644 blob abc 7\tcontent/photon/example/one.md\0"
            b"100644 blob def 7\tcontent/photon/example/run.py\0"
        )
        with patch.object(preview, "command", side_effect=[entries, b"# title"]) as command:
            preview.snapshot("a" * 40, self.root)
        self.assertEqual((self.root / "content/photon/example/one.md").read_text(), "# title")
        self.assertFalse((self.root / "content/photon/example/run.py").exists())
        self.assertEqual(command.call_count, 2)
        self.assertEqual((self.root / "config/products.json").read_bytes(),
                         (preview.ROOT / "config/products.json").read_bytes())

    def test_snapshot_size_limit_is_checked_before_writing(self):
        entries = f"100644 blob abc {preview.MAX_SOURCE_BYTES + 1}\tcontent/large.png\0".encode()
        with patch.object(preview, "command", return_value=entries) as command:
            with self.assertRaisesRegex(ValueError, "300 MiB"):
                preview.snapshot("a" * 40, self.root)
        self.assertEqual(command.call_count, 1)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_online_html_shares_assets_and_pins_preview_identity(self):
        style = preview.asset(self.root, b"body{color:black}", ".css")
        encoded = base64.b64encode(b"example raster").decode()
        output = build.document("Title", f'<article><img src="data:image/png;base64,{encoded}"></article>', "old style")
        target = self.root / "previews/7" / ("a" * 40) / "photon/example/one.html"
        preview.web_document(output, target, self.root, style, True)
        first = target.read_text()
        self.assertNotIn("<style>", first)
        self.assertNotIn(encoded, first)
        self.assertIn("noindex,nofollow", first)
        self.assertIn("img-src 'self' data:", first)
        self.assertIn("base-uri 'none'; form-action 'none'", first)
        self.assertIn("../../../../../assets/", first)
        preview.web_document(output, self.root / "index.html", self.root, style, False)
        self.assertNotIn("noindex", (self.root / "index.html").read_text())
        self.assertEqual(len(list((self.root / "assets").iterdir())), 2)
        banner = preview.notice("a" * 40, "b" * 40, 7)
        for expected in ("待审", "PR #7", "a" * 40, "b" * 40, "/pull/7"):
            self.assertIn(expected, banner)

    def test_article_source_links_use_snapshot_not_workflow_commit(self):
        series = self.root / "content/photon/example"
        series.mkdir(parents=True)
        (series / "SOURCES.md").write_text("source")
        rendered, _ = build.render_body("[source](SOURCES.md)", series, self.root, "a" * 40)
        self.assertIn("/blob/" + "a" * 40 + "/content/photon/example/SOURCES.md", rendered)

    def test_no_stale_or_closed_pr_gets_preview_status(self):
        records = [
            {"number": 1, "sha": "a" * 40},
            {"number": 2, "sha": "b" * 40},
            {"number": 3, "sha": "c" * 40},
        ]
        with patch.object(preview, "pulls", return_value=[
            {"number": 1, "head": {"sha": "d" * 40}},
            {"number": 2, "head": {"sha": "b" * 40}},
        ]):
            self.assertEqual(preview.current_records(records), [records[1]])

    def test_new_main_prevents_publishing_old_catalogue(self):
        (self.root / "previews.json").write_text(json.dumps({"main": "a" * 40, "renderer": "d" * 40, "pulls": []}))
        with patch.object(preview, "api", return_value={"sha": "b" * 40}), patch.object(preview, "command") as command:
            with self.assertRaisesRegex(ValueError, "Main advanced"):
                preview.publish(self.root)
        command.assert_not_called()

    def test_new_pr_revision_prevents_publishing_old_snapshot(self):
        (self.root / "previews.json").write_text(json.dumps({
            "main": "a" * 40, "renderer": "d" * 40,
            "pulls": [{"number": 1, "sha": "b" * 40, "path": f"previews/1/{'b' * 40}/", "state": "success"}],
        }))
        with patch.object(preview, "api", return_value={"sha": "a" * 40}), \
                patch.object(preview, "pulls", return_value=[]), \
                patch.object(preview, "command") as command:
            with self.assertRaisesRegex(ValueError, "PR changed"):
                preview.publish(self.root)
        command.assert_not_called()

    def test_deployment_rejects_executable_metadata_and_symlinks(self):
        manifest = {"main": "a" * 40, "renderer": "d" * 40, "pulls": []}
        (self.root / ".nojekyll").touch()
        (self.root / "index.html").write_text("page")
        preview.validate_site(self.root, manifest)
        unsafe = self.root / ".git"
        unsafe.mkdir()
        with self.assertRaisesRegex(ValueError, "hidden"):
            preview.validate_site(self.root, manifest)
        unsafe.rmdir()
        (self.root / "linked.html").symlink_to(self.root / "index.html")
        with self.assertRaisesRegex(ValueError, "Links"):
            preview.validate_site(self.root, manifest)

    def test_deployment_manifest_cannot_redirect_status_to_another_path(self):
        manifest = {
            "main": "a" * 40, "renderer": "d" * 40,
            "pulls": [{"number": 1, "sha": "b" * 40, "path": "//attacker.test/", "state": "success"}],
        }
        with self.assertRaisesRegex(ValueError, "manifest"):
            preview.validate_site(self.root, manifest)


if __name__ == "__main__":
    unittest.main()
