import hashlib
import tempfile
import unittest
from pathlib import Path

from tools import catalog


class CatalogTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        manuscript = self.root / "content/photon/example/one.md"
        manuscript.parent.mkdir(parents=True)
        manuscript.write_text("# title")
        self.article = {
            "path": manuscript, "key": "content/photon/example/one.md",
            "product": "photon", "series": "A series", "audience": "Engineers",
            "title": "New [article]", "summary": "One problem", "minutes": (9, 17), "assets": [],
        }
        self.products = {
            "photon": {"name": "Photon", "url": "https://example.com/photon"},
            "fluid": {"name": "Fluid", "url": "https://example.com/fluid"},
        }
        self.record = {
            "article": self.article["key"], "manuscript_sha256": hashlib.sha256(manuscript.read_bytes()).hexdigest(),
            "assets": [], "over_ten_screens": True,
        }

    def test_new_series_and_long_article_have_a_complete_reading_entry(self):
        output = catalog.render(self.products, [self.article], [self.record], self.root)
        for expected in (
            "#series-photon-example", "Engineers", "One problem", "9–17 分钟",
            "长文提示", "content/photon/example/one.md", "content/photon/example/SOURCES.md",
            "待首篇审核后收录", r"New \[article\]",
        ):
            self.assertIn(expected, output)

    def test_stale_or_incomplete_report_cannot_publish_catalog(self):
        for report in ([], [self.record, self.record]):
            with self.subTest(report=report), self.assertRaises(ValueError):
                catalog.render(self.products, [self.article], report, self.root)
        self.article["path"].write_text("# changed")
        with self.assertRaisesRegex(ValueError, "stale"):
            catalog.render(self.products, [self.article], [self.record], self.root)

    def test_readme_check_catches_missing_entries_and_preserves_other_text(self):
        readme = self.root / "README.md"
        readme.write_text("Brand\n" + catalog.BEGIN + "\nold\n" + catalog.END + "\nRules\n")
        with self.assertRaisesRegex(ValueError, "stale"):
            catalog.update(readme, "new entry", check=True)
        catalog.update(readme, "new entry")
        catalog.update(readme, "new entry", check=True)
        self.assertEqual(readme.read_text(), "Brand\n" + catalog.BEGIN + "\n\nnew entry\n\n" + catalog.END + "\nRules\n")
        readme.write_text("no markers")
        with self.assertRaises(ValueError):
            catalog.update(readme, "new entry")


if __name__ == "__main__":
    unittest.main()
