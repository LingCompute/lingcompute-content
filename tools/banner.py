"""章节横幅与案例卡绘制。

公众号正文里的章节标题在发布版中是一张斜切缎带图：微信编辑器会过滤伪元素，
CSS 做不出这个形状，因此由构建现场生成 PNG。几何、配色与字号取自发布版
（1080 画布，微信按 642 CSS 像素显示）。
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache/fonts"

CANVAS = (1080, 159)
SUPERSAMPLE = 3
RIBBON_TOP = 35
RIBBON_HEIGHT = 78
SKEW = 41
SIDE_PADDING = 40
PADDING_GROWTH = 0.15
PADDING_REFERENCE = 464
MIN_RIBBON = 370
MAX_TEXT_WIDTH = 940
FONT_SIZE = 52
MIN_FONT_SIZE = 40
MAX_LINES = 2
LINE_GAP = 6
PALE_TILT = -1.2
PALE_PADDING = 2
ACCENT = (22, 22, 11)
ACCENT_GAP = 4
LIGHT = (12, 109, 219)
DARK = (7, 79, 181)
PALE_ALPHA = 74
CARD_BACKGROUND = (236, 235, 236)
CARD_INK = (26, 26, 26)
CARD_SUBINK = (51, 51, 51)


def ttf(weight="Semibold"):
    """把缓存中的 MiSans WOFF2 转成 PIL 可读的 TTF。"""
    source = CACHE / f"MiSans-{weight}.woff2"
    target = CACHE / f"MiSans-{weight}.ttf"
    if not source.is_file():
        raise ValueError("MiSans fonts missing; run python tools/fonts.py before building")
    if not target.is_file() or target.stat().st_mtime < source.stat().st_mtime:
        from fontTools.ttLib import TTFont

        font = TTFont(str(source))
        font.flavor = None
        font.save(str(target))
    return target


def gradient(width, height, light=LIGHT, dark=DARK):
    strip = Image.new("RGB", (width, 1))
    draw = ImageDraw.Draw(strip)
    for x in range(width):
        ratio = x / max(width - 1, 1)
        draw.point((x, 0), tuple(round(a + (b - a) * ratio) for a, b in zip(light, dark)))
    return strip.resize((width, height), Image.Resampling.NEAREST)


def parallelogram(left, top, width, height, skew):
    """左下角为 (left, top+height) 的平行四边形：顶边相对底边右移 skew。"""
    return [
        (left + skew, top),
        (left + skew + width, top),
        (left + width, top + height),
        (left, top + height),
    ]


def measure(text, font):
    box = font.getbbox(text)
    return box[2] - box[0], box[3] - box[1]


def fit(text, width, weight="Semibold"):
    """在给定宽度内选字号；超出下限时按字数折行。"""
    for size in range(FONT_SIZE, MIN_FONT_SIZE - 1, -2):
        font = ImageFont.truetype(str(ttf(weight)), size)
        if measure(text, font)[0] <= width:
            return size, [text]
    size = MIN_FONT_SIZE
    font = ImageFont.truetype(str(ttf(weight)), size)
    per_line = max(1, len(text) // MAX_LINES + 1)
    lines = [text[index:index + per_line] for index in range(0, len(text), per_line)]
    if len(lines) > MAX_LINES or any(measure(line, font)[0] > width for line in lines):
        raise ValueError(f"章节标题过长，请改写为 18 字以内：{text}")
    return size, lines


def banner(text, width=CANVAS[0], height=CANVAS[1]):
    scale = SUPERSAMPLE
    size, lines = fit(text, MAX_TEXT_WIDTH)
    font = ImageFont.truetype(str(ttf("Semibold")), size * scale)
    line_gap = LINE_GAP * scale
    boxes = [font.getbbox(line) for line in lines]
    text_width = max(box[2] - box[0] for box in boxes)
    line_height = max(box[3] - box[1] for box in boxes)
    text_height = line_height * len(lines) + line_gap * (len(lines) - 1)

    ribbon_height = RIBBON_HEIGHT * scale
    if len(lines) > 1:
        ribbon_height += text_height - line_height
    padding = SIDE_PADDING + max(0, text_width / scale - PADDING_REFERENCE) * PADDING_GROWTH
    ribbon_width = round(max(text_width + 2 * padding * scale, MIN_RIBBON * scale))
    canvas = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
    top = (RIBBON_TOP * scale) if len(lines) == 1 else ((height * scale - ribbon_height) // 2)
    left = (width * scale - ribbon_width) // 2 - SKEW * scale // 2

    shape = parallelogram(left, top, ribbon_width, ribbon_height, SKEW * scale)
    fill = gradient(ribbon_width, ribbon_height)

    pale_mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(pale_mask).polygon(
        parallelogram(
            left - PALE_PADDING * scale,
            top - PALE_PADDING * scale,
            ribbon_width + 2 * PALE_PADDING * scale,
            ribbon_height + 2 * PALE_PADDING * scale,
            SKEW * scale,
        ),
        fill=PALE_ALPHA,
    )
    pale_mask = pale_mask.rotate(
        PALE_TILT, resample=Image.Resampling.BICUBIC,
        center=(left + ribbon_width / 2, top + ribbon_height / 2),
    )
    pale_layer = fill.resize(canvas.size, Image.Resampling.NEAREST).convert("RGBA")
    pale_layer.putalpha(pale_mask)
    canvas = Image.alpha_composite(canvas, pale_layer)

    width_px, height_px, skew_px = (value * scale for value in ACCENT)
    middle = top + ribbon_height / 2
    left_edge = left + (middle - top) * SKEW * scale / ribbon_height
    right_edge = left + ribbon_width + (top + ribbon_height - middle) * SKEW * scale / ribbon_height
    for side in (-1, 1):
        start = (
            left_edge - ACCENT_GAP * scale - width_px - skew_px
            if side < 0
            else right_edge + 2 * ACCENT_GAP * scale
        )
        accent = parallelogram(start, middle - height_px / 2, width_px, height_px, skew_px)
        accent_mask = Image.new("L", canvas.size, 0)
        ImageDraw.Draw(accent_mask).polygon(accent, fill=255)
        accent_layer = fill.resize(canvas.size, Image.Resampling.NEAREST).convert("RGBA")
        accent_layer.putalpha(accent_mask)
        canvas = Image.alpha_composite(canvas, accent_layer)

    ribbon_mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(ribbon_mask).polygon(shape, fill=255)
    ribbon_layer = fill.resize(canvas.size, Image.Resampling.NEAREST).convert("RGBA")
    ribbon_layer.putalpha(ribbon_mask)
    canvas = Image.alpha_composite(canvas, ribbon_layer)

    draw = ImageDraw.Draw(canvas)
    y = (top + (ribbon_height - text_height) // 2) - boxes[0][1]
    for index, line in enumerate(lines):
        box = boxes[index]
        x = (width * scale - (box[2] - box[0])) // 2 - box[0] + SKEW * scale // 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255, 255))
        y += line_height + line_gap
    return canvas.resize((width, height), Image.Resampling.LANCZOS)


def case_card(title, qr, width=1080, height=334):
    scale = SUPERSAMPLE
    canvas = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
    card = Image.new("RGBA", canvas.size, CARD_BACKGROUND + (255,))
    mask = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, canvas.size[0] - 1, canvas.size[1] - 1), radius=16 * scale, fill=255
    )
    canvas.paste(card, (0, 0), mask)

    panel = 210 * scale
    padding = 10 * scale
    with Image.open(qr) as source:
        code = source.convert("RGBA")
        code = code.resize((panel - 2 * padding, panel - 2 * padding), Image.Resampling.NEAREST)
    white = Image.new("RGBA", (panel, panel), (255, 255, 255, 255))
    white_mask = Image.new("L", white.size, 0)
    ImageDraw.Draw(white_mask).rounded_rectangle((0, 0, panel - 1, panel - 1), radius=8 * scale, fill=255)
    white.paste(code, (padding, padding))
    canvas.paste(white, (77 * scale, (height * scale - panel) // 2), white_mask)

    label = ImageFont.truetype(str(ttf("Semibold")), 46 * scale)
    body = ImageFont.truetype(str(ttf("Regular")), 44 * scale)
    draw = ImageDraw.Draw(canvas)
    left = 353 * scale
    draw.text((left, 118 * scale), "学习中心配套案例", font=label, fill=CARD_INK + (255,))
    draw.text((left, 196 * scale), title, font=body, fill=CARD_SUBINK + (255,))
    return canvas.resize((width, height), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("output")
    parser.add_argument("--kind", choices=["banner", "case"], default="banner")
    parser.add_argument("--qr")
    options = parser.parse_args()
    image = banner(options.text) if options.kind == "banner" else case_card(options.text, options.qr)
    image.save(options.output)


if __name__ == "__main__":
    main()
