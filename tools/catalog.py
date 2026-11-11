import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- BEGIN GENERATED CATALOG -->"
END = "<!-- END GENERATED CATALOG -->"


def text(value):
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", " ".join(value.splitlines()))


def render(products, articles, report, root=ROOT):
    records = {record["article"]: record for record in report}
    if len(records) != len(report) or set(records) != {article["key"] for article in articles}:
        raise ValueError("Build report must match the current article list")
    groups = {}
    for article in articles:
        record = records[article["key"]]
        fingerprint = hashlib.sha256(article["path"].read_bytes()).hexdigest()
        assets = [
            (path.relative_to(root).as_posix(), hashlib.sha256(path.read_bytes()).hexdigest())
            for path in article["assets"]
        ]
        if record["manuscript_sha256"] != fingerprint or assets != [
            (asset["path"], asset["sha256"]) for asset in record["assets"]
        ]:
            raise ValueError(f"Build report is stale: {article['key']}")
        groups.setdefault(article["product"], {}).setdefault(article["path"].parent.name, []).append(article)
    lines = ["| 产品 | 系列 | 产品入口 |", "| --- | --- | --- |"]
    for product, details in products.items():
        series = groups.get(product, {})
        links = "、".join(
            f"[{text(entries[0]['series'])}](#series-{product}-{slug})"
            for slug, entries in series.items()
        ) or "待首篇审核后收录"
        lines.append(f"| {text(details['name'])} | {links} | [产品介绍]({details['url']}) |")
    for product, series in groups.items():
        for slug, entries in series.items():
            lines.extend([
                "", f'<a id="series-{product}-{slug}"></a>', "",
                f"### {text(entries[0]['series'])}", "",
                f"适合：{text(entries[0]['audience'])}。", "",
            ])
            for index, article in enumerate(entries, 1):
                lower, upper = article["minutes"]
                warning = (
                    " **长文提示：超过10参考屏，建议先扫描小标题，再按问题细读。**"
                    if records[article["key"]]["over_ten_screens"] else ""
                )
                evidence = (Path(article["key"]).parent / "SOURCES.md").as_posix()
                lines.extend([
                    f"{index}. [{text(article['title'])}]({quote(article['key'])}) — {text(article['summary'])}",
                    "",
                    f"   预计阅读 **{lower}–{upper} 分钟**，实操另计。{warning}"
                    f" [来源、定量口径与素材说明]({quote(evidence)})。",
                    "",
                ])
    lines.extend(["阅读时长为编辑模型估计；参考视口为390×844 CSS像素，不同设备会有差异。", ""])
    return "\n".join(lines)


def update(readme, catalog, check=False):
    original = readme.read_text()
    if original.count(BEGIN) != 1 or original.count(END) != 1:
        raise ValueError("README needs exactly one generated catalog block")
    before, remainder = original.split(BEGIN)
    _, after = remainder.split(END)
    expected = before + BEGIN + "\n\n" + catalog.rstrip() + "\n\n" + END + after
    if check and expected != original:
        raise ValueError("README catalog is stale; build, then run python tools/catalog.py")
    if not check:
        readme.write_text(expected)


if __name__ == "__main__":
    try:
        from .build import read_articles
    except ImportError:
        from build import read_articles

    arguments = argparse.ArgumentParser()
    arguments.add_argument("--check", action="store_true")
    options = arguments.parse_args()
    products, articles = read_articles()
    report = json.loads((ROOT / "build/report.json").read_text())
    update(ROOT / "README.md", render(products, articles, report), options.check)
    print("README product, series and reading information verified" if options.check else "Updated README catalog")
