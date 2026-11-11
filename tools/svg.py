import hashlib
import math
import re
import xml.etree.ElementTree as ET

NAMESPACE = "http://www.w3.org/2000/svg"
TAGS = {
    "svg", "g", "defs", "symbol", "use", "title", "desc", "path", "rect",
    "circle", "ellipse", "line", "polyline", "polygon", "text", "tspan",
    "linearGradient", "radialGradient", "stop", "clipPath", "mask", "marker", "pattern",
}
PRESENTATION = {
    "fill", "fill-opacity", "fill-rule", "stroke", "stroke-width", "stroke-opacity",
    "stroke-linecap", "stroke-linejoin", "stroke-miterlimit", "stroke-dasharray",
    "stroke-dashoffset", "opacity", "color", "font-family", "font-size", "font-weight",
    "font-style", "text-anchor", "dominant-baseline", "alignment-baseline",
    "letter-spacing", "word-spacing", "text-decoration", "clip-path", "clip-rule",
    "mask", "marker-start", "marker-mid", "marker-end", "stop-color", "stop-opacity",
    "vector-effect", "paint-order",
}
ATTRIBUTES = PRESENTATION | {
    "id", "x", "y", "x1", "y1", "x2", "y2", "dx", "dy", "cx", "cy", "r", "rx", "ry",
    "width", "height", "viewBox", "preserveAspectRatio", "d", "points", "transform",
    "href", "offset", "gradientUnits", "gradientTransform", "spreadMethod", "fx", "fy",
    "fr", "clipPathUnits", "maskUnits", "maskContentUnits", "markerUnits",
    "markerWidth", "markerHeight", "refX", "refY", "orient", "patternUnits",
    "patternContentUnits", "patternTransform", "textLength", "lengthAdjust", "rotate",
}
IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*")


def image(path, alt, occurrence):
    raw = path.read_bytes()
    if len(raw) > 2 * 1024 * 1024:
        raise ValueError(f"SVG exceeds the 2 MiB limit: {path.name}")
    try:
        source = raw.decode("utf-8-sig")
        if re.search(r"<!\s*(DOCTYPE|ENTITY)", source, re.I):
            raise ValueError(f"SVG must not contain DTD or entity declarations: {path.name}")
        root = ET.fromstring(source)
    except (UnicodeError, ET.ParseError) as error:
        raise ValueError(f"Invalid UTF-8 SVG: {path.name}") from error
    nodes = []
    pending = [(root, 0)]
    while pending:
        node, depth = pending.pop()
        if depth > 64 or len(nodes) >= 10000:
            raise ValueError(f"SVG exceeds the 64 nesting or 10000 element limit: {path.name}")
        nodes.append(node)
        pending.extend((child, depth + 1) for child in reversed(node))
    if root.tag not in {"svg", f"{{{NAMESPACE}}}svg"}:
        raise ValueError(f"Expected an SVG root: {path.name}")
    try:
        bounds = [float(value) for value in re.split(r"[\s,]+", root.attrib["viewBox"].strip())]
        if len(bounds) != 4 or not all(math.isfinite(value) for value in bounds) or min(bounds[2:]) <= 0:
            raise ValueError
        if max(bounds[2:]) / min(bounds[2:]) > 32:
            raise ValueError
    except (KeyError, ValueError):
        raise ValueError(f"SVG needs a finite positive viewBox with aspect ratio at most 32: {path.name}") from None
    prefix = f"figure-{hashlib.sha256(raw).hexdigest()[:12]}-{occurrence}-"
    identifiers = {}
    for node in nodes:
        if "id" in node.attrib:
            identifier = node.attrib["id"]
            if not IDENTIFIER.fullmatch(identifier) or identifier in identifiers:
                raise ValueError(f"Invalid or duplicate SVG id: {path.name}")
            identifiers[identifier] = prefix + identifier

    def reference(identifier):
        if identifier not in identifiers:
            raise ValueError(f"Missing SVG fragment #{identifier}: {path.name}")
        return identifiers[identifier]

    for node in nodes:
        tag = node.tag.removeprefix(f"{{{NAMESPACE}}}")
        if tag not in TAGS:
            raise ValueError(f"Unsupported SVG element {tag}: {path.name}")
        node.tag = tag
        values = {}
        for original, value in node.attrib.items():
            name = "href" if original == "{http://www.w3.org/1999/xlink}href" else original
            if name == "{http://www.w3.org/XML/1998/namespace}space" and value in {"default", "preserve"}:
                values["xml:space"] = value
                continue
            if name == "style":
                for declaration in value.split(";"):
                    if not declaration.strip():
                        continue
                    property_name, separator, property_value = declaration.partition(":")
                    property_name = property_name.strip()
                    if not separator or property_name not in PRESENTATION:
                        raise ValueError(f"Use SVG presentation attributes for styles: {path.name}")
                    values[property_name] = property_value.strip()
                continue
            if name not in ATTRIBUTES:
                raise ValueError(f"Unsupported SVG attribute {name}: {path.name}")
            values[name] = value
        for name, value in list(values.items()):
            if any(token in value for token in ("\\", "@", "/*", "*/")):
                raise ValueError(f"Unsupported SVG attribute value: {path.name}")
            if name == "id":
                values[name] = identifiers[value]
            elif name == "href":
                if not value.startswith("#") or not IDENTIFIER.fullmatch(value[1:]):
                    raise ValueError(f"SVG references must be local fragments: {path.name}")
                values[name] = "#" + reference(value[1:])
            else:
                values[name] = re.sub(
                    r"url\(\s*['\"]?#([A-Za-z_][A-Za-z0-9_.-]*)['\"]?\s*\)",
                    lambda match: f"url(#{reference(match[1])})", value, flags=re.I,
                )
                without_fragments = re.sub(r"url\(#[A-Za-z_][A-Za-z0-9_.-]*\)", "", values[name])
                if re.search(r"url\s*\(", without_fragments, re.I):
                    raise ValueError(f"SVG resources must be local fragments: {path.name}")
        node.attrib.clear()
        node.attrib.update(values)
    root.set("xmlns", NAMESPACE)
    root.set("class", "vector-image")
    root.set("role", "img")
    root.set("aria-label", alt)
    root.set("font-family", "MiSans, sans-serif")
    return ET.tostring(root, encoding="unicode", short_empty_elements=False)
