import argparse
import base64
import hashlib
import html
import json
import math
import os
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import bleach
import markdown
from PIL import Image

try:
    from .fonts import font_style
except ImportError:
    from fonts import font_style

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
REPOSITORY = "https://github.com/LingCompute/lingcompute-content"
SOURCE_REF = quote(os.environ.get("GITHUB_SHA", "main"), safe="")
TAGS = {
    "p", "br", "h1", "h2", "h3", "h4", "strong", "em", "a", "img",
    "ul", "ol", "li", "blockquote", "pre", "code", "table", "thead",
    "tbody", "tr", "th", "td", "sub", "sup", "hr",
}


def local_path(base, reference, root=ROOT):
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc:
        raise ValueError(f"Expected a local file: {reference}")
    relative = Path(unquote(parsed.path))
    if relative.is_absolute() or not parsed.path:
        raise ValueError(f"Invalid local file: {reference}")
    candidate = (base / relative).resolve()
    if not candidate.is_relative_to(root.resolve()) or not candidate.is_file():
        raise ValueError(f"Missing file or path outside repository: {reference}")
    return candidate


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def data_uri(path):
    media = {".png": "png", ".gif": "gif", ".jpg": "jpeg", ".jpeg": "jpeg", ".webp": "webp"}
    suffix = path.suffix.lower()
    if suffix not in media:
        raise ValueError(f"Unsupported article image: {path.name}")
    with Image.open(path) as image:
        image.verify()
    return f"data:image/{media[suffix]};base64,{base64.b64encode(path.read_bytes()).decode()}"


def attributes(tag, name, value):
    return (
        tag == "p" and name == "class" and value == "eq"
        or tag == "a" and name in {"href", "title"}
        or tag == "img" and name in {"src", "alt", "title"}
        or tag in {"th", "td"} and name in {"colspan", "rowspan"}
    )


class ContentHTML(HTMLParser):
    def __init__(self, base, root=ROOT):
        super().__init__(convert_charrefs=False)
        self.base = base
        self.root = root.resolve()
        self.parts = []
        self.assets = []
        self.text = []
        self.equations = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "img":
            alt = values.get("alt", "").strip()
            if not alt:
                raise ValueError("Every image needs a descriptive caption")
            path = local_path(self.base, values.get("src", ""), self.root)
            if not path.is_relative_to(self.base.resolve()):
                raise ValueError("Article images must be inside their series directory")
            self.assets.append(path)
            self.text.append(alt)
            self.parts.append(f'<img alt="{html.escape(alt, quote=True)}" src="{data_uri(path)}">')
            return
        if tag == "a" and values.get("href"):
            target = values["href"]
            parsed = urlsplit(target)
            if parsed.scheme:
                if parsed.scheme not in {"https", "http", "mailto"}:
                    raise ValueError(f"Unsupported link: {target}")
            elif parsed.netloc:
                raise ValueError(f"Protocol-relative link is not supported: {target}")
            elif parsed.path:
                destination = local_path(self.base, target, self.root)
                values["href"] = (
                    f"{REPOSITORY}/blob/{SOURCE_REF}/{quote(destination.relative_to(self.root).as_posix())}"
                    + (f"#{quote(parsed.fragment)}" if parsed.fragment else "")
                )
                attributes_html = " ".join(
                    f'{name}="{html.escape(value, quote=True)}"' for name, value in values.items()
                )
                self.parts.append(f"<a {attributes_html}>")
                return
        if tag == "p" and values.get("class") == "eq":
            self.equations += 1
        self.parts.append(self.get_starttag_text())

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        self.parts.append(data)
        self.text.append(data)

    def handle_entityref(self, name):
        self.parts.append(f"&{name};")
        self.text.append(html.unescape(f"&{name};"))

    def handle_charref(self, name):
        self.parts.append(f"&#{name};")
        self.text.append(html.unescape(f"&#{name};"))


def render_body(manuscript, base, root=ROOT):
    rendered = markdown.markdown(manuscript, extensions=["extra", "sane_lists"])
    cleaned = bleach.clean(
        rendered, tags=TAGS, attributes=attributes, protocols={"https", "http", "mailto"}, strip=True
    )
    parser = ContentHTML(base, root)
    parser.feed(cleaned)
    body = "".join(parser.parts)

    def figure(match):
        alt, source = match.groups()
        label, separator, caption = alt.partition("：")
        caption = caption if separator else alt
        badge = f'<span class="fig-tag">{label}</span>' if separator else ""
        return f'<figure><img alt="{alt}" src="{source}"><figcaption>{badge}{caption}</figcaption></figure>'

    body = re.sub(r'<p><img alt="([^"]*)" src="([^"]+)"></p>', figure, body)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="table-wrap">\1</div>', body, flags=re.S)
    body = re.sub(
        r"(?<=>)([^<>]+)(?=<)",
        lambda match: match.group(1).replace("κ", '<span class="greek">κ</span>'),
        body,
    )
    return body, parser


def reading_minutes(text, figures, equations):
    han = len(re.findall(r"[\u3400-\u9fff]", text))
    words = len(re.findall(r"[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*", text))
    lower = max(1, math.ceil(han / 450 + words / 200 + figures / 6 + equations / 12))
    upper = max(lower + 1, math.ceil(han / 250 + words / 120 + figures * 25 / 60 + equations / 5))
    return lower, upper


def read_articles(root=ROOT):
    root = root.resolve()
    products = json.loads((root / "config/products.json").read_text())
    articles = []
    listed = set()
    for manifest in sorted((root / "content").glob("*/*/series.json")):
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest.parent.name):
            raise ValueError(f"Invalid series directory: {manifest.parent.name}")
        series = json.loads(manifest.read_text())
        product = series["product"]
        if product not in products or manifest.parent.parent.name != product:
            raise ValueError(f"Unknown or inconsistent product: {product}")
        if not series["title"].strip() or not series["audience"].strip():
            raise ValueError(f"Series title and audience are required: {manifest}")
        if not (manifest.parent / "SOURCES.md").is_file():
            raise ValueError(f"Missing minimum evidence record: {manifest.parent}")
        for entry in series["articles"]:
            slug = entry["slug"]
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
                raise ValueError(f"Invalid article slug: {slug}")
            path = local_path(manifest.parent, f"{slug}.md", root)
            if path in listed:
                raise ValueError(f"Duplicate article: {path}")
            listed.add(path)
            manuscript = path.read_text()
            if not manuscript.startswith("# ") or not entry["summary"].strip():
                raise ValueError(f"Article needs a heading and summary: {path}")
            if not entry["sources"] or any(
                urlsplit(url).scheme != "https" or not urlsplit(url).netloc for url in entry["sources"]
            ):
                raise ValueError(f"Article needs HTTPS sources: {path}")
            if not isinstance(entry.get("authors"), list) or any(
                not isinstance(author, str) or not re.fullmatch(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*", author)
                for author in entry["authors"]
            ):
                raise ValueError(f"Article authors must be a list of GitHub logins: {path}")
            body, parser = render_body(manuscript, path.parent, root)
            minutes = reading_minutes(" ".join(parser.text), len(parser.assets), parser.equations)
            articles.append({
                "path": path,
                "key": path.relative_to(root).as_posix(),
                "title": manuscript.splitlines()[0][2:].strip(),
                "summary": entry["summary"],
                "series": series["title"],
                "audience": series["audience"],
                "product": product,
                "body": body,
                "assets": parser.assets,
                "equations": parser.equations,
                "minutes": minutes,
            })
    actual = {
        path.resolve() for path in (root / "content").glob("*/*/*.md")
        if path.name not in {"SOURCES.md", "README.md"}
    }
    if not articles or actual != listed:
        raise ValueError("Every article must appear exactly once in a series.json manifest")
    return products, articles


def legacy_review(article, ledger, root=ROOT):
    record = ledger.get(article["key"])
    if record is None or digest(article["path"]) != record["manuscript_sha256"]:
        return False
    current = {path.relative_to(root.resolve()).as_posix(): digest(path) for path in article["assets"]}
    return current == record["assets"]


def document(title, content, style):
    return (
        '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; '
        'img-src data:; font-src data:; style-src \'unsafe-inline\'">'
        f"<title>{html.escape(title)}</title><style>{style}</style></head>"
        f"<body>{content}</body></html>"
    )


def article_html(article, products, style, logo, reviewed, screens=None, navigation=""):
    lower, upper = article["minutes"]
    screen_text = f"{screens:.1f} 参考屏" if screens is not None else "测量中"
    warning = (
        '<p class="warning">长文提示：正文超过10参考屏，可先扫描小标题，再按问题细读。</p>'
        if screens is not None and screens > 10 else ""
    )
    review_text = (
        "与历史人审清单中的内容指纹匹配；原审核者署名和日期未提供。"
        if reviewed else "新稿审核以对应GitHub PR记录为准；预览本身不代表审核通过。"
    )
    content = (
        '<article><header class="meta"><p>构建预览 · 正式收录以主分支及PR审核记录为准</p>'
        f"<p>{html.escape(products[article['product']]['name'])} · {html.escape(article['series'])}</p>"
        f"<p>适合：{html.escape(article['audience'])}</p>"
        f"<p>本文解决：{html.escape(article['summary'])}</p>"
        f"<p>预计阅读 {lower}–{upper} 分钟，实操另计 · {screen_text}</p>{warning}"
        '<p>阅读时长为编辑模型估计；参考视口390×844 CSS像素，不同设备会有差异。</p>'
        f'</header><main id="article-body">{article["body"]}</main>'
        f'<footer class="brand"><img src="{logo}" alt="灵算科技 LingCompute">'
        '<p>自有文章及插图：CC BY-NC 4.0；商用请另行联系。商标与另有标注的第三方材料除外。</p>'
        '<p>字体：<a href="https://hyperos.mi.com/font/en/download/">MiSans（小米）</a>，按其字体许可使用。</p>'
        f"<p>{review_text}</p>"
        f'<p><a href="{REPOSITORY}/blob/{SOURCE_REF}/{quote(article["path"].parent.relative_to(ROOT).as_posix())}/SOURCES.md">'
        "来源、指标口径与素材说明</a></p>"
        f'</footer><nav aria-label="文章导航">{navigation}</nav></article>'
    )
    return document(article["title"], content, style)


def export_wechat(page):
    return page.locator("article").evaluate("""article => {
        const clone = article.cloneNode(true);
        const originals = [article, ...article.querySelectorAll("*")];
        const copies = [clone, ...clone.querySelectorAll("*")];
        const properties = [
          "color", "background-color", "font-family", "font-size", "font-weight",
          "font-style", "line-height", "text-align", "text-decoration",
          "margin-top", "margin-bottom", "padding-top", "padding-bottom",
          "padding-left", "padding-right", "border-left", "border-top",
          "border-bottom", "border-radius", "display", "vertical-align",
          "overflow-wrap", "white-space", "border-collapse", "table-layout"
        ];
        originals.forEach((node, index) => {
            const style = getComputedStyle(node);
            copies[index].style.cssText = properties.map(
              property => property + ":" + style.getPropertyValue(property)
            ).join(";");
            if (node.tagName === "IMG" || node.tagName === "TABLE") {
                copies[index].style.width = node.closest(".brand") ? "180px" : "100%";
                copies[index].style.maxWidth = "100%";
                copies[index].style.height = "auto";
            }
        });
        clone.style.padding = "0";
        clone.querySelectorAll("nav").forEach(node => node.remove());
        return clone.outerHTML;
    }""")


def build():
    from playwright.sync_api import sync_playwright

    products, articles = read_articles()
    ledger = json.loads((ROOT / "reviews/legacy.json").read_text())
    style = font_style() + "\n" + (ROOT / "tools/style.css").read_text()
    brand = ROOT / "assets/brand/lingcompute-horizontal.svg"
    BUILD.mkdir(exist_ok=True)
    report = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chromium")
        page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
        logo_directory = BUILD / "assets"
        logo_directory.mkdir(exist_ok=True)
        logo_path = logo_directory / "lingcompute-horizontal.png"
        svg_uri = "data:image/svg+xml;base64," + base64.b64encode(brand.read_bytes()).decode()
        page.set_content(f'<img src="{svg_uri}" style="width:720px;height:auto">', wait_until="load")
        page.locator("img").screenshot(path=str(logo_path), omit_background=True)
        logo = data_uri(logo_path)
        for article in articles:
            destination = BUILD / article["path"].relative_to(ROOT / "content").with_suffix(".html")
            destination.parent.mkdir(parents=True, exist_ok=True)
            reviewed = legacy_review(article, ledger)
            navigation = f'<a href="{REPOSITORY}/blob/main/README.md">产品与系列目录</a>'
            page.set_content(article_html(article, products, style, logo, reviewed), wait_until="load")
            page.evaluate("async () => { await document.fonts.ready; await Promise.all(Array.from(document.images, image => image.decode())); }")
            height = page.locator("#article-body").evaluate("element => element.getBoundingClientRect().height")
            screens = height / 844
            output = article_html(article, products, style, logo, reviewed, screens, navigation)
            destination.write_text(output)
            page.set_content(output, wait_until="load")
            page.evaluate("async () => { await document.fonts.ready; await Promise.all(Array.from(document.images, image => image.decode())); }")
            if page.evaluate("document.documentElement.scrollWidth > innerWidth + 1"):
                raise ValueError(f"Horizontal overflow at reference viewport: {article['key']}")
            page.screenshot(path=str(destination.with_suffix(".png")), full_page=True, animations="disabled")
            wechat = export_wechat(page)
            destination.with_suffix(".wechat.html").write_text(document(article["title"], wechat, ""))
            assets = [
                {
                    "order": index + 1,
                    "path": path.relative_to(ROOT).as_posix(),
                    "sha256": digest(path),
                    "bytes": path.stat().st_size,
                }
                for index, path in enumerate(article["assets"])
            ]
            record = {
                "article": article["key"],
                "manuscript_sha256": digest(article["path"]),
                "reading_minutes": list(article["minutes"]),
                "reading_estimate": "editorial heuristic; practice excluded",
                "reference_viewport_css_px": [390, 844],
                "body_height_css_px": round(height, 1),
                "reference_screens": round(screens, 2),
                "over_ten_screens": screens > 10,
                "historical_review_matches": reviewed,
                "assets": assets,
                "brand_asset": {
                    "source": brand.relative_to(ROOT).as_posix(),
                    "source_sha256": digest(brand),
                    "upload": logo_path.relative_to(BUILD).as_posix(),
                    "sha256": digest(logo_path),
                    "bytes": logo_path.stat().st_size,
                },
            }
            destination.with_suffix(".manifest.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
            report.append(record)
            print(f"{article['title']}: {screens:.1f}屏，约{article['minutes'][0]}–{article['minutes'][1]}分钟"
                  + ("；超长已提示" if screens > 10 else ""))
        browser.close()
    cards = []
    for article in articles:
        relative = quote(article["path"].relative_to(ROOT / "content").with_suffix(".html").as_posix())
        cards.append(
            f'<section class="card"><h2><a href="{relative}">{html.escape(article["title"])}</a></h2>'
            f'<p>{html.escape(article["series"])} · {html.escape(article["summary"])}</p></section>'
        )
    (BUILD / "index.html").write_text(document(
        "灵算技术内容库",
        "<article><h1>灵算技术内容库</h1>" + "".join(cards)
        + '<footer class="brand">字体：<a href="https://hyperos.mi.com/font/en/download/">MiSans（小米）</a>，按其字体许可使用。</footer></article>',
        style,
    ))
    (BUILD / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    arguments = argparse.ArgumentParser()
    arguments.add_argument("--check", action="store_true", help="Validate sources without launching Chromium")
    options = arguments.parse_args()
    if options.check:
        _, checked = read_articles()
        print(f"Validated {len(checked)} articles")
    else:
        build()
