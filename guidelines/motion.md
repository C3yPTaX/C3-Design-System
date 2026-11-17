# Bewegung

Ziel: die visuelle Zurückhaltung professioneller Desktop-Software mit der flüssigen Interaktion moderner Apple-Oberflächen. Die Oberfläche fühlt sich lebendig an, ohne je hektisch oder verspielt zu wirken.

Ausprobieren: [`examples/preview.html`](../examples/preview.html), Seite Bewegung.

## Prinzipien

1. **Funktion vor Wirkung.** Jede Animation beantwortet eine Frage: Woher kommt das? Was hat sich geändert? Hat mein Klick funktioniert?
2. **Kurz.** 120 bis 250 ms. Häufige Aktionen reagieren sofort, nur ihre Rückmeldung ist animiert.
3. **Weich.** Natürliche Beschleunigung und sanftes Abbremsen. Linear nur für Fortschritt und Drehung.
4. **Klein.** Wege von 2 bis 8 px. Skalierung höchstens von 0,97 auf 1.
5. **Leise.** Kein Bounce, kein Überschwingen, kein Pulsieren, kein dauerhaftes Leuchten.
6. **Sparsam.** Es bewegt sich immer nur das, womit gerade interagiert wird.
7. **Günstig.** Nur Deckkraft, Farbe und Transformation animieren. Keine Layout-Eigenschaften wie Breite, Höhe oder Position im Fluss.

## Tokens

| Token | Wert | Zweck |
| --- | --- | --- |
| `motion.duration.instant` | 80 ms | Drücken |
| `motion.duration.fast` | 120 ms | Hover, Fokus, Checkbox, alles Schließende |
| `motion.duration.normal` | 180 ms | Tabs, Dropdowns, Schalter, Statuswechsel |
| `motion.duration.slow` | 250 ms | Dialoge, aufklappende Bereiche, Toasts |
| `motion.duration.loop` | 1400 ms | Ein Durchlauf von unbestimmtem Fortschritt und Skeleton |
| `motion.duration.spin` | 900 ms | Eine Umdrehung des Ladekreises |
| `motion.easing.standard` | `0.2, 0, 0, 1` | Zustandswechsel auf der Stelle |
| `motion.easing.enter` | `0.16, 1, 0.3, 1` | Erscheinen: schneller Start, langes weiches Auslaufen |
| `motion.easing.exit` | `0.4, 0, 1, 1` | Verschwinden: beschleunigt hinaus |
| `motion.easing.linear` | `0, 0, 1, 1` | Fortschritt, Drehung |
| `motion.distance.lift` | 2 px | Karte beim Hover |
| `motion.distance.shift` | 4 px | Menü, Panelwechsel |
| `motion.distance.enter` | 8 px | Dialog, Toast. Größter erlaubter Weg |
| `motion.scale.press` | 0,98 | Button beim Drücken |
| `motion.scale.enter` | 0,97 | Startgröße eines Dialogs |

Erscheinen dauert länger als Verschwinden. Was geht, soll nicht im Weg stehen.

## Pro Komponente

| Komponente | Animation | Dauer und Kurve |
| --- | --- | --- |
| Button | Hintergrund und Rahmen wechseln die Farbe | `fast`, `standard` |
| Button gedrückt | Skalierung auf 0,98 | `instant` |
| Hauptaktion | Beim Hover zusätzlich ein 4 px Ring in Cyan mit 14 Prozent Deckkraft | `fast` |
| Karte, interaktiv | Hebt sich 2 px, Rahmen kräftiger, leichter Schatten | `normal`, `enter` |
| Eingabefeld | Rahmenfarbe beim Hover und Fokus | `fast` |
| Checkbox | Haken zeichnet sich, Fläche färbt sich | `fast`, `enter` |
| Schalter | Knopf gleitet, Spur färbt sich | `normal`, `standard` |
| Tabs | Unterstrich gleitet zum neuen Tab, Inhalt blendet ein und rückt 4 px hoch | `normal` |
| Navigation | Markierung gleitet zum neuen Eintrag | `normal`, `standard` |
| Dropdown, Menü | Öffnen: Einblenden, 4 px Weg, Skalierung von 0,98. Schließen: schneller ausblenden | `normal` `enter`, `fast` `exit` |
| Aufklappbarer Bereich | Höhe öffnet weich, Inhalt blendet ein, Chevron dreht 180 Grad | `slow`, `standard` |
| Dialog | Abdunklung blendet ein. Dialog blendet ein, wächst von 0,97 und rückt 8 px hoch | `slow` `enter`, Schließen `fast` `exit` |
| Toast | Blendet ein und rückt 8 px hoch. Geht mit 4 px nach unten | `slow` `enter`, `fast` `exit` |
| Badge bei Statuswechsel | Farben wechseln, kurzer Einblendimpuls | `normal` und `slow` |
| Neue Tabellenzeile | Blendet ein, Hintergrund in `accent.subtle` klingt aus | 1600 ms gesamt, einmalig |
| Fortschritt bestimmt | Balken wächst gleichmäßig | `slow`, `standard` |
| Fortschritt unbestimmt | Balkenabschnitt läuft durch | `loop` |
| Tooltip | Blendet nach 400 ms Wartezeit ein | `fast` |

Nicht animiert werden: Texteingaben, Scrollen, Fenster öffnen und schließen (macht das Betriebssystem), Fehler beim Speichern (sofort zeigen), wiederholte Tastaturbedienung.

## Reduzierte Bewegung

Wenn das System reduzierte Bewegung verlangt:

- Wege werden 0 px, Skalierung bleibt 1.
- Farb- und Deckkraftwechsel bleiben, weil sie Zustände erklären und keine Bewegung erzeugen.
- Skeleton schimmert nicht, unbestimmter Fortschritt läuft nicht, sondern wird als ruhiger Balken gezeigt.
- Der Ladekreis dreht sich halb so schnell.

In CSS erledigt `tokens/c3.css` den größten Teil automatisch über `prefers-reduced-motion`. Für WinForms siehe [platforms.md](platforms.md).

## Umsetzung

**HTML und CSS:** `transition` und `@keyframes` mit den CSS-Variablen. Keine Animationsbibliotheken. Referenz: [`examples/c3-ui.css`](../examples/c3-ui.css).

**WinForms:** Nur was zuverlässig ohne Flackern läuft: Farbübergänge in eigengezeichneten Controls, gleitende Knöpfe und Markierungen, Fortschritt, Ein- und Ausblenden ganzer Fenster über `Opacity`. Keine verschobenen oder skalierten Controls. Details in [platforms.md](platforms.md).

**Andere Frameworks:** Die Tokens auf die eingebauten Mittel abbilden (WPF Storyboards, Qt `QPropertyAnimation`, SwiftUI `.animation`). Die Kurven sind kubische Bézierkurven und lassen sich überall direkt eintragen.
