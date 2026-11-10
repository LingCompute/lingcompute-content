import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from tools import build


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.series = self.root / "content/photon/example"
        self.series.mkdir(parents=True)
        self.image = self.series / "figure.png"
        Image.new("RGB", (10, 10), "white").save(self.image)

    def test_image_caption_and_equation_survive_sanitizing(self):
        rendered, parser = build.render_body(
            '# 标题\n\n![图 1：参数示例](figure.png)\n\n<p class="eq">κ<sub>ref</sub> = 1</p>',
            self.series, self.root,
        )
        self.assertIn("<figcaption>", rendered)
        self.assertIn("参数示例", rendered)
        self.assertIn("<sub>ref</sub>", rendered)
        self.assertEqual(parser.equations, 1)
        self.assertEqual(parser.assets, [self.image])

    def test_scripts_events_and_unsafe_links_are_removed(self):
        rendered, _ = build.render_body(
            '<script>alert(1)</script><img src="figure.png" alt="图" onerror="alert(2)">'
            '<a href="javascript:alert(3)" onclick="alert(4)">链接</a>'
            '<iframe src="https://example.com"></iframe>',
            self.series, self.root,
        )
        for forbidden in ("<script", "onerror", "onclick", "javascript:", "<iframe"):
            self.assertNotIn(forbidden, rendered)

    def test_path_traversal_symlinks_and_cross_series_images_fail(self):
        outside = self.root / "private.png"
        Image.new("RGB", (10, 10)).save(outside)
        (self.series / "link.png").symlink_to(outside)
        with self.subTest("outside repository"), self.assertRaises(ValueError):
            build.local_path(self.series, "../../../../outside.png", self.root)
        for reference in ("../../../private.png", "link.png", "/etc/passwd", "https://example.com/a.png"):
            with self.subTest(reference=reference), self.assertRaises(ValueError):
                build.render_body(f"![图]({reference})", self.series, self.root)
        (self.series / "private.txt").write_text("not an image")
        with self.assertRaises(ValueError):
            build.render_body("![图](private.txt)", self.series, self.root)

    def test_relative_links_are_validated_and_resolve_in_export(self):
        (self.series / "SOURCES.md").write_text("来源")
        rendered, _ = build.render_body("[来源](SOURCES.md#条件)", self.series, self.root)
        self.assertIn(f"/blob/{build.SOURCE_REF}/content/photon/example/SOURCES.md#%E6%9D%A1%E4%BB%B6", rendered)
        with self.assertRaises(ValueError):
            build.render_body("[缺失](missing.md)", self.series, self.root)

    def test_reading_estimate_includes_figures_and_equations(self):
        lower, upper = build.reading_minutes("中" * 900, 0, 0)
        self.assertEqual((lower, upper), (2, 4))
        with_figures = build.reading_minutes("中" * 900, 6, 12)
        self.assertGreater(with_figures[0], lower)
        self.assertGreater(with_figures[1], upper)
        self.assertEqual(build.reading_minutes("", 0, 0), (1, 2))

    def test_historical_approval_is_bound_to_text_and_assets(self):
        manuscript = self.series / "one.md"
        manuscript.write_text("# 正文")
        key = manuscript.relative_to(self.root).as_posix()
        article = {"key": key, "path": manuscript, "assets": [self.image]}
        record = {
            key: {
                "manuscript_sha256": build.digest(manuscript),
                "assets": {self.image.relative_to(self.root).as_posix(): build.digest(self.image)},
            }
        }
        self.assertTrue(build.legacy_review(article, record, self.root))
        manuscript.write_text("# 修改正文")
        self.assertFalse(build.legacy_review(article, record, self.root))
        manuscript.write_text("# 正文")
        Image.new("RGB", (10, 10), "black").save(self.image)
        self.assertFalse(build.legacy_review(article, record, self.root))

    def test_manifest_must_list_every_manuscript_exactly_once(self):
        (self.root / "config").mkdir()
        (self.root / "config/products.json").write_text(json.dumps({"photon": {"name": "光子"}}))
        (self.series / "SOURCES.md").write_text("来源")
        (self.series / "one.md").write_text("# 标题")
        manifest = {
            "product": "photon", "title": "系列", "audience": "工程师",
            "articles": [{"slug": "one", "authors": [], "summary": "问题", "sources": ["https://example.com"]}],
        }
        (self.series / "series.json").write_text(json.dumps(manifest))
        self.assertEqual(len(build.read_articles(self.root)[1]), 1)
        (self.series / "unlisted.md").write_text("# 遗漏")
        with self.assertRaises(ValueError):
            build.read_articles(self.root)

    def test_series_directory_cannot_inject_html(self):
        (self.root / "config").mkdir()
        (self.root / "config/products.json").write_text(json.dumps({"photon": {"name": "光子"}}))
        malicious = self.series.with_name('example"><style>')
        self.series.rename(malicious)
        (malicious / "series.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "Invalid series directory"):
            build.read_articles(self.root)


if __name__ == "__main__":
    unittest.main()
