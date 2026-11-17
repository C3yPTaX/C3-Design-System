"""Qualitätsprüfung des Design-Systems.

    python scripts/check.py

Prüft:
    1. Originale unverändert (SHA-256)
    2. Generierte Token-Dateien aktuell
    3. Kontraste der festgelegten Farbpaare (WCAG 2.2)
    4. Sprachregeln in Dokumentation und Beispielen
    5. Keine privaten Daten (E-Mail-Adressen, Telefonnummern)
    6. ICO-Datei enthält alle Größen

Benötigt Pillow für Punkt 6. Ohne Pillow wird dieser Punkt übersprungen.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def fail(msg):
    errors.append(msg)


# 1. Originale -----------------------------------------------------------------
sums = ROOT / "assets" / "originals" / "SHA256SUMS"
for line in sums.read_text().splitlines():
    digest, name = line.split(maxsplit=1)
    f = sums.parent / name
    if not f.exists():
        fail(f"Original fehlt: {name}")
    elif hashlib.sha256(f.read_bytes()).hexdigest() != digest:
        fail(f"Original verändert: {name}")

# 2. Tokens --------------------------------------------------------------------
r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build-tokens.py"), "--check"],
                   capture_output=True, text=True)
if r.returncode != 0:
    fail((r.stderr or r.stdout).strip())

# 3. Kontraste -----------------------------------------------------------------
tokens = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))


def tok(path):
    node = tokens
    for p in path.split("."):
        node = node[p]
    v = node["$value"]
    return tok(v[1:-1]) if v.startswith("{") else v


def lum(hexv):
    h = hexv.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


TEXT, UI = 4.5, 3.0
pairs = []
for bg in ("bg.canvas", "bg.subtle", "surface.card", "surface.input", "surface.popover"):
    for fg in ("text.primary", "text.secondary", "text.muted", "accent.text",
               "status.success", "status.warning", "status.danger"):
        pairs.append((fg, bg, TEXT))
    pairs.append(("border.focus", bg, UI))
    pairs.append(("accent.default", bg, UI))
pairs += [
    ("text.primary", "surface.control", TEXT),
    ("text.primary", "surface.controlHover", TEXT),
    ("text.onAccent", "accent.default", TEXT),
    ("text.onAccent", "accent.hover", TEXT),
    ("text.onAccent", "accent.pressed", TEXT),
    ("text.primary", "accent.subtle", TEXT),
    ("accent.text", "accent.subtle", TEXT),
    ("status.success", "status.successSubtle", TEXT),
    ("status.warning", "status.warningSubtle", TEXT),
    ("status.danger", "status.dangerSubtle", TEXT),
    ("#FFFFFF", "status.dangerSolid", TEXT),
    ("#FFFFFF", "status.dangerSolidHover", TEXT),
]
for fg, bg, need in pairs:
    a = fg if fg.startswith("#") else tok("color." + fg)
    b = tok("color." + bg)
    got = ratio(a, b)
    if got < need:
        fail(f"Kontrast {fg} auf {bg}: {got:.2f} < {need}")

# 4. Sprachregeln --------------------------------------------------------------
FORBIDDEN = {
    "–": "Halbgeviertstrich",
    "—": "Geviertstrich",
    "»": "Doppel-Chevron",
    "«": "Doppel-Chevron",
    "≫": "Doppel-Chevron",
    "…": "Auslassungszeichen",
    "...": "drei Punkte",
    ">>": "Doppel-Chevron",
}


def prose(text, suffix):
    if suffix == ".md":
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    else:  # HTML: nur sichtbarer Text
        text = re.sub(r"<(script|style)\b.*?</\1>", "", text, flags=re.S | re.I)
        text = re.sub(r"<code\b.*?</code>", "", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
    return text


docs = [p for p in ROOT.rglob("*") if p.suffix in (".md", ".html") and ".git" not in p.parts]
for p in docs:
    text = prose(p.read_text(encoding="utf-8"), p.suffix)
    for n, line in enumerate(text.splitlines(), 1):
        for ch, name in FORBIDDEN.items():
            if ch in line:
                fail(f"{p.relative_to(ROOT)}: {name} in Zeile mit '{line.strip()[:60]}'")

# 5. Private Daten -------------------------------------------------------------
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?<![\w#.])\+?\d[\d /-]{8,}\d(?![\w])")
ALLOWED_EMAIL = {"noreply@anthropic.com"}
for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts or p.suffix not in (".md", ".html", ".json", ".css", ".ps1", ".py", ".yml"):
        continue
    text = p.read_text(encoding="utf-8")
    for m in EMAIL.findall(text):
        if m not in ALLOWED_EMAIL:
            fail(f"{p.relative_to(ROOT)}: E-Mail-Adresse {m}")
    if p.suffix in (".md", ".html"):
        for m in PHONE.findall(prose(text, p.suffix)):
            fail(f"{p.relative_to(ROOT)}: mögliche Telefonnummer {m}")

# 6. ICO -----------------------------------------------------------------------
try:
    from PIL import Image
    ico = Image.open(ROOT / "assets" / "icon" / "c3yptax.ico")
    want = {(s, s) for s in (16, 20, 24, 32, 40, 48, 64, 128, 256)}
    if set(ico.info["sizes"]) != want:
        fail(f"ICO-Größen unvollständig: {sorted(ico.info['sizes'])}")
except ImportError:
    print("Pillow fehlt, ICO-Prüfung übersprungen.")

if errors:
    print("Fehler:")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print(f"Alle Prüfungen bestanden ({len(pairs)} Farbpaare, {len(docs)} Dokumente).")
