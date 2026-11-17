# Buttons

## Varianten

| Variante | Fläche | Text | Einsatz |
| --- | --- | --- | --- |
| Primär | `accent.default` | `text.onAccent` | Die eine Hauptaktion eines Bereichs: Speichern, Anlegen, Starten |
| Sekundär | `surface.control` | `text.primary` | Alle anderen Aktionen: Abbrechen, Exportieren |
| Ghost | transparent | `text.secondary` | Werkzeugleisten, Tabellenzeilen, Schließen-Symbol |
| Destruktiv | `status.dangerSolid` | Weiß | Endgültiges Löschen, meist im Bestätigungsdialog |

## Maße

| Größe | Höhe | Innenabstand seitlich | Einsatz |
| --- | --- | --- | --- |
| Klein | 28 px | 12 px | Tabellenzeilen, Werkzeugleisten, Karten |
| Standard | 32 px | 16 px | Überall sonst |
| Groß | 40 px | 20 px | Einzelne Hauptaktion auf leeren Seiten oder im Startbildschirm |

Symbol-Buttons sind quadratisch (28 oder 32 px) mit 16 px Symbol. Radius `sm`, Schrift `label`, Abstand Symbol zu Text 8 px.

## Zustände

| Zustand | Primär | Sekundär | Ghost |
| --- | --- | --- | --- |
| Hover | `accent.hover` plus 4 px Ring mit 14 Prozent Cyan | `surface.controlHover` | Fläche `surface.control`, Text `text.primary` |
| Gedrückt | `accent.pressed`, Skalierung 0,98 | `surface.controlPressed`, 0,98 | wie Hover, 0,98 |
| Fokus | 2 px Ring `border.focus`, 2 px Abstand | gleich | gleich |
| Deaktiviert | `surface.disabled`, Text `text.disabled` | gleich | gleich |
| Laden | Spinner links, Text wird zur Verlaufsform (`Wird gespeichert`), gesperrt | gleich | gleich |

Der destruktive Button wird beim Hover dunkler statt heller, damit der weiße Text lesbar bleibt.

## Regeln

- Höchstens ein primärer Button pro Bereich. In Dialogen steht er rechts außen.
- Beschriftung ist ein Verb, gegebenenfalls mit Objekt: `Speichern`, `Profil anlegen`. Nie `OK` oder `Ja`.
- Symbole nur, wenn sie die Bedeutung schneller machen (Plus, Download). Nicht jeder Button braucht eines.
- Symbol-Buttons ohne Text haben immer einen Tooltip und eine zugängliche Bezeichnung.
- Buttons werden nicht abgeschnitten. Wenn der Text nicht passt, wird er kürzer.
- Deaktivierte Buttons erklären sich durch den Kontext. Wenn nicht klar ist, warum, lieber aktiv lassen und beim Klick erklären.

## Bewegung

Farbwechsel `fast` mit `standard`, Drücken `instant`. Kein Hover-Anheben bei Buttons.
