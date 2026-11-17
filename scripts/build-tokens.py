"""Erzeugt plattformspezifische Token-Dateien aus tokens/tokens.json.

    python scripts/build-tokens.py          schreibt die Dateien
    python scripts/build-tokens.py --check  prüft nur, ob sie aktuell sind

Ausgaben:
    tokens/c3.css          CSS Custom Properties für HTML-Projekte
    tokens/c3-theme.ps1    Hashtable $C3 für PowerShell und WinForms

Keine Abhängigkeiten außer Python 3.9 oder neuer.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tokens" / "tokens.json"
OUT_CSS = ROOT / "tokens" / "c3.css"
OUT_PS1 = ROOT / "tokens" / "c3-theme.ps1"

HEADER = "Generiert aus tokens/tokens.json mit scripts/build-tokens.py. Nicht von Hand bearbeiten."

# WinForms kennt keine Fallback-Listen. Diese Schriften sind auf jedem Windows vorhanden.
WINFORMS_FONTS = {"ui": "Segoe UI", "mono": "Consolas"}


def flatten(node, path=(), inherited_type=None, out=None):
    """Liefert {('color','accent','default'): (type, value)}."""
    if out is None:
        out = {}
    t = node.get("$type", inherited_type)
    if "$value" in node:
        out[path] = (t, node["$value"])
        return out
    for key, child in node.items():
        if key.startswith("$"):
            continue
        flatten(child, path + (key,), t, out)
    return out


REF = re.compile(r"^\{([^}]+)\}$")


def resolve(value, tokens, seen=()):
    if isinstance(value, str):
        m = REF.match(value)
        if m:
            key = tuple(m.group(1).split("."))
            if key in seen or key not in tokens:
                raise SystemExit(f"Ungültige Referenz: {value}")
            return resolve(tokens[key][1], tokens, seen + (key,))
        return value
    if isinstance(value, dict):
        return {k: resolve(v, tokens, seen) for k, v in value.items()}
    if isinstance(value, list):
        return [resolve(v, tokens, seen) for v in value]
    return value


def css_name(path):
    return "--c3-" + "-".join(re.sub(r"(?<!^)(?=[A-Z])", "-", p).lower() for p in path)


def css_family(families):
    generic = {"sans-serif", "serif", "monospace", "system-ui", "-apple-system", "BlinkMacSystemFont"}
    return ", ".join(f if f in generic else f'"{f}"' for f in families)


def css_value(t, v, path, tokens):
    raw = tokens[path][1]
    ref = REF.match(raw) if isinstance(raw, str) else None
    if ref:  # Referenzen bleiben im CSS als var() erhalten
        return f"var({css_name(tuple(ref.group(1).split('.')))})"
    if t == "fontFamily":
        return css_family(v)
    if t == "cubicBezier":
        return "cubic-bezier({})".format(", ".join(str(x) for x in v))
    if t == "shadow":
        return f"{v['offsetX']} {v['offsetY']} {v['blur']} {v['spread']} {v['color']}"
    if t == "typography":
        return "{w} {s}/{lh} {f}".format(
            w=v["fontWeight"], s=v["fontSize"], lh=v["lineHeight"], f=css_family(v["fontFamily"])
        )
    return str(v)


def build_css(tokens):
    lines = [f"/* {HEADER} */", "", ":root {", "  color-scheme: dark;"]
    group = None
    for path, (t, _) in tokens.items():
        if path[0] != group:
            group = path[0]
            lines.append("")
        v = resolve(tokens[path][1], tokens)
        lines.append(f"  {css_name(path)}: {css_value(t, v, path, tokens)};")
    lines.append("}")
    lines += [
        "",
        "/* Reduzierte Bewegung: keine Wege und Skalierungen, Farb- und Deckkraftwechsel bleiben. */",
        "@media (prefers-reduced-motion: reduce) {",
        "  :root {",
    ]
    for path, (t, _) in tokens.items():
        if path[:2] == ("motion", "distance"):
            lines.append(f"    {css_name(path)}: 0px;")
        if path[:2] == ("motion", "scale"):
            lines.append(f"    {css_name(path)}: 1;")
    lines += ["  }", "}", ""]
    return "\n".join(lines)


def ps_color(hexv):
    h = hexv.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    a = int(h[6:8], 16) if len(h) == 8 else 255
    return f"[System.Drawing.Color]::FromArgb({a}, {r}, {g}, {b})"


def ps_number(x):
    return str(int(x)) if float(x).is_integer() else repr(float(x))


def px(v):
    return float(str(v).removesuffix("px"))


def build_ps1(tokens):
    tree = {}

    def put(keys, value):
        node = tree
        for k in keys[:-1]:
            node = node.setdefault(k, {})
        node[keys[-1]] = value

    for path, (t, _) in tokens.items():
        v = resolve(tokens[path][1], tokens)
        top = path[0]
        if top == "color":
            put(("Color",) + path[1:], ps_color(v))
        elif top == "font" and path[1] == "family":
            put(("Font", "Family", path[2]), f"'{WINFORMS_FONTS[path[2]]}'")
        elif top == "font" and path[1] == "size":
            put(("Font", "SizePt", path[2]), ps_number(px(v) * 0.75))
        elif top == "font" and path[1] == "weight":
            put(("Font", "Weight", path[2]), ps_number(v))
        elif top in ("space", "radius", "size"):
            put((top.capitalize(),) + path[1:], ps_number(px(v)))
        elif top == "motion" and path[1] == "duration":
            put(("Motion", "DurationMs", path[2]), ps_number(float(v.removesuffix("ms"))))
        elif top == "motion" and path[1] == "easing":
            put(("Motion", "Easing", path[2]), "@(" + ", ".join(ps_number(x) for x in v) + ")")
        elif top == "motion" and path[1] == "distance":
            put(("Motion", "DistancePx", path[2]), ps_number(px(v)))
        elif top == "motion" and path[1] == "scale":
            put(("Motion", "Scale", path[2]), ps_number(v))
        # typography und shadow: in WinForms über Font-Objekte bzw. nicht abbildbar

    def emit(node, indent):
        pad = "    " * indent
        out = []
        for k, v in node.items():
            key = k[0].upper() + k[1:] if k[0].isalpha() else k
            if isinstance(v, dict):
                out.append(f"{pad}'{key}' = @{{")
                out += emit(v, indent + 1)
                out.append(f"{pad}}}")
            else:
                out.append(f"{pad}'{key}' = {v}")
        return out

    lines = [
        f"# {HEADER}",
        "#",
        "# Verwendung:  . \"$PSScriptRoot\\c3-theme.ps1\"",
        "#              $form.BackColor = $C3.Color.Bg.Canvas",
        "#              $font = New-Object System.Drawing.Font($C3.Font.Family.Ui, $C3.Font.SizePt.Md)",
        "# Schriftgrößen in Punkt, Maße in Pixel bei 96 dpi, Dauer in Millisekunden.",
        "",
        "Add-Type -AssemblyName System.Drawing",
        "",
        "$C3 = @{",
    ]
    lines += emit(tree, 1)
    lines += ["}", ""]
    return "\n".join(lines)


def main():
    tokens = flatten(json.loads(SRC.read_text(encoding="utf-8")))
    outputs = {OUT_CSS: build_css(tokens), OUT_PS1: build_ps1(tokens)}
    if "--check" in sys.argv:
        stale = [p.name for p, text in outputs.items()
                 if not p.exists() or p.read_text(encoding="utf-8-sig") != text]
        if stale:
            raise SystemExit("Veraltet, bitte scripts/build-tokens.py ausführen: " + ", ".join(stale))
        print("Token-Dateien sind aktuell.")
        return
    for p, text in outputs.items():
        # Windows PowerShell 5.1 liest UTF-8 nur mit BOM korrekt
        enc = "utf-8-sig" if p.suffix == ".ps1" else "utf-8"
        p.write_text(text, encoding=enc, newline="\n")
    print(f"{len(tokens)} Tokens geschrieben.")


if __name__ == "__main__":
    main()
