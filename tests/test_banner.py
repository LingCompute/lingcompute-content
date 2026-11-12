import tempfile
import unittest
from pathlib import Path

from tools import banner


class BannerTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def test_canvas_matches_the_published_layout(self):
        image = banner.banner("先把两个指标说清楚")
        self.assertEqual(image.size, banner.CANVAS)
        self.assertEqual(image.mode, "RGBA")

    def test_ribbon_widens_with_the_title_and_keeps_a_minimum(self):
        short = banner.banner("下期预告")
        long = banner.banner("仿真结果：分光比、透射与相位一起看")
        self.assertEqual(short.size, banner.CANVAS)
        self.assertLess(self._ribbon_width(short), self._ribbon_width(long))
        self.assertGreaterEqual(self._ribbon_width(short), banner.MIN_RIBBON - 4)

    def test_long_title_wraps_to_two_lines(self):
        image = banner.banner("仿真结果：分光比、透射与相位一起看，还要加上一段更长的说明文字")
        self.assertEqual(image.size, banner.CANVAS)

    def test_title_that_cannot_fit_two_lines_is_rejected(self):
        with self.assertRaises(ValueError):
            banner.banner("这是一个特别长的章节标题" * 4)

    def test_case_card_matches_the_published_layout(self):
        qr = self.root / "qr.png"
        from PIL import Image

        Image.new("RGB", (200, 200), "white").save(qr)
        card = banner.case_card("Y 分支：Waveguide Y junction", qr)
        self.assertEqual(card.size, (1080, 334))
        self.assertEqual(card.mode, "RGBA")

    def _ribbon_width(self, image):
        alpha = image.split()[3]
        columns = [
            x for x in range(image.width)
            if any(alpha.getpixel((x, y)) > 200 for y in range(0, image.height, 4))
        ]
        return max(columns) - min(columns)


if __name__ == "__main__":
    unittest.main()
