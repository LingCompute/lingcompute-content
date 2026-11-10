import base64
import hashlib
import io
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache/fonts"
URL = "https://hyperos.mi.com/font-download/MiSans.zip"
WEIGHTS = {
    "Regular": (400, "d704c1a932c0bd7e8a071d276cd81c0ed0c9fecfa26ac234f4bed0559fe1cb2d"),
    "Medium": (500, "44e28ca6c2f0ca79829f192831ef87b5eec7c464f5cfb7a83467f57bb6e58114"),
    "Semibold": (600, "78227c6ec59566785c65ac0b5312328bfa2f879918f3d7403725785615a9a8f6"),
}


def checked(data, expected):
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("MiSans font fingerprint changed; verify the official download before updating")
    return data


def font_style(cache=CACHE):
    rules = []
    for name, (weight, fingerprint) in WEIGHTS.items():
        path = cache / f"MiSans-{name}.woff2"
        if not path.is_file():
            raise ValueError("MiSans fonts missing; run python tools/fonts.py before building")
        encoded = base64.b64encode(checked(path.read_bytes(), fingerprint)).decode()
        rules.append(
            '@font-face{font-family:"MiSans";font-style:normal;'
            f'font-weight:{weight};font-display:block;'
            f'src:url("data:font/woff2;base64,{encoded}") format("woff2")}}'
        )
    return "\n".join(rules)


def install():
    if all(
        (path := CACHE / f"MiSans-{name}.woff2").is_file()
        and hashlib.sha256(path.read_bytes()).hexdigest() == fingerprint
        for name, (_, fingerprint) in WEIGHTS.items()
    ):
        print("MiSans Regular / Medium / Semibold fingerprints verified")
        return
    with urlopen(URL, timeout=60) as response:
        archive = ZipFile(io.BytesIO(response.read()))
    fonts = {
        name: checked(archive.read(f"MiSans/woff2/MiSans-{name}.woff2"), fingerprint)
        for name, (_, fingerprint) in WEIGHTS.items()
    }
    CACHE.mkdir(parents=True, exist_ok=True)
    for name, data in fonts.items():
        (CACHE / f"MiSans-{name}.woff2").write_bytes(data)
    print("Prepared original MiSans Regular / Medium / Semibold for embedded previews")


if __name__ == "__main__":
    install()
