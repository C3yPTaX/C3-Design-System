"""Erzeugt das Programmicon eines Produkts aus Rahmenvorlage und Produktzeichen.

    python scripts/build-product-icon.py <zeichen.svg> <zielordner> [--name NAME]

Das Zeichen ist eine SVG-Datei mit viewBox "0 0 100 100" und einem oder
mehreren <path>-Elementen in einer Farbe. Löcher entstehen über evenodd.
Regeln für das Zeichen stehen in guidelines/branding.md.

Ausgabe im Zielordner:
    NAME.ico                 alle Größen in einer Datei
    NAME-icon-<größe>.png    jede Größe einzeln

Bis 32 px zeigt das Icon das Zeichen auf einer kleinen Chip-Platte, darüber das
Zeichen im Chip-Rahmen.
Der Hintergrund ist transparent, dunkel ist nur das Innere des Chips.
Die Vorlage assets/product-icon/c3-product-frame.svg wird nur gelesen.

Benötigt Pillow und resvg-py (pip install pillow resvg-py).
"""

import argparse
import io
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import resvg_py
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "assets" / "product-icon" / "c3-product-frame.svg"

ICON_SIZES = [16, 20, 24, 32, 40, 48, 64, 128, 256]
SMALL_ICON_MAX = 32      # bis zu dieser Größe nur das Zeichen, darüber mit Rahmen
FRAME_SHARE = 0.96       # Anteil des Rahmens an der Icon-Fläche

SYMBOL_GRID = "0 0 100 100"
# Kleine Icons: Das Zeichen sitzt auf einer dunklen Platte in Form des Chips,
# damit es auch auf hellem Grund lesbar bleibt (viewBox 128 x 128).
SMALL_VIEWBOX = "0 0 128 128"
SMALL_SYMBOL = 'x="22" y="22" width="84" height="84"'
SMALL_PLATE = ('<path d="M26,4 H102 L124,26 V102 L102,124 H26 L4,102 V26 Z" '
               'fill="#01070C" stroke="#07FCFD" stroke-width="5"/>')

SVG_NS = "{http://www.w3.org/2000/svg}"


def read_symbol(path: Path) -> str:
    """Liest alle Pfade des Zeichens und gibt sie als einen Pfad zurück."""
    root = ET.parse(path).getroot()
    if " ".join(root.get("viewBox", "").split()) != SYMBOL_GRID:
        sys.exit(f'{path.name}: viewBox muss "{SYMBOL_GRID}" sein.')
    parts = [p.get("d", "").strip() for p in root.iter(f"{SVG_NS}path")]
    parts = [d for d in parts if d]
    if not parts:
        sys.exit(f"{path.name}: kein <path> mit Pfaddaten gefunden.")
    return " ".join(parts)


def compose(template: str, d: str, with_frame: bool) -> str:
    """Setzt das Zeichen in die Vorlage ein. Ohne Rahmen bleibt nur das Zeichen."""
    svg, n = re.subn(r'(<path id="zeichen"[^>]*\sd=")[^"]*(")', lambda m: m.group(1) + d + m.group(2), template)
    if n != 1:
        sys.exit("Vorlage: Pfad mit id zeichen nicht gefunden.")
    if with_frame:
        return svg
    svg, n = re.subn(r"<!-- VORLAGE: Rahmen Anfang -->.*?<!-- VORLAGE: Rahmen Ende -->", "", svg, flags=re.S)
    if n != 1:
        sys.exit("Vorlage: Marken für den Rahmen nicht gefunden.")
    svg = re.sub(r'viewBox="[^"]*" width="\d+" height="\d+"', f'viewBox="{SMALL_VIEWBOX}"', svg, count=1)
    svg = re.sub(r'(<svg id="produktzeichen") x="[^"]*" y="[^"]*" width="[^"]*" height="[^"]*"',
                 lambda m: SMALL_PLATE + "\n  " + m.group(1) + " " + SMALL_SYMBOL, svg, count=1)
    return svg


def render(svg: str, size: int) -> Image.Image:
    png = resvg_py.svg_to_bytes(svg_string=svg, width=size, height=size)
    return Image.open(io.BytesIO(bytes(png))).convert("RGBA")


def icon(template: str, d: str, size: int) -> Image.Image:
    """Icon mit transparentem Hintergrund. Dunkel ist nur das Innere des Chip-Rahmens."""
    if size <= SMALL_ICON_MAX:
        return render(compose(template, d, with_frame=False), size)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    art = render(compose(template, d, with_frame=True), round(size * FRAME_SHARE))
    canvas.alpha_composite(art, ((size - art.width) // 2, (size - art.height) // 2))
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser(description="Programmicon eines Produkts erzeugen.")
    parser.add_argument("zeichen", type=Path, help="SVG-Datei mit dem Produktzeichen")
    parser.add_argument("zielordner", type=Path, help="Ordner für ICO und PNG")
    parser.add_argument("--name", help="Dateiname ohne Endung, Standard ist der Name der Zeichen-Datei")
    args = parser.parse_args()

    name = args.name or args.zeichen.stem
    d = read_symbol(args.zeichen)
    template = TEMPLATE.read_text(encoding="utf-8")
    args.zielordner.mkdir(parents=True, exist_ok=True)

    icons = {s: icon(template, d, s) for s in ICON_SIZES}
    for s, im in icons.items():
        im.save(args.zielordner / f"{name}-icon-{s}.png", optimize=True)
    icons[ICON_SIZES[-1]].save(
        args.zielordner / f"{name}.ico",
        format="ICO",
        sizes=[(s, s) for s in ICON_SIZES],
        append_images=[icons[s] for s in ICON_SIZES[:-1]],
    )

    print(f"Icon erzeugt: {args.zielordner / (name + '.ico')}")


if __name__ == "__main__":
    main()
