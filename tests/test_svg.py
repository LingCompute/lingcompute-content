import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from tools import build, svg


class SVGTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.path = self.root / "diagram.svg"

    def write(self, body, attributes='viewBox="0 0 600 300"'):
        self.path.write_text(f'<svg xmlns="{svg.NAMESPACE}" {attributes}>{body}</svg>')

    def test_editable_text_geometry_and_local_references_survive(self):
        self.write(
            '<defs><linearGradient id="blue"><stop offset="0" stop-color="#0649AD"/>'
            '</linearGradient></defs><rect id="panel" width="600" height="300" fill="url(#blue)"/>'
            '<text x="20" y="40" style="font-size:24px;font-weight:500">光功率 κ &amp; P</text>'
            '<use href="#panel"/>'
        )
        output = svg.image(self.path, "图 1：光功率", 1)
        document = ET.fromstring(output)
        self.assertEqual(document.attrib["aria-label"], "图 1：光功率")
        self.assertEqual(document.attrib["font-family"], "MiSans, sans-serif")
        self.assertIn("光功率 κ &amp; P", output)
        self.assertIn('font-size="24px"', output)
        self.assertIn('fill="url(#figure-', output)
        self.assertNotIn('id="panel"', output)
        self.assertNotIn('href="#panel"', output)
        self.assertNotEqual(output, svg.image(self.path, "图 1：光功率", 2))

    def test_markdown_embeds_vector_after_caption_and_greek_processing(self):
        self.write('<text x="20" y="40">κ 中文</text>')
        output, parser = build.render_body("![图 1：矢量参数](diagram.svg)", self.root, self.root)
        self.assertIn("<figure><svg ", output)
        self.assertIn("<figcaption>", output)
        self.assertIn("κ 中文", output)
        self.assertNotIn('<span class="greek">', output)
        self.assertNotIn("vector:1", output)
        self.assertEqual(parser.assets, [self.path])
        self.assertEqual(parser.text, ["图 1：矢量参数"])
        self.assertNotIn("data:image/png", output)

    def test_scripts_foreign_content_and_global_styles_are_rejected(self):
        for body in (
            "<script>alert(1)</script>", '<rect onload="alert(1)"/>',
            '<foreignObject><p>html</p></foreignObject>',
            '<image href="data:image/png;base64,AAAA"/>',
            '<style>body{display:none}</style>', '<animate attributeName="x"/>',
            '<rect class="brand"/>', '<rect style="position:fixed"/>',
            '<rect xml:base="https://attacker.test/"/>',
            '<g xmlns:xlink="http://www.w3.org/1999/xlink" xlink:id="foreign"/>',
            '<a href="https://attacker.test/">link</a>',
        ):
            with self.subTest(body=body), self.assertRaises(ValueError):
                self.write(body)
                svg.image(self.path, "test", 1)

    def test_external_resources_and_obfuscated_css_are_rejected(self):
        for body in (
            '<use href="https://attacker.test/asset.svg#one"/>',
            '<use href="file:///etc/passwd"/>',
            '<use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="//attacker.test/one"/>',
            '<rect fill="url(https://attacker.test/one)"/>',
            '<rect fill="URL(//attacker.test/one)"/>',
            '<rect style="fill:u\\72l(https://attacker.test/one)"/>',
            '<rect style="fill:url(/*x*/https://attacker.test/one)"/>',
            '<rect fill="url(#missing)"/>', '<use href="#missing"/>',
        ):
            with self.subTest(body=body), self.assertRaises(ValueError):
                self.write(body)
                svg.image(self.path, "test", 1)

    def test_xml_entities_invalid_dimensions_ids_and_resource_limits_fail(self):
        sources = [
            '<!DOCTYPE svg [<!ENTITY x "secret">]><svg viewBox="0 0 1 1">&x;</svg>',
            '<svg viewBox="0 0 1 1"><!ENTITY x "secret"></svg>',
            "<html/>", "<svg/>", '<svg viewBox="0 0 nan 300"/>',
            '<svg viewBox="0 0 600 -1"/>', '<svg viewBox="0 0 1 1 1"/>',
            '<svg viewBox="0 0 1 1e100"/>',
            '<svg viewBox="0 0 1 1"><g id="same"/><g id="same"/></svg>',
            '<svg viewBox="0 0 1 1"><g id="bad id"/></svg>',
            '<svg viewBox="0 0 1 1">' + "<g/>" * 10000 + "</svg>",
            '<svg viewBox="0 0 1 1">' + "<g>" * 65 + "</g>" * 65 + "</svg>",
            " " * (2 * 1024 * 1024 + 1),
        ]
        for source in sources:
            with self.subTest(source=source[:100]), self.assertRaises(ValueError):
                self.path.write_text(source)
                svg.image(self.path, "test", 1)


if __name__ == "__main__":
    unittest.main()
