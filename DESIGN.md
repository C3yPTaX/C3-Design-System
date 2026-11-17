# C3yPTaX Designsprache

Dunkel, modern, technisch, minimalistisch, professionell.

Dieses Dokument beschreibt die verbindlichen Regeln. Die konkreten Werte stehen ausschließlich in [`tokens/tokens.json`](tokens/tokens.json). Wenn hier ein Wert genannt wird, dient er der Orientierung. Bei Abweichungen gilt die Token-Datei.

## 1. Haltung

**Das Logo darf auffallen. Die Oberfläche hält sich zurück.**

Die Markengrafiken von C3yPTaX sind bewusst futuristisch: Chip-Rahmen, Leuchtkonturen, Schaltkreislinien. Die Benutzeroberflächen übernehmen davon nur die Farbwelt und die Präzision, nicht die Effekte. Vorbild sind ruhige, hochwertige Desktop-Anwendungen.

| Wir wollen | Wir vermeiden |
| --- | --- |
| Nahezu schwarze Hintergründe, anthrazitfarbene Flächen | Neonflächen, Verläufe hinter Inhalten |
| Cyan gezielt für Hauptaktion, Fokus und Auswahl | Dauerhaftes Leuchten, Glow um Karten |
| Klare Raster und großzügige Abstände | HUD-Elemente, Fadenkreuze, Scanlinien in Formularen |
| Dezente Rahmen, abgerundete Ecken | Harte Kontraste zwischen allen Flächen |
| Kurze, weiche Übergänge | Bounce, große Zooms, Endlosanimationen ohne Grund |
| Kurze, vollständige Texte | Abgeschnittene Beschriftungen, Floskeln |

Ein guter Test: Ein Screenshot der Anwendung sollte auch ohne Logo seriös wirken und mit Logo sofort als C3yPTaX erkennbar sein.

## 2. Marke

`C3yPTaX` ist die übergeordnete Entwicklermarke. Produkte sind einzelne Anwendungen unter dieser Marke. Das Design-System gilt für alle Produkte gleichermaßen und enthält nichts Produktspezifisches.

Logos, Icons und Wallpaper sowie ihre Verwendung: [guidelines/branding.md](guidelines/branding.md).

## 3. Farbe

Alle Farben wurden aus den Originalgrafiken gemessen und für Bildschirmoberflächen abgestimmt.

### Herleitung

| In den Grafiken gemessen | Wert | Verwendung im UI |
| --- | --- | --- |
| Hintergrund der Grafiken | `#01070C` | Basis für `bg.canvas`, leicht aufgehellt auf `#0A0D10` |
| Leuchtendes Cyan der Konturen | `#07FCFD` | Zu kräftig für Flächen. Abgeleitet: `accent.default` `#19D4DC` |
| Türkis der Schaltkreise | `#06D0C4` | Abgeleitet: `secondary.default` `#1FC7B6` |
| Grüner Kern | `#48F762` | Abgeleitet: `status.success` `#3FD97A` |
| Helle Lichtkante | `#D5FDFE` | Inspiration für den leicht kühlen Ton von `text.primary` |

Die neutralen Grautöne sind leicht in Richtung des kühlen Blauschwarz der Marke verschoben.

### Rollen

| Rolle | Token | Wert | Wofür |
| --- | --- | --- | --- |
| Haupthintergrund | `color.bg.canvas` | `#0A0D10` | Fensterhintergrund |
| Nebenhintergrund | `color.bg.subtle` | `#0E1215` | Seitenleiste, Titel- und Statusleiste |
| Karte | `color.surface.card` | `#14181D` | Karten, Panels, Dialoge |
| Eingabe | `color.surface.input` | `#1A1F25` | Eingabefelder, Dropdowns |
| Popover | `color.surface.popover` | `#1C2127` | Menüs, Toasts, Tooltips |
| Bedienelement | `color.surface.control` | `#20262D` | Sekundäre Buttons |
| Trennlinie | `color.border.subtle` | `#232A31` | Tabellenzeilen, Trenner |
| Rahmen | `color.border.default` | `#2E363F` | Karten, Dialoge |
| Rahmen Eingabe | `color.border.control` | `#4B5661` | Eingabefelder, Checkboxen |
| Text | `color.text.primary` | `#E6EBEF` | Überschriften, Fließtext |
| Text zweiter Ordnung | `color.text.secondary` | `#A8B2BC` | Beschriftungen, Tabellenwerte |
| Gedämpft | `color.text.muted` | `#8A949E` | Hilfetexte, Platzhalter |
| Deaktiviert | `color.text.disabled` | `#5E6670` | Deaktivierte Elemente |
| Akzent | `color.accent.default` | `#19D4DC` | Hauptaktion, Fokus, aktive Auswahl |
| Akzent Hover | `color.accent.hover` | `#4DE2E8` | Hover, Fokusring, Links |
| Akzent Hintergrund | `color.accent.subtle` | `#0E2A2E` | Ausgewählte Zeile, aktive Navigation |
| Erfolg | `color.status.success` | `#3FD97A` | Verbunden, gespeichert |
| Warnung | `color.status.warning` | `#F5A524` | Achtung, Update nötig |
| Fehler | `color.status.danger` | `#FF6B70` | Fehlertext und Symbole |
| Destruktiv | `color.status.dangerSolid` | `#C8373E` | Fläche von Lösch-Buttons |

Die Farben unter `color.brand` sind **nur für Logo, Splash und Marketing**. Sie kommen in normalen Bedienelementen nicht vor.

### Regeln

1. **Sparsam.** Pro Ansicht gibt es höchstens eine gefüllte Cyan-Fläche: die Hauptaktion. Alles andere nutzt Cyan nur als Linie, Text oder Symbol.
2. **Grün ist Status.** Grün bedeutet Erfolg oder Verbindung und wird nie als Dekoration oder zweiter Akzent verwendet.
3. **Flächen staffeln sich nach Höhe.** Je weiter vorne eine Fläche liegt, desto heller ist sie: canvas, card, input, popover.
4. **Status nie nur über Farbe.** Immer Text oder Symbol dazu.
5. **Kontraste:** Text mindestens 4,5:1, Bedienelemente und Fokusring mindestens 3:1. `scripts/check.py` prüft das für alle festgelegten Kombinationen.
6. **Keine Farbwerte im Code.** Projekte lesen Farben aus den Token-Dateien.

## 4. Typografie

Systemschriften statt Webfonts: Segoe UI unter Windows, SF Pro unter macOS. Für Werte, Pfade und Logs Cascadia Mono oder Consolas. Die Schrift aus dem Logo wird in der Oberfläche nie nachgebaut, der Schriftzug erscheint nur als Bild.

| Stil | Größe | Gewicht | Verwendung |
| --- | --- | --- | --- |
| `display` | 28 px | Semibold | Selten: Kennzahlen, leere Startseiten |
| `title` | 20 px | Semibold | Seitentitel, einmal pro Ansicht |
| `heading` | 16 px | Semibold | Karten- und Dialogtitel |
| `label` | 13 px | Semibold | Feldbeschriftungen, Buttons, Tabs |
| `body` | 14 px | Regular | Fließtext, Tabellen, Eingaben |
| `small` | 13 px | Regular | Hilfetexte, Metadaten |
| `caption` | 12 px | Regular | Zeitstempel, Badges, Spaltenköpfe |
| `code` | 13 px | Regular, Monospace | Pfade, Werte |

Regeln:

- Nur zwei Gewichte: Regular und Semibold. Kein Bold, kein Light.
- Keine Großbuchstaben-Überschriften und kein gesperrter Text.
- Satzanfang groß, sonst normale Rechtschreibung. Keine Title Case Überschriften.
- Zahlen in Tabellen mit gleich breiten Ziffern (`tabular-nums`) und rechtsbündig.
- Fließtext höchstens etwa 70 Zeichen breit.

## 5. Raster, Abstände und Größen

Alle Abstände folgen einem 4-Pixel-Raster (`space.1` = 4 px bis `space.12` = 48 px).

| Situation | Abstand |
| --- | --- |
| Symbol zu Text, Elemente in einem Button | 8 px |
| Beschriftung zu Feld | 6 px |
| Felder untereinander | 16 px |
| Innenabstand von Karten | 20 px |
| Innenabstand von Dialogen | 24 px seitlich |
| Karten untereinander | 16 px |
| Seitenrand | 32 px, auf kleinen Bildschirmen 16 px |
| Abschnitte | 32 px |

| Element | Höhe |
| --- | --- |
| Button und Eingabefeld, Standard | 32 px |
| Kompakt | 28 px |
| Groß, nur für einzelne Hauptaktionen | 40 px |
| Tabellenzeile | 40 px, kompakt 32 px |
| Navigationseintrag | 36 px |
| Titelleiste | 44 px |
| Seitenleiste | 232 px breit |

Ausrichtung: Beschriftungen stehen über den Feldern und sind linksbündig. Aktionen eines Dialogs stehen rechts unten, die Hauptaktion ganz rechts. Zahlen sind rechtsbündig.

## 6. Form

| Radius | Wert | Für |
| --- | --- | --- |
| `xs` | 4 px | Checkbox, Badge, Tooltip |
| `sm` | 6 px | Buttons, Eingabefelder, Menüeinträge |
| `md` | 8 px | Menüs, Toasts, Hinweisboxen |
| `lg` | 10 px | Karten, Panels |
| `xl` | 14 px | Dialoge |
| `full` | rund | Schalter, Statuspunkte |

Rahmen sind 1 px breit. Schatten gibt es nur für schwebende Elemente (Menüs, Toasts, Dialoge) und als Hover-Rückmeldung bei Karten. Ruhende Flächen haben keinen Schatten.

## 7. Bewegung

Bewegung erklärt, was passiert: Etwas erscheint, wechselt oder reagiert. Sie soll sich flüssig und hochwertig anfühlen, nie verspielt.

| Token | Dauer | Für |
| --- | --- | --- |
| `instant` | 80 ms | Drücken |
| `fast` | 120 ms | Hover, Fokus, Checkbox, Schließen |
| `normal` | 180 ms | Tabs, Dropdowns, Statuswechsel |
| `slow` | 250 ms | Dialoge, aufklappende Bereiche, Toasts |

Bewegungswege sind klein: 2 px Anheben, 4 px Verschieben, höchstens 8 px. Elemente erscheinen mit `enter` (schneller Start, weiches Abbremsen) und verschwinden schneller mit `exit`. Reduzierte Bewegung entfernt Wege und Skalierung, Farbwechsel bleiben.

Alle Details, erlaubte Animationen pro Komponente und die Umsetzung in WinForms: [guidelines/motion.md](guidelines/motion.md).

## 8. Zustände

Jedes interaktive Element hat diese Zustände, in dieser Reihenfolge der Wichtigkeit:

| Zustand | Darstellung |
| --- | --- |
| Normal | Ruhig, ohne Akzent |
| Hover | Fläche eine Stufe heller oder Rahmen kräftiger, 120 ms |
| Gedrückt | Fläche dunkler, Button minimal kleiner (0,98), 80 ms |
| Fokus (Tastatur) | 2 px Ring in `accent.hover` mit 2 px Abstand. Nie entfernen |
| Ausgewählt | Hintergrund `accent.subtle`, Text oder Symbol in `accent.text` |
| Deaktiviert | Fläche `surface.disabled`, Text `text.disabled`, keine Hover-Reaktion |
| Fehler | Rahmen und Meldung in `status.danger`, Meldung direkt unter dem Feld |
| Laden | Spinner im Element, Text bleibt erhalten oder wird ersetzt, Element gesperrt |

## 9. Sprache

Texte sind Teil des Designs. Kurz, natürlich, vollständig lesbar. Keine Gedankenstriche, keine dekorativen Pfeile, keine Floskeln, keine abgeschnittenen Beschriftungen. Details: [guidelines/writing.md](guidelines/writing.md).

## 10. Barrierefreiheit

- Kontraste wie unter Farbe beschrieben, automatisch geprüft.
- Alles ist per Tastatur bedienbar, die Reihenfolge folgt dem Layout.
- Fokus ist immer sichtbar.
- Klickflächen mindestens 28 px hoch, in Touch-Oberflächen 40 px.
- Symbole ohne Text haben einen Tooltip und eine zugängliche Bezeichnung.
- Systemeinstellung für reduzierte Bewegung wird respektiert.
- Skalierung bis 150 Prozent ohne abgeschnittene Texte.

## 11. Komponenten

Technologieunabhängige Spezifikationen stehen in [`components/`](components/):

- [Buttons](components/buttons.md)
- [Formulare](components/forms.md): Eingabefelder, Dropdowns, Checkboxen, Schalter
- [Container](components/containers.md): Karten, Panels, Dialoge
- [Navigation](components/navigation.md): Seitenleiste, Tabs, Menüs
- [Rückmeldung](components/feedback.md): Status, Hinweise, Toasts, Laden, Fehler
- [Daten](components/data.md): Tabellen und Listen
