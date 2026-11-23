# Branding

Alle Dateien liegen in [`assets/`](../assets/). Die Originale in `assets/originals/` bleiben unverändert. Alle anderen Dateien werden daraus erzeugt: Logos, Icons und Profilbild mit `python scripts/build-assets.py`, die Wallpaper mit `python scripts/build-wallpapers.py`.

## Übersicht

| Asset | Datei | Einsatz |
| --- | --- | --- |
| Hauptlogo mit Schriftzug | `logo/c3yptax-logo-{256,512,1024}.png` | Startbildschirm, Über-Dialog, README, Dokumentation |
| Kompaktlogo ohne Schrift | `mark/c3yptax-mark-{128,256,512}.png` | Wenn der Name schon sichtbar ist oder wenig Platz ist |
| Marken-Icon | `icon/c3yptax.ico` | Zeichen der Marke, Programmicon für Produkte ohne eigenes Produkt-Icon |
| Marken-Icon als PNG | `icon/c3yptax-icon-{16 bis 256}.png` | Favicon, Web-Manifest, plattformübergreifende Apps |
| Vorlage für Produkt-Icons | `product-icon/c3-product-frame.svg` | Eigenes Programmicon je Produkt, siehe unten |
| Icon des Design-Systems | `product-icon/c3-designsystem/` | Produkt-Icon von C3-DesignSystem mit seinem Zeichen |
| Profilbild | `profile/c3yptax-avatar-{256,512,1024}.jpg` | GitHub, Foren, Social Media |
| Wallpaper mit Schriftzug | `wallpaper/c3yptax-wallpaper-wordmark-{1920x1080,2560x1440,3840x2160}.png` | Desktop, Präsentationstitel |
| Wallpaper ohne Schriftzug | `wallpaper/c3yptax-wallpaper-{1920x1080,2560x1440,3840x2160}.png` | Desktop, Hintergrund für Titelfolien mit eigenem Text |

## Originale

| Datei | Größe | Inhalt |
| --- | --- | --- |
| `c3yptax-logo.webp` | 1254 x 1254 | Chip mit C3, Symbolen und Schriftzug |
| `c3yptax-mark.jpg` | 1254 x 1254 | Chip mit C3 im Kreis, ohne Schrift |

Die Prüfsummen stehen in `assets/originals/SHA256SUMS`. `scripts/check.py` meldet jede Veränderung.

Logos, Icons und Profilbild werden nicht größer als die Originale erzeugt, weil Hochskalieren unscharf wird.

## Wallpaper

Die Wallpaper gibt es in Full HD, WQHD und 4K, jeweils mit und ohne Schriftzug. Sie werden aus `c3yptax-mark.jpg` und dem Schriftzug aus `c3yptax-logo.webp` zusammengesetzt.

- Das Logo bleibt unverändert und steht kleiner in der Mitte.
- Der Grund ist ruhig: `color.brand.deep` mit einem weichen Lichthof in `color.brand.glow`.
- Keine Schaltkreislinien, keine Lichtkeile, keine HUD-Leiste.
- Die Ränder bleiben frei, damit Desktopsymbole und Taskleiste nichts verdecken.

Auch die 4K-Fassung ist echt. Der Grund wird in jeder Auflösung neu berechnet, und das Logo wird nirgends hochskaliert: In 4K ist es 900 px breit, das Original hat 1254 px.

## Marken-Icon

Das Marken-Icon ist ein abgerundetes Quadrat in der Hintergrundfarbe der Grafiken (`color.brand.deep`) mit transparenten Ecken.

- **16 bis 32 px:** nur die Buchstaben C3. Rahmen und Kreis wären in dieser Größe nur Rauschen.
- **ab 40 px:** C3 im Chip-Rahmen.

Beide Varianten stecken gemeinsam in `c3yptax.ico` (16, 20, 24, 32, 40, 48, 64, 128, 256 px). Windows wählt je nach Anzeige automatisch die passende Größe, auch bei 125 und 150 Prozent Skalierung.

Verwendung:

- EXE-Dateien, Taskleiste, Fenstersymbol, Startmenü: nur für Produkte ohne eigenes Produkt-Icon (siehe unten).
- Ordner wie `App`: **kein** eigenes Ordnersymbol, keine `desktop.ini`.
- In WinForms: `$form.Icon = New-Object System.Drawing.Icon($pfad)`. Beispiel in [`examples/winforms-demo.ps1`](../examples/winforms-demo.ps1).
- Im Web: `icon/c3yptax-icon-32.png` und `-64.png` als Favicon.

## Produkt-Icons

Jedes Produkt bekommt ein eigenes Programmicon, damit sich die Anwendungen auf dem Desktop und in der Taskleiste unterscheiden. Der Chip-Rahmen bleibt bei allen gleich, in der Mitte steht statt C3 ein Produktzeichen. Das Icon mit C3 bleibt das Zeichen der Marke. Solange ein Produkt kein eigenes Zeichen hat, nutzt es `icon/c3yptax.ico`.

- **16 bis 32 px:** das Produktzeichen auf einer kleinen dunklen Platte in Form des Chips.
- **ab 40 px:** Produktzeichen im Chip-Rahmen.
- **Hintergrund:** transparent. Dunkel ist nur das Innere des Chips, es gibt keine quadratische Kachel. So sitzt das Icon auf hellem und dunklem Desktop ohne dunklen Rand.

Die Vorlage liegt in `product-icon/c3-product-frame.svg`. `python scripts/build-product-icon.py <zeichen.svg> <zielordner>` setzt ein Zeichen ein und erzeugt ICO und PNG in allen Größen (benötigt Pillow und resvg-py). Zwei Beispiele mit Übersicht stehen in [`examples/product-icons/`](../examples/product-icons/).

Regeln für das Zeichen:

- SVG mit einem Raster von 100 x 100. Das Zeichen bleibt zwischen 6 und 94.
- Eine geschlossene Fläche in einer Farbe, Löcher über `evenodd`. Farbe, Lichtkante und Schein kommen aus der Vorlage.
- Stege und Lücken mindestens 8 Einheiten breit. Feinere Details verschwinden bei 16 px.
- Gerade Kanten und Abschrägungen im Winkel von 45 Grad, passend zu den Buchstaben des Logos.
- Ein Motiv, das die Aufgabe des Produkts zeigt. Keine Buchstaben, kein C3, keine Motive des Logos wie Fadenkreuz oder Leiterbahnen.
- Das fertige Icon und sein Zeichen liegen im Produkt, nicht im Design-System.

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
