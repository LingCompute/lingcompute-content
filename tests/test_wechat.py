import json
import re
import unittest
from pathlib import Path

from tools import wechat

ROOT = Path(__file__).resolve().parents[1]
STUB = "data:image/png;base64,iVBORw0KGgo="

SAMPLE = """
<h1>标题不进正文</h1>
<h2>章节标题</h2>
<p>正文段落，带<strong>强调</strong>与<span class="greek">κ</span>。</p>
<p class="eq">Δφ = 2κL</p>
<p class="note">脚注说明。</p>
<figure><img alt="图 1：示意" src="data:image/png;base64,AA"><figcaption><span class="fig-tag">图 1</span>示意</figcaption></figure>
<ul><li>· 列表项</li></ul>
<table><thead><tr><th>a</th><th>b</th><th>c</th></tr></thead>
<tbody><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5</td><td>6</td></tr></tbody></table>
"""


def without_media(css):
    """去掉 @media / @print 块：手机断点的取值与公众号稿无关。"""
    out, index = [], 0
    while True:
        start = css.find("@", index)
        if start < 0:
            out.append(css[index:])
            return "".join(out)
        out.append(css[index:start])
        depth, cursor = 0, css.find("{", start)
        while cursor < len(css):
            if css[cursor] == "{":
                depth += 1
            elif css[cursor] == "}":
                depth -= 1
                if depth == 0:
                    break
            cursor += 1
        index = cursor + 1


def render(source=SAMPLE, vectors=()):
    return wechat.render(
        source, banners=lambda text: STUB, vectors=vectors, case=("案例", STUB),
        follow=STUB, signature=STUB, cta=STUB,
    )


class ThemeTests(unittest.TestCase):
    def test_every_element_style_is_a_declaration_list(self):
        for name, declarations in wechat.theme()["elements"].items():
            with self.subTest(element=name):
                self.assertTrue(declarations, f"{name} 没有声明")
                for prop, value in declarations.items():
                    self.assertNotIn(";", prop)
                    self.assertFalse(prop.startswith("-"), "不要依赖浏览器前缀")
                    self.assertTrue(str(value).strip())

    def test_tokens_cover_every_placeholder(self):
        theme = wechat.theme()
        used = set()
        for declarations in theme["elements"].values():
            for value in declarations.values():
                used.update(re.findall(r"\{([a-z-]+)\}", value))
        self.assertEqual(used - set(theme["tokens"]), set())

    def test_published_values_are_the_ones_we_ship(self):
        style = wechat.styles()
        self.assertIn("font-size:15px", style["p"])
        self.assertIn("margin:17px 0", style["p"])
        self.assertIn("font-size:18px", style["h3"], "公众号稿的 h3 要顶到 18px，与发布版一致")
        self.assertIn("border-left:4px solid #2E7FD1", style["h3"])
        self.assertIn("font-size:16px", style["eq"])
        self.assertIn("background:#F6FAFE", style["eq"])
        self.assertIn("font-size:14.5px", style["table"])
        self.assertIn("font-size:13px", style["th"])
        self.assertIn("font-size:14px", style["note"])

    def test_doc_lists_every_element(self):
        doc = (ROOT / "docs/wechat-template.md").read_text()
        for name in wechat.theme()["elements"]:
            with self.subTest(element=name):
                self.assertIn(f"`{name}`", doc, f"{name} 没有写进 docs/wechat-template.md")

    def test_theme_matches_preview_css(self):
        css = without_media((ROOT / "tools/style.css").read_text())
        variables = dict(re.findall(r"(--[a-z-]+):(#[0-9A-Fa-f]{6})", css))

        def value(raw):
            return re.sub(r"var\((--[a-z-]+)\)", lambda m: variables[m.group(1)], raw).strip()

        rules = {}
        for selector, body in re.findall(r"(?m)^([^@{}\n][^{}]*)\{([^{}]*)\}", css):
            for one in selector.split(","):
                declarations = {}
                for part in body.split(";"):
                    prop, _, val = part.partition(":")
                    if prop.strip():
                        declarations[prop.strip()] = value(val)
                rules.setdefault(one.strip(), {}).update(declarations)

        theme = wechat.theme()["elements"]
        tokens = wechat.theme()["tokens"]
        shared = {
            "p": ("font-size", "line-height", "margin"),
            "figcaption": ("font-size", "line-height", "margin-top"),
            "fig-tag": ("font-size", "padding", "border-radius", "letter-spacing"),
            "eq": ("font-size", "line-height", "background", "border-left", "padding"),
            "table": ("font-size", "line-height", "border-collapse"),
            "th": ("font-size", "padding", "border-bottom", "font-weight"),
            "td": ("padding", "border-bottom", "vertical-align"),
        }
        for element, properties in shared.items():
            selector = f".{element}" if element in {"fig-tag", "eq"} else element
            for prop in properties:
                with self.subTest(element=element, property=prop):
                    expected = re.sub(r"\{([a-z-]+)\}", lambda m: tokens[m.group(1)], theme[element][prop])
                    # 预览稿里正文字号与行高由 body 继承，元素上不重复声明
                    actual = rules[selector].get(prop, rules["body"].get(prop))
                    self.assertEqual(actual, expected)


class RenderTests(unittest.TestCase):
    def test_headings_become_banners_and_the_title_is_dropped(self):
        page = render()
        self.assertNotIn("<h1", page)
        self.assertNotIn("<h2", page)
        self.assertIn('alt="章节：章节标题"', page)
        self.assertIn("margin-top:40px", page)
        self.assertEqual(page.count("<h3"), 0)

    def test_h3_keeps_the_rule_and_sixty_eighteen(self):
        page = render("<h3>小节</h3>")
        self.assertIn("font-size:18px", page)
        self.assertIn("border-left:4px solid #2E7FD1", page)

    def test_classes_are_inlined_and_removed(self):
        page = render()
        self.assertNotIn("class=", page)
        self.assertIn("font-size:16px", page)  # 公式卡片
        self.assertIn("font-style:italic", page)

    def test_list_items_get_a_marker_because_wechat_drops_list_style(self):
        page = render("<ul><li>无符号</li></ul><ol><li>第一</li><li>第二</li></ol>")
        self.assertIn(">· 无符号<", page)
        self.assertIn(">1. 第一<", page)
        self.assertIn(">2. 第二<", page)

    def test_a_hand_written_marker_is_not_duplicated(self):
        page = render("<ul><li>· 已有符号</li></ul>")
        self.assertEqual(page.count("· 已有符号"), 1)

    def test_table_gets_zebra_rows_and_no_border_on_the_last_row(self):
        page = render()
        cells = re.findall(r"<td ([^>]*)>", page)
        self.assertEqual(len(cells), 6)
        self.assertIn("background:#FAFCFF", cells[3], "第二行应隔行浅底")
        self.assertIn("border-bottom:none", cells[3], "最后一行不留底线")

    def test_wide_tables_drop_nowrap(self):
        header = "".join(f"<th>列{index}</th>" for index in range(5))
        row = "".join(f"<td>{index}</td>" for index in range(5))
        page = render(f"<table><thead><tr>{header}</tr></thead><tbody><tr>{row}</tr></tbody></table>")
        self.assertNotIn("white-space:nowrap", page)

    def test_svg_is_replaced_by_its_rasterised_copy(self):
        page = render('<figure><svg aria-label="图 2：矢量" viewBox="0 0 10 10"></svg></figure>', [STUB])
        self.assertIn(f'src="{STUB}"', page)
        self.assertIn('alt="图 2：矢量"', page)
        self.assertNotIn("<svg", page)

    def test_vectors_and_svg_sources_must_line_up(self):
        with self.assertRaises(ValueError):
            render('<figure><svg aria-label="图" viewBox="0 0 10 10"></svg></figure>', [])

    def test_ending_is_case_signature_and_call_to_action(self):
        page = render()
        self.assertIn("学习中心配套案例：案例", page)
        self.assertIn("灵算科技联系方式与品牌标识", page)
        self.assertIn("点击阅读原文", page)

    def test_missing_case_skips_the_card(self):
        page = wechat.render(SAMPLE, banners=lambda text: STUB, follow=STUB, signature=STUB, cta=STUB)
        self.assertNotIn("学习中心配套案例", page)


class AuditTests(unittest.TestCase):
    def test_clean_output_passes(self):
        self.assertEqual(wechat.audit(render()), [])

    def test_leftover_class_is_reported(self):
        problems = wechat.audit('<p class="eq">x</p>')
        self.assertTrue(any("class" in problem for problem in problems))

    def test_fixed_pixel_width_is_reported(self):
        problems = wechat.audit('<img alt="图" src="data:image/png;base64,AA" style="width:642px">')
        self.assertTrue(any("像素宽度" in problem for problem in problems))

    def test_forbidden_css_is_reported(self):
        problems = wechat.audit('<p style="position:absolute">x</p>')
        self.assertTrue(any("position" in problem for problem in problems))

    def test_external_image_is_reported(self):
        problems = wechat.audit('<img alt="图" src="https://example.com/a.png">')
        self.assertTrue(any("data URI" in problem for problem in problems))

    def test_missing_alt_is_reported(self):
        problems = wechat.audit('<img src="data:image/png;base64,AA">')
        self.assertTrue(any("alt" in problem for problem in problems))


class ContentTests(unittest.TestCase):
    def test_every_article_renders_and_audits_clean(self):
        from tools import build
        _, articles = build.read_articles()
        for article in articles:
            with self.subTest(article=article["key"]):
                page = wechat.render(
                    article["body"], banners=lambda text: STUB,
                    vectors=[STUB] * len(article["vectors"]),
                    case=(article["case"]["title"], STUB) if article["case"] else None,
                    follow=STUB, signature=STUB, cta=STUB,
                )
                self.assertEqual(wechat.audit(page), [])
                self.assertNotIn("<h2", page)


if __name__ == "__main__":
    unittest.main()
