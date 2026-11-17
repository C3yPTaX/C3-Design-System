# Branding

Alle Dateien liegen in [`assets/`](../assets/). Die Originale in `assets/originals/` bleiben unverändert. Alle anderen Dateien werden mit `python scripts/build-assets.py` daraus erzeugt.

## Übersicht

| Asset | Datei | Einsatz |
| --- | --- | --- |
| Hauptlogo mit Schriftzug | `logo/c3yptax-logo-{256,512,1024}.png` | Startbildschirm, Über-Dialog, README, Dokumentation |
| Kompaktlogo ohne Schrift | `mark/c3yptax-mark-{128,256,512}.png` | Wenn der Name schon sichtbar ist oder wenig Platz ist |
| Programmicon | `icon/c3yptax.ico` | EXE, Taskleiste, Fenstertitel, Verknüpfungen |
| Programmicon als PNG | `icon/c3yptax-icon-{16 bis 256}.png` | Favicon, Web-Manifest, plattformübergreifende Apps |
| Profilbild | `profile/c3yptax-avatar-{256,512,1024}.jpg` | GitHub, Foren, Social Media |
| Wallpaper mit Schriftzug | `originals/c3yptax-wallpaper-wordmark-*.webp` | Desktop, Präsentationstitel |
| Wallpaper ohne Schriftzug | `originals/c3yptax-wallpaper-1920x1080.webp` | Desktop, Hintergrund für Titelfolien mit eigenem Text |

## Originale

| Datei | Größe | Inhalt |
| --- | --- | --- |
| `c3yptax-logo.webp` | 1254 x 1254 | Chip mit C3, Symbolen und Schriftzug |
| `c3yptax-mark.jpg` | 1254 x 1254 | Chip mit C3 im Kreis, ohne Schrift |
| `c3yptax-wallpaper-wordmark-2000x1125.webp` | 2000 x 1125 | Wallpaper mit Schriftzug |
| `c3yptax-wallpaper-wordmark-1920x1080.webp` | 1920 x 1080 | Wallpaper mit Schriftzug |
| `c3yptax-wallpaper-1920x1080.webp` | 1920 x 1080 | Wallpaper ohne Schriftzug |

Die Prüfsummen stehen in `assets/originals/SHA256SUMS`. `scripts/check.py` meldet jede Veränderung.

Größere Varianten als die Originale werden nicht erzeugt, weil Hochskalieren unscharf wird. Für 4K-Wallpaper braucht es neue Originale.

## Programmicon

Das Icon ist ein abgerundetes Quadrat in der Hintergrundfarbe der Grafiken (`color.brand.deep`) mit transparenten Ecken.

- **16 bis 32 px:** nur die Buchstaben C3. Rahmen und Kreis wären in dieser Größe nur Rauschen.
- **ab 40 px:** C3 im Chip-Rahmen.

Beide Varianten stecken gemeinsam in `c3yptax.ico` (16, 20, 24, 32, 40, 48, 64, 128, 256 px). Windows wählt je nach Anzeige automatisch die passende Größe, auch bei 125 und 150 Prozent Skalierung.

Verwendung:

- EXE-Dateien, Taskleiste, Fenstersymbol, Startmenü: ja.
- Ordner wie `App`: **kein** eigenes Ordnersymbol, keine `desktop.ini`.
- In WinForms: `$form.Icon = New-Object System.Drawing.Icon($pfad)`. Beispiel in [`examples/winforms-demo.ps1`](../examples/winforms-demo.ps1).
- Im Web: `icon/c3yptax-icon-32.png` und `-64.png` als Favicon.

## Regeln

- Logos immer auf dunklem Grund. Die Grafiken haben einen eingebauten schwarzen Hintergrund und sind nicht für helle Flächen gedacht.
- Um das Logo bleibt Freiraum von mindestens einem Viertel seiner Breite.
- Logos nicht verzerren, umfärben, beschneiden oder mit Effekten versehen.
- In der Titelleiste einer Anwendung steht das Icon in 16 bis 20 px, nie das Hauptlogo.
- Wallpaper sind keine GUI-Hintergründe. Hinter Formularen, Tabellen und Text bleibt die Fläche ruhig und einfarbig.
- Komplette Wallpaper nie als Icon, Logos nie als dauerhafter Hintergrund.
- Ein Splash-Screen darf das Hauptlogo groß auf `color.brand.deep` zeigen, für höchstens die Dauer des Ladevorgangs.

## Produktnamen

Produkte heißen `C3-Name`. In Fenstertiteln steht der Produktname, nicht `C3yPTaX`. Die Marke erscheint im Über-Dialog und in der Dokumentation.
