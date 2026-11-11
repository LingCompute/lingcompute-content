import hashlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

from tools import fonts


class FontTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.cache = Path(temporary.name)
        self.data = b"original-font"
        self.weights = {"Regular": (400, hashlib.sha256(self.data).hexdigest())}

    def test_missing_or_changed_embedded_font_is_rejected(self):
        with patch.object(fonts, "WEIGHTS", self.weights):
            with self.assertRaisesRegex(ValueError, "fonts missing"):
                fonts.font_style(self.cache)
            (self.cache / "MiSans-Regular.woff2").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "fingerprint changed"):
                fonts.font_style(self.cache)

    def test_original_font_is_embedded_with_selected_weight(self):
        (self.cache / "MiSans-Regular.woff2").write_bytes(self.data)
        with patch.object(fonts, "WEIGHTS", self.weights):
            style = fonts.font_style(self.cache)
        self.assertIn("data:font/woff2;base64,b3JpZ2luYWwtZm9udA==", style)
        self.assertIn("font-weight:400", style)

    def test_download_validates_before_writing_and_reuses_verified_cache(self):
        buffer = io.BytesIO()
        with ZipFile(buffer, "w") as archive:
            archive.writestr("MiSans/woff2/MiSans-Regular.woff2", self.data)
        with (
            patch.object(fonts, "CACHE", self.cache),
            patch.object(fonts, "WEIGHTS", {"Regular": (400, "wrong")}),
            patch.object(fonts, "urlopen", return_value=io.BytesIO(buffer.getvalue())),
        ):
            with self.assertRaises(ValueError):
                fonts.install()
            self.assertFalse((self.cache / "MiSans-Regular.woff2").exists())
        with (
            patch.object(fonts, "CACHE", self.cache),
            patch.object(fonts, "WEIGHTS", self.weights),
            patch.object(fonts, "urlopen", return_value=io.BytesIO(buffer.getvalue())) as download,
        ):
            fonts.install()
            fonts.install()
            self.assertEqual(download.call_count, 1)
            self.assertEqual((self.cache / "MiSans-Regular.woff2").read_bytes(), self.data)


if __name__ == "__main__":
    unittest.main()
