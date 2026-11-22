"""Erzeugt die Wallpaper aus assets/originals.

Die Originale werden nur gelesen. Aufruf aus dem Repository-Wurzelordner:

    python scripts/build-wallpapers.py

Aufbau: unverändertes Kompaktlogo, kleiner und mittig, auf ruhigem Grund mit
weichem Lichthof. Die Variante mit Schriftzug setzt den Schriftzug aus dem
Hauptlogo darunter. Das Logo wird in keiner Auflösung hochskaliert.

Benötigt Pillow und NumPy (pip install pillow numpy).
"""

from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / "assets" / "originals"
OUT = ROOT / "assets" / "wallpaper"

# Token color.brand.deep und color.brand.glow
DEEP = np.array([1, 7, 12], float)
GLOW = np.array([6, 59, 61], float)

# Alle Maße gelten für die Bezugsbreite und werden pro Auflösung skaliert.
BASE_WIDTH = 3840
SIZES = [(3840, 2160), (2560, 1440), (1920, 1080)]

MARK_SIZE = 900          # Kantenlänge des Kompaktlogos, kleiner als das Original
WORD_WIDTH = 620         # Breite des Schriftzugs
WORD_GAP = 40            # Abstand zwischen Logo und Schriftzug
CROP_WORD = (200, 955, 1054, 1082)  # Schriftzug in c3yptax-logo.webp (1254 x 1254)

CENTER_Y = 0.5           # Höhe der Logomitte ohne Schriftzug
CENTER_Y_WORD = 0.44     # mit Schriftzug etwas höher, damit das Paar mittig sitzt

BLACK_POINT = 16         # Schwarzwert der Grafiken, wird vor dem Aufhellen entfernt
FEATHER_MARK = 0.06      # weicher Rand, Anteil der kürzeren Kante
FEATHER_WORD = 0.15

HALO_RADIUS = (0.42, 0.62)      # Lichthof, Anteil von Breite und Höhe
HALO_FALLOFF = 2.2
HALO_STRENGTH = 0.55
VIGNETTE_RADIUS = (0.95, 1.1)
VIGNETTE_FALLOFF = 0.6
VIGNETTE_FLOOR = 0.72           # Helligkeit am äußersten Rand

# Rauschen gegen Ringe im Verlauf. Startwert und Reihenfolge nicht ändern,
# sonst ändern sich alle Bilder.
NOISE_SEED = 3
NOISE_LUMA = 1.1
NOISE_CHROMA = 0.6


def lift(img: Image.Image, black: int = BLACK_POINT) -> np.ndarray:
    """Schwarzen Grund der Grafik entfernen, damit sie per Screen sauber aufgeht."""
    a = np.asarray(img.convert("RGB"), float)
    return np.clip((a - black) / (255 - black), 0, 1)


def radial(w: int, h: int, cx: float, cy: float, rx: float, ry: float) -> np.ndarray:
    y, x = np.mgrid[0:h, 0:w]
    d = np.sqrt(((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2)
    return np.clip(1 - d, 0, 1)


def background(w: int, h: int, cy: float) -> np.ndarray:
    g = radial(w, h, w / 2, cy, w * HALO_RADIUS[0], h * HALO_RADIUS[1]) ** HALO_FALLOFF
    bg = DEEP + (GLOW - DEEP) * HALO_STRENGTH * g[..., None]
    v = radial(w, h, w / 2, h / 2, w * VIGNETTE_RADIUS[0], h * VIGNETTE_RADIUS[1]) ** VIGNETTE_FALLOFF
    bg *= (VIGNETTE_FLOOR + (1 - VIGNETTE_FLOOR) * v)[..., None]
    return bg / 255


def screen(bg: np.ndarray, layer: np.ndarray, x: int, y: int) -> None:
    h, w = layer.shape[:2]
    reg = bg[y:y + h, x:x + w]
    bg[y:y + h, x:x + w] = 1 - (1 - reg) * (1 - layer)


def feather(layer: np.ndarray, edge: float) -> np.ndarray:
    h, w = layer.shape[:2]
    y, x = np.mgrid[0:h, 0:w]
    d = np.minimum.reduce([x, y, w - 1 - x, h - 1 - y]) / (min(w, h) * edge)
    return layer * np.clip(d, 0, 1)[..., None]


def dither(bg: np.ndarray) -> Image.Image:
    """Dreieckig verteiltes Rauschen plus feines Korn, damit der Verlauf in 8 Bit keine Ringe bildet."""
    rng = np.random.default_rng(NOISE_SEED)
    luma = (rng.random(bg.shape[:2]) - rng.random(bg.shape[:2]))[..., None] * NOISE_LUMA
    chroma = (rng.random(bg.shape) - rng.random(bg.shape)) * NOISE_CHROMA
    out = bg * 255 + luma + chroma
    return Image.fromarray(np.clip(out, 0, 255).round().astype("uint8"))


def build(mark: Image.Image, word: Image.Image, w: int, h: int, with_word: bool) -> Image.Image:
    scale = w / BASE_WIDTH
    size = round(MARK_SIZE * scale)
    cy = h * (CENTER_Y_WORD if with_word else CENTER_Y)
    bg = background(w, h, cy)
    m = feather(lift(mark.resize((size, size), Image.LANCZOS)), FEATHER_MARK)
    screen(bg, m, (w - size) // 2, int(cy - size / 2))
    if with_word:
        ww = round(WORD_WIDTH * scale)
        wh = round(word.height * ww / word.width)
        wl = feather(lift(word.resize((ww, wh), Image.LANCZOS)), FEATHER_WORD)
        screen(bg, wl, (w - ww) // 2, int(cy + size / 2 + WORD_GAP * scale))
    # Das Rauschen kommt pro Auflösung ganz zum Schluss auf das fertige Bild.
    return dither(bg)


def main() -> None:
    mark = Image.open(ORIG / "c3yptax-mark.jpg")
    word = Image.open(ORIG / "c3yptax-logo.webp").crop(CROP_WORD)

    OUT.mkdir(exist_ok=True)
    for w, h in SIZES:
        for with_word, tag in ((False, ""), (True, "-wordmark")):
            name = f"c3yptax-wallpaper{tag}-{w}x{h}.png"
            build(mark, word, w, h, with_word).save(OUT / name, optimize=True)

    print("Wallpaper erzeugt.")


if __name__ == "__main__":
    main()
