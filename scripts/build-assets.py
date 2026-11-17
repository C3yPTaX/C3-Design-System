"""Erzeugt alle abgeleiteten Branding-Dateien aus assets/originals.

Die Originale werden nur gelesen. Aufruf aus dem Repository-Wurzelordner:

    python scripts/build-assets.py

Benötigt Pillow (pip install pillow).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / "assets" / "originals"
OUT = ROOT / "assets"

# Hintergrundfarbe der Originalgrafiken (gemessen), Token color.brand.deep
TILE = (1, 7, 12)

# Ausschnitte aus c3yptax-mark.jpg (1254 x 1254)
CROP_FRAME = (222, 247, 1032, 1057)   # Chip-Rahmen mit C3, quadratisch
CROP_LETTERS = (262, 442, 992, 812)   # nur die Buchstaben C3

ICON_SIZES = [16, 20, 24, 32, 40, 48, 64, 128, 256]
SMALL_ICON_MAX = 32  # bis zu dieser Größe nur die Buchstaben, darüber der Rahmen


def rounded_mask(size: int, radius: int) -> Image.Image:
    scale = 4  # supersampling für glatte Kanten
    m = Image.new("L", (size * scale, size * scale), 0)
    ImageDraw.Draw(m).rounded_rectangle(
        (0, 0, size * scale - 1, size * scale - 1), radius * scale, fill=255
    )
    return m.resize((size, size), Image.LANCZOS)


def fit(img: Image.Image, width: int) -> Image.Image:
    height = round(img.height * width / img.width)
    out = img.resize((width, height), Image.LANCZOS)
    if width <= 64:
        out = out.filter(ImageFilter.UnsharpMask(radius=0.6, percent=60, threshold=1))
    return out


def icon(mark: Image.Image, size: int) -> Image.Image:
    tile = Image.new("RGB", (size, size), TILE)
    if size <= SMALL_ICON_MAX:
        art = fit(mark.crop(CROP_LETTERS), round(size * 0.94))
        radius = max(2, round(size * 0.18))
    else:
        art = fit(mark.crop(CROP_FRAME), round(size * 0.96))
        radius = round(size * 0.18)
    tile.paste(art, ((size - art.width) // 2, (size - art.height) // 2))
    result = tile.convert("RGBA")
    result.putalpha(rounded_mask(size, radius))
    return result


def main() -> None:
    logo = Image.open(ORIG / "c3yptax-logo.webp").convert("RGB")
    mark = Image.open(ORIG / "c3yptax-mark.jpg").convert("RGB")

    for d in ("logo", "mark", "icon", "profile"):
        (OUT / d).mkdir(exist_ok=True)

    # Hauptlogo mit Schriftzug
    for s in (1024, 512, 256):
        fit(logo, s).save(OUT / "logo" / f"c3yptax-logo-{s}.png", optimize=True)

    # Kompaktes Logo ohne Schrift, eng beschnitten auf den Rahmen
    frame = mark.crop(CROP_FRAME)
    for s in (512, 256, 128):
        fit(frame, s).save(OUT / "mark" / f"c3yptax-mark-{s}.png", optimize=True)

    # Programmicon
    icons = {s: icon(mark, s) for s in ICON_SIZES}
    for s, im in icons.items():
        im.save(OUT / "icon" / f"c3yptax-icon-{s}.png", optimize=True)
    largest = icons[ICON_SIZES[-1]]
    largest.save(
        OUT / "icon" / "c3yptax.ico",
        format="ICO",
        sizes=[(s, s) for s in ICON_SIZES],
        append_images=[icons[s] for s in ICON_SIZES[:-1]],
    )

    # Profilbild: komplettes Kompaktlogo, kreisförmig zuschneidbar
    for s in (1024, 512, 256):
        fit(mark, s).save(OUT / "profile" / f"c3yptax-avatar-{s}.jpg", quality=92, optimize=True)

    print("Assets erzeugt.")


if __name__ == "__main__":
    main()
