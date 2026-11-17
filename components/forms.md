# Formulare

## Aufbau eines Feldes

```
Beschriftung            label, text.secondary
[ Eingabefeld        ]  32 px hoch
Hilfetext oder Fehler   caption
```

- Beschriftung immer über dem Feld, linksbündig, 6 px Abstand.
- Felder untereinander mit 16 px Abstand. Zusammengehörige Gruppen mit 24 px und optional einer Überschrift `heading`.
- Platzhaltertext ist ein Beispiel, keine Beschriftung (`Zum Beispiel Turnier`).
- Pflichtfelder werden nicht markiert, optionale Felder bekommen den Zusatz `optional` in der Beschriftung.

## Eingabefeld

| Eigenschaft | Wert |
| --- | --- |
| Höhe | 32 px (`size.control.md`) |
| Fläche | `surface.input` |
| Rahmen | 1 px `border.control` |
| Radius | `sm` |
| Text | `body`, `text.primary` |
| Platzhalter | `text.muted` |
| Innenabstand | 12 px, mit Symbol links 34 px |

| Zustand | Darstellung |
| --- | --- |
| Hover | Rahmen `text.disabled` |
| Fokus | Rahmen `accent.default` plus 1 px innerer Ring in derselben Farbe |
| Fehler | Rahmen `status.danger`, Meldung mit Fehlersymbol darunter |
| Deaktiviert | Fläche `surface.disabled`, Rahmen `border.subtle`, Text `text.disabled` |
| Nur lesen | Wie normal, aber ohne Rahmen. Text bleibt kopierbar |

Validierung erst beim Verlassen des Feldes oder beim Absenden, nicht bei jedem Tastendruck. Sobald der Fehler behoben ist, verschwindet die Meldung sofort.

## Dropdown

- Gleiche Maße wie das Eingabefeld, rechts ein Chevron in `text.muted`.
- Die Liste ist ein Popover: Fläche `surface.popover`, Rahmen `border.strong`, Radius `md`, Schatten `md`, 4 px Innenabstand, 4 px unter dem Feld.
- Einträge 32 px hoch, Radius `xs`, Hover `surface.controlHover`, gewählter Eintrag in `accent.text`.
- Tastatur: Pfeiltasten wechseln, Enter wählt, Escape schließt und gibt den Fokus zurück.
- Bewegung: Öffnen `normal` mit `enter`, 4 px Weg und Skalierung von 0,98. Schließen `fast` mit `exit`. Chevron dreht 180 Grad.
- Ab etwa zehn Einträgen bekommt die Liste ein Suchfeld.

## Checkbox und Radio

| Eigenschaft | Wert |
| --- | --- |
| Größe | 16 x 16 px |
| Radius | `xs`, Radio rund |
| Rahmen | `border.control` |
| Aktiv | Fläche `accent.default`, Haken in `text.onAccent` |
| Abstand zur Beschriftung | 8 px |

Die Beschriftung ist klickbar. Der Haken zeichnet sich in `fast` mit `enter`. Checkboxen für unabhängige Optionen, Radios für genau eine Wahl aus wenigen sichtbaren Optionen.

## Schalter

- 34 x 20 px, rund. Spur `surface.controlHover`, aktiv `accent.default`. Knopf 14 px, aktiv in `text.onAccent`.
- Für Einstellungen, die sofort wirken. Wenn erst gespeichert werden muss, ist eine Checkbox richtig.
- Beschriftung rechts vom Schalter beschreibt den eingeschalteten Zustand.
- Bewegung: Knopf gleitet in `normal` mit `standard`.

## Segmentierte Auswahl

Für zwei bis vier gleichwertige Ansichten oder Zeiträume. Fläche `surface.input`, aktives Segment `surface.controlHover`, die Markierung gleitet in `normal`.
