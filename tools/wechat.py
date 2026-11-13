"""公众号稿排版器：把正文 HTML 变成可直接粘进微信编辑器的内联样式 HTML。

微信编辑器只保留内联样式与图片，会过滤 class、伪元素与外链样式表，所以发布稿
的每个元素都带 style。取值来自 `config/wechat-theme.json`（两篇发布版逐项实测），
本模块只负责结构、内联与校验：

- 不依赖浏览器：样式是查表得到的，不靠 computed style 反推，构建与 CI 都不需要
  Chromium 就能产出并检查发布稿；
- 不猜设计值：颜色、字号、间距只在主题文件里出现一次；
- 能自查：`audit()` 拦截微信会吃掉或会在手机宽度溢出的写法。

用法（构建侧）：`render(body, banners=..., vectors=..., case=..., follow=...)`。
"""

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEME_PATH = ROOT / "config/wechat-theme.json"

VOID = {"img", "br", "hr", "meta", "link", "input"}
KEEP = {
    "section", "p", "span", "strong", "em", "a", "img", "figure", "figcaption",
    "h3", "h4", "table", "thead", "tbody", "tr", "th", "td", "ul", "ol", "li",
    "blockquote", "pre", "code", "br", "sub", "sup", "hr",
}
FORBIDDEN = (
    "position", "z-index", "transform", "filter", "clip-path", "animation",
    "transition", "float", "display:grid", "display:flex", "content:",
    "background-image", "::before", "::after",
)


def theme(path=THEME_PATH):
    return json.loads(Path(path).read_text())


def _resolve(value, tokens):
    return re.sub(r"\{([a-z-]+)\}", lambda match: tokens[match.group(1)], value)


def styles(theme_=None):
    """把主题里的元素样式解析成可直接写进 style 的字符串。"""
    theme_ = theme_ or theme()
    tokens = theme_["tokens"]
    return {
        name: ";".join(f"{key}:{_resolve(value, tokens)}" for key, value in declarations.items())
        for name, declarations in theme_["elements"].items()
    }


class Node:
    __slots__ = ("tag", "attrs", "children", "styles")

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.children = []
        self.styles = ()

    @property
    def classes(self):
        return set((self.attrs.get("class") or "").split())

    @property
    def text(self):
        return "".join(child if isinstance(child, str) else child.text for child in self.children)


class _Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = Node("#root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)

    def handle_entityref(self, name):
        self.stack[-1].children.append(f"&{name};")

    def handle_charref(self, name):
        self.stack[-1].children.append(f"&#{name};")


def parse(source):
    parser = _Parser()
    parser.feed(source)
    parser.close()
    return parser.root


def _nodes(node):
    for child in node.children:
        if isinstance(child, Node):
            yield child


def _walk(node):
    for child in _nodes(node):
        yield child
        yield from _walk(child)


def _columns(table):
    rows = [node for node in _walk(table) if node.tag == "tr"]
    return max(
        (sum(1 for cell in _nodes(row) if cell.tag in {"th", "td"}) for row in rows), default=0
    )


def _rows(tbody):
    return [node for node in _nodes(tbody) if node.tag == "tr"]


def _transform(node, theme_, vectors, banners, context):
    """就地改写：算好每个节点的样式名，把 h2 换成横幅图、把内联 SVG 换成 PNG。"""
    parent_tag = context.get("parent_tag")
    in_figure = parent_tag == "figure"
    rows = _rows(node) if node.tag in {"tbody", "thead"} else []
    row_index = -1
    item_index = -1
    replacement = []
    for child in node.children:
        if isinstance(child, str):
            replacement.append(child)
            continue
        if child.tag == "h1":
            # 微信标题栏已经有大标题，正文里不再重复
            continue
        if child.tag == "svg":
            uri = next(vectors, None)
            if uri is None:
                raise ValueError("Inline SVG needs a rasterised PNG for the WeChat export")
            image = Node("img", {"alt": child.attrs.get("aria-label", ""), "src": uri})
            image.styles = ("img" if in_figure else "plate",)
            replacement.append(image)
            continue
        if child.tag == "h2":
            text = html.unescape(re.sub(r"<[^>]+>", "", child.text)).strip()
            section = Node("section")
            section.styles = ("banner",)
            image = Node("img", {"alt": f"章节：{text}", "src": banners(text)})
            image.styles = ("plate",)
            section.children = [image]
            replacement.append(section)
            continue
        if child.tag == "div" and child.classes == {"table-wrap"}:
            _transform(child, theme_, vectors, banners, context)
            replacement.extend(child.children)
            continue
        if child.tag not in KEEP:
            _transform(child, theme_, vectors, banners, context)
            replacement.extend(child.children)
            continue

        child.styles = _element_styles(child, context, theme_)
        child.attrs.pop("class", None)
        child.attrs.pop("style", None)
        child_context = {**context, "parent_tag": child.tag, "in_figure": in_figure}
        if child.tag == "table":
            child_context["columns"] = _columns(child)
        elif child.tag == "tr":
            row_index += 1
            child_context["row"] = row_index
            child_context["rows"] = len(rows)
        elif child.tag == "li":
            item_index += 1
            _marker(child, node.tag, item_index)
        _transform(child, theme_, vectors, banners, child_context)
        replacement.append(child)
    node.children = replacement


MARKERS = ("·", "・", "•", "-", "–", "—")


def _marker(item, list_tag, index):
    """给列表项补项目符号：微信会把 list-style 置为 none，符号只能写进文字。"""
    text = item.text.lstrip()
    if not text or text[0] in MARKERS or re.match(r"\d+\s*[.、)）]", text):
        return
    item.children.insert(0, f"{'·' if list_tag == 'ul' else f'{index + 1}.'} ")


def _element_styles(node, context, theme_):
    if node.tag == "section":
        return ()
    if node.tag == "img":
        return ("img" if context.get("parent_tag") == "figure" else "plate",)
    if node.tag == "p":
        classes = node.classes
        return ("eq",) if "eq" in classes else (("note",) if "note" in classes else ("p",))
    if node.tag == "span":
        classes = node.classes
        if "fig-tag" in classes:
            return ("fig-tag",)
        return ("greek",) if "greek" in classes else ()
    if node.tag == "th":
        nowrap = context.get("columns", 0) <= theme_["limits"]["max_nowrap_columns"]
        return ("th", "th-nowrap") if nowrap else ("th",)
    if node.tag == "td":
        row = context.get("row", 0)
        names = ["td"]
        if row % 2 == 1:
            names.append("td-zebra")
        if row == context.get("rows", 0) - 1:
            names.append("td-last")
        return tuple(names)
    return (node.tag,) if node.tag in {
        "h3", "strong", "em", "a", "ul", "ol", "li", "figure", "figcaption",
        "table", "blockquote", "pre", "code", "sub", "sup", "br", "hr",
    } else ()


def _serialise(node, out, style_map):
    if isinstance(node, str):
        out.append(node)
        return
    if node.tag == "#root":
        for child in node.children:
            _serialise(child, out, style_map)
        return
    style = ";".join(filter(None, (style_map.get(name) for name in node.styles)))
    attributes = []
    if style:
        attributes.append(("style", style))
    attributes.extend(node.attrs.items())
    rendered = "".join(
        f' {name}="{html.escape(str(value), quote=True)}"' for name, value in attributes if value is not None
    )
    out.append(f"<{node.tag}{rendered}>")
    if node.tag in VOID:
        return
    for child in node.children:
        _serialise(child, out, style_map)
    out.append(f"</{node.tag}>")


def _plate(tag_class, alt, uri):
    section = Node("section")
    section.styles = ("case",) if tag_class == "case-card" else ("plate-section",)
    image = Node("img", {"alt": alt, "src": uri})
    image.styles = ("plate",)
    section.children = [image]
    return section


def _ending_nodes(case, signature, cta):
    """页尾三段：案例卡 → 签名卡 → 阅读原文条。case 为 None 时跳过（横向比较篇没有单一案例）。"""
    nodes = []
    if case:
        title, uri = case
        nodes.append(_plate("case-card", f"学习中心配套案例：{title}", uri))
    nodes.append(_plate("signature", "灵算科技联系方式与品牌标识", signature))
    nodes.append(_plate("cta", "点击阅读原文，进入官网免费试用", cta))
    return nodes


def render(body, *, banners, vectors=(), case=None, follow=None, signature=None, cta=None, theme_=None):
    """把正文 HTML 变成公众号稿正文。

    body      : 已清洗的正文 HTML（可含 <h2>、<figure>、内联 <svg>）
    banners   : 章节标题 -> 横幅图 data URI 的函数
    vectors   : 按正文顺序排列的 SVG 栅格化 PNG data URI
    case      : (案例名, 卡片图 data URI)；无案例传 None
    follow/signature/cta: 载体图 data URI
    """
    theme_ = theme_ or theme()
    style_map = styles(theme_)
    tree = parse(body)
    _transform(tree, theme_, iter(vectors), banners, {"parent_tag": None})
    root = Node("section")
    root.styles = ("root",)
    root.children = list(tree.children)
    if follow:
        root.children.insert(0, _plate("follow", "点击上方蓝字关注我们", follow))
    if signature and cta:
        root.children.extend(_ending_nodes(case, signature, cta))
    out = []
    _serialise(root, out, style_map)
    return "".join(out)


def document(title, content):
    """公众号稿的独立 HTML 文件：只为在本地预览，粘贴时取 <section> 里的内容。"""
    return (
        '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; '
        'img-src data:; font-src data:; style-src \'unsafe-inline\'">'
        f"<title>{html.escape(title)}</title></head>"
        f'<body style="margin:0;padding:22px 16px;background:#fff">{content}</body></html>'
    )


def audit(source, theme_=None):
    """检查微信会吃掉、或会在手机宽度溢出的写法；返回问题列表。"""
    theme_ = theme_ or theme()
    problems = []
    for node in _walk(parse(source)):
        if node.tag == "h2":
            problems.append("h2 必须换成章节横幅图，微信里不保留可选中标题")
        if node.attrs.get("class"):
            problems.append(f"<{node.tag}> 仍带 class，微信不认 class 样式")
        if node.tag == "img" and not node.attrs.get("alt"):
            problems.append("图片缺少 alt 图注")
        if node.tag == "img" and node.attrs.get("src", "").startswith(("http://", "https://")):
            problems.append("图片必须是 data URI，外链会被微信拦截")
        style = node.attrs.get("style", "")
        for forbidden in FORBIDDEN:
            if forbidden in style:
                problems.append(f"<{node.tag}> 用了微信不支持的声明：{forbidden}")
        if node.tag in {"img", "table"} and re.search(r"(?:^|;)width:\d+px", style):
            problems.append(f"<{node.tag}> 写死了像素宽度，手机宽度会溢出")
    return problems


def main():
    parser = argparse.ArgumentParser(description="公众号稿样式与自检")
    parser.add_argument("--spec", action="store_true", help="打印当前主题的内联样式表")
    parser.add_argument("--check", metavar="FILE", nargs="*", help="检查已有的公众号稿 HTML")
    options = parser.parse_args()
    if options.spec:
        for name, style in styles().items():
            print(f"{name}: {style}")
        return
    if options.check:
        failures = 0
        for path in options.check:
            for problem in audit(Path(path).read_text()):
                print(f"{path}: {problem}")
                failures += 1
        if failures:
            sys.exit(1)
        print(f"Checked {len(options.check)} WeChat pages")
        return
    parser.print_help()


if __name__ == "__main__":
    main()
