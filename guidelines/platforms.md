# Umsetzung nach Plattform

Dieselbe Designsprache, nicht zwingend dieselben Komponenten. Jede Plattform nutzt ihre eigenen Mittel und liest die Werte aus den Tokens.

| Plattform | Datei | Einbindung |
| --- | --- | --- |
| HTML, CSS | `tokens/c3.css` | `<link rel="stylesheet" href="c3.css">`, Werte über `var(--c3-...)` |
| PowerShell, WinForms | `tokens/c3-theme.ps1` | `. .\c3-theme.ps1`, Werte über `$C3.Color.Accent.Default` |
| Alles andere | `tokens/tokens.json` | W3C Design Tokens, mit jedem JSON-Parser lesbar |

Die Dateien werden in das jeweilige Projekt kopiert, nicht verlinkt. So bleibt jedes Projekt eigenständig. Bei einem Update des Design-Systems werden sie erneut kopiert.

## HTML und CSS

```html
<link rel="stylesheet" href="tokens/c3.css">
<link rel="stylesheet" href="c3-ui.css"> <!-- optional: Referenzkomponenten -->
```

- `c3.css` enthält nur Variablen und die Regel für reduzierte Bewegung.
- [`examples/c3-ui.css`](../examples/c3-ui.css) ist eine fertige Umsetzung aller Komponenten mit dem Präfix `c3-`. Sie darf übernommen, gekürzt oder an ein Framework angepasst werden.
- In Frameworks wie React oder Vue werden die Variablen genauso verwendet. Für Tailwind lassen sich die Variablen in der Theme-Konfiguration referenzieren.
- Keine Webfonts laden. Der Font-Stack in `--c3-font-family-ui` nutzt die Systemschrift.

## PowerShell und WinForms

```powershell
. "$PSScriptRoot\c3-theme.ps1"

$form.BackColor = $C3.Color.Bg.Canvas
$form.ForeColor = $C3.Color.Text.Primary
$form.Font      = New-Object System.Drawing.Font($C3.Font.Family.Ui, $C3.Font.SizePt.Md)
$form.Icon      = New-Object System.Drawing.Icon("$PSScriptRoot\Resources\c3yptax.ico")
```

Vollständiges Beispiel: [`examples/winforms-demo.ps1`](../examples/winforms-demo.ps1).

### Schrift

WinForms rechnet in Punkt. `$C3.Font.SizePt` enthält die umgerechneten Werte (Pixel mal 0,75). Für Semibold wird die Schriftfamilie `Segoe UI Semibold` mit normalem Stil verwendet, nicht `FontStyle.Bold`.

| Stil | Punkt | Font |
| --- | --- | --- |
| title | 15 | Segoe UI Semibold |
| heading | 12 | Segoe UI Semibold |
| label | 9,75 | Segoe UI Semibold |
| body | 10,5 | Segoe UI |
| small | 9,75 | Segoe UI |
| caption | 9 | Segoe UI |
| code | 9,75 | Consolas |

Für sehr dichte Werkzeugoberflächen ist `body` mit 9,75 pt erlaubt. Kleiner als 9 pt wird nichts.

### Controls

- Standard-Controls von Windows sehen im dunklen Thema uneinheitlich aus. Buttons, Schalter, Checkboxen und Eingaberahmen werden deshalb selbst gezeichnet (`UserControl` oder abgeleitete Klasse mit `OnPaint`).
- Abgerundete Ecken über `GraphicsPath` mit `SmoothingMode.AntiAlias`. Radius aus `$C3.Radius`.
- Text mit `TextRenderer.DrawText` zeichnen, nicht mit `Graphics.DrawString`, damit er dem System entspricht. **Kein** `TextFormatFlags.EndEllipsis` für Beschriftungen: Texte werden passend gemacht, nicht abgeschnitten.
- `DoubleBuffered = $true` und `ControlStyles.OptimizedDoubleBuffer` gegen Flackern.
- `TextBox` und `ComboBox` behalten ihr natives Verhalten. Sie bekommen `BackColor = $C3.Color.Surface.Input`, `BorderStyle = None` und einen gezeichneten Rahmen im umgebenden Panel.
- DPI: Anwendung als DPI-bewusst starten (`SetProcessDpiAwareness` oder Manifest) und `AutoScaleMode = Dpi` setzen. Maße aus den Tokens gelten für 96 dpi und werden mit `DeviceDpi / 96` skaliert.

### Titelleiste unter Windows 10 und 11

Die native Titelleiste wird dunkel geschaltet, statt sie nachzubauen:

```powershell
Add-Type -Namespace C3 -Name Dwm -MemberDefinition @'
[DllImport("dwmapi.dll")] public static extern int DwmSetWindowAttribute(IntPtr hwnd, int attr, ref int value, int size);
'@
$on = 1
[C3.Dwm]::DwmSetWindowAttribute($form.Handle, 20, [ref]$on, 4) | Out-Null   # dunkler Modus
$caption = 0x0015120E  # Bg.Subtle #0E1215 als COLORREF (0x00BBGGRR), nur Windows 11
[C3.Dwm]::DwmSetWindowAttribute($form.Handle, 35, [ref]$caption, 4) | Out-Null
```

Ältere Windows-Versionen ignorieren die Aufrufe ohne Fehler.

### Animationen in WinForms

Nur Animationen, die zuverlässig und ohne spürbare Last laufen:

| Erlaubt | Umsetzung |
| --- | --- |
| Farbübergang bei Hover und Fokus | Farbe zwischen zwei Werten interpolieren, `Invalidate()` |
| Schalterknopf, Navigationsmarkierung, Tab-Unterstrich | Position innerhalb eines eigengezeichneten Controls interpolieren |
| Fortschrittsbalken | Breite des gezeichneten Balkens interpolieren |
| Dialog ein- und ausblenden | `Form.Opacity` von 0 auf 1, `slow` beim Öffnen, `fast` beim Schließen |
| Ladekreis | Winkel pro Tick erhöhen |

| Nicht erlaubt | Warum |
| --- | --- |
| Controls verschieben oder skalieren (`Location`, `Size`) | Layout-Neuberechnung, Flackern |
| Panels einblenden über Deckkraft von Child-Controls | WinForms kennt keine echte Transparenz für Controls |
| Mehrere Timer pro Fenster | Unnötige Last. Ein gemeinsamer Timer reicht |

Muster: ein einziger `System.Windows.Forms.Timer` mit 15 ms Intervall pro Fenster, der alle laufenden Animationen fortschreibt und sich selbst stoppt, wenn nichts mehr läuft. Fortschritt `t` von 0 bis 1 aus der verstrichenen Zeit, dann Kurve anwenden:

```csharp
// Kubische Bézierkurve wie in CSS. p = Tokenwerte, z. B. motion.easing.standard
static double Ease(double t, double x1, double y1, double x2, double y2) {
    double lo = 0, hi = 1, s = t;
    for (int i = 0; i < 12; i++) {           // x(s) = t per Bisektion lösen
        s = (lo + hi) / 2;
        double x = 3*(1-s)*(1-s)*s*x1 + 3*(1-s)*s*s*x2 + s*s*s;
        if (x < t) lo = s; else hi = s;
    }
    return 3*(1-s)*(1-s)*s*y1 + 3*(1-s)*s*s*y2 + s*s*s;
}
static Color Lerp(Color a, Color b, double t) =>
    Color.FromArgb((int)(a.A + (b.A - a.A) * t), (int)(a.R + (b.R - a.R) * t),
                   (int)(a.G + (b.G - a.G) * t), (int)(a.B + (b.B - a.B) * t));
```

### Reduzierte Bewegung in Windows

Windows hat die Einstellung `Animationseffekte` (Einstellungen, Barrierefreiheit, Visuelle Effekte). Abfrage:

```powershell
$animate = [System.Windows.Forms.SystemInformation]::UIEffectsEnabled
```

Ist der Wert `$false`, werden alle Dauern auf 0 gesetzt. Farbwechsel passieren dann sofort, Dialoge erscheinen ohne Einblenden.

## Andere Frameworks

`tokens/tokens.json` folgt dem Format der W3C Design Tokens Community Group:

- Farben als Hex, mit Alpha als achtstelliges Hex (`#RRGGBBAA`).
- Maße als Zeichenkette mit `px`, Dauer mit `ms`.
- Referenzen in geschweiften Klammern, z. B. `{color.accent.hover}`.

Werkzeuge wie Style Dictionary können daraus weitere Formate erzeugen (Swift, Kotlin, XAML, SCSS). Für einfache Fälle reicht ein eigenes Skript nach dem Vorbild von [`scripts/build-tokens.py`](../scripts/build-tokens.py).
