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
        self.assertTrue(preview.source_file("100644", "blob", "content/photon/series/figure.svg"))
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

    def test_online_preview_keeps_editable_inline_svg(self):
        series = self.root / "content/photon/example"
        series.mkdir(parents=True)
        (series / "figure.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50">'
            '<text x="10" y="20">可修改</text></svg>'
        )
        body, _ = build.render_body("![图 1：矢量图](figure.svg)", series, self.root)
        style = preview.asset(self.root, b"body{color:black}", ".css")
        target = self.root / "index.html"
        preview.web_document(build.document("test", body, ""), target, self.root, style, True)
        self.assertIn('class="vector-image"', target.read_text())
        self.assertIn("可修改", target.read_text())
        self.assertEqual(len(list((self.root / "assets").iterdir())), 1)

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

    def article(self, key):
        path = self.root / key
        return {"key": key, "path": path, "assets": [path.parent / "figures/one.png"]}

    def test_pr_scope_uses_file_changes_even_if_main_has_newer_articles(self):
        first = self.article("content/photon/example/one.md")
        unrelated = self.article("content/photon/another/two.md")
        changes = [{"filename": first["key"], "status": "modified"}]
        self.assertEqual(preview.affected_articles([first, unrelated], changes, self.root), [first])
        self.assertEqual(preview.removed_articles(changes), [])

    def test_image_metadata_and_evidence_changes_include_related_articles(self):
        first = self.article("content/photon/example/one.md")
        unrelated = self.article("content/photon/another/two.md")
        for path in ("figures/one.png", "series.json", "SOURCES.md"):
            with self.subTest(path=path):
                changes = [{"filename": "content/photon/example/" + path, "status": "modified"}]
                self.assertEqual(preview.affected_articles([first, unrelated], changes, self.root), [first])

    def test_changed_manuscripts_appear_before_related_articles(self):
        first = self.article("content/photon/example/one.md")
        second = self.article("content/photon/example/two.md")
        changes = [
            {"filename": second["key"], "status": "added"},
            {"filename": "content/photon/example/series.json", "status": "modified"},
        ]
        self.assertEqual(preview.affected_articles([first, second], changes, self.root), [second, first])

    def test_removed_and_renamed_articles_are_explicit_and_tools_do_not_select_content(self):
        first = self.article("content/photon/example/one.md")
        changes = [
            {"filename": "production/moved.md", "previous_filename": first["key"], "status": "renamed"},
            {"filename": "content/photon/example/two.md", "status": "removed"},
            {"filename": "content/photon/example/SOURCES.md", "status": "removed"},
        ]
        self.assertEqual(preview.removed_articles(changes), [
            "content/photon/example/one.md", "content/photon/example/two.md",
        ])
        self.assertEqual(preview.affected_articles([first], [{"filename": "tools/build.py", "status": "modified"}], self.root), [])

    def test_incomplete_or_stale_pr_diff_fails_closed(self):
        pull = {"number": 1, "head": {"sha": "a" * 40}}
        with patch.object(preview, "api", side_effect=[
            {"head": {"sha": "b" * 40}},
        ]), self.assertRaisesRegex(ValueError, "PR changed"):
            preview.pull_files(pull)
        with patch.object(preview, "api", side_effect=[
            {"head": {"sha": "a" * 40}, "changed_files": 2}, [{"filename": "one"}],
        ]), self.assertRaisesRegex(ValueError, "Incomplete"):
            preview.pull_files(pull)

    def test_pr_file_pagination_keeps_changes_after_the_first_hundred(self):
        pull = {"number": 1, "head": {"sha": "a" * 40}}
        first = [{"filename": f"content/photon/example/{index}.png"} for index in range(100)]
        last = [{"filename": "content/photon/example/one.md"}]
        with patch.object(preview, "api", side_effect=[
            {"head": {"sha": "a" * 40}, "changed_files": 101}, first, last,
        ]) as api:
            self.assertEqual(preview.pull_files(pull), first + last)
        self.assertIn("page=2", api.call_args.args[0])

    def test_site_build_finishes_catalogue_and_manifest_with_no_open_prs(self):
        site = self.root / "site"

        def main_snapshot(*arguments):
            (site / "index.html").write_text(build.document("main", "<article>main</article>", ""))
            return 1

        def assets(*arguments):
            return preview.asset(site, b"body{color:black}", ".css"), "logo"

        with patch.object(preview, "api", return_value={"sha": "a" * 40}), \
                patch.object(preview, "pulls", return_value=[]), \
                patch.object(preview, "command", return_value=("b" * 40).encode()), \
                patch.object(preview, "prepare_assets", side_effect=assets), \
                patch.object(preview, "render_snapshot", side_effect=main_snapshot), \
                patch("playwright.sync_api.sync_playwright"):
            preview.generate(site)
        manifest = json.loads((site / "previews.json").read_text())
        self.assertEqual(manifest, {"main": "a" * 40, "renderer": "b" * 40, "pulls": []})
        self.assertIn("待审预览目录", (site / "previews/index.html").read_text())
        preview.validate_site(site, manifest)


if __name__ == "__main__":
    unittest.main()
