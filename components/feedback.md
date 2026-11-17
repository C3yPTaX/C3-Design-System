# Status, Hinweise, Laden und Fehler

## Statusfarben

| Status | Text und Symbol | Fläche | Rahmen |
| --- | --- | --- | --- |
| Erfolg | `status.success` | `status.successSubtle` | `status.successBorder` |
| Warnung | `status.warning` | `status.warningSubtle` | `status.warningBorder` |
| Fehler | `status.danger` | `status.dangerSubtle` | `status.dangerBorder` |
| Info | `accent.text` | `status.infoSubtle` | `status.infoBorder` |
| Neutral | `text.secondary` | `surface.control` | `border.default` |

Status wird immer mit Text oder Symbol gezeigt, nie nur über Farbe.

## Badge

22 px hoch, Radius `xs`, `caption` in Semibold, 6 px Statuspunkt vor dem Text. Für Zustände in Tabellen und Karten: `Verbunden`, `Entwurf`, `Update verfügbar`. Beim Statuswechsel gehen die Farben in `normal` über, dazu ein kurzer Einblendimpuls in `slow`.

## Hinweisbox

Für Informationen, die zu einem Bereich gehören und stehen bleiben. Radius `md`, 12 px oben und unten, 16 px seitlich, Symbol links, Titel in `label`, Text in `small` und `text.secondary`.

Eine Hinweisbox pro Bereich. Wenn mehrere nötig scheinen, stimmt meist die Struktur nicht.

## Toast

Für kurze Rückmeldungen auf eine Aktion, die nicht im Blickfeld liegt.

| Eigenschaft | Wert |
| --- | --- |
| Position | Unten rechts, 20 px Abstand zum Fensterrand |
| Breite | 360 px |
| Fläche | `surface.popover`, Rahmen `border.strong`, Radius `md`, Schatten `md` |
| Inhalt | Statussymbol, Titel `label`, ein Satz `small`, Schließen-Symbol |
| Dauer | 5 Sekunden, Fehler bleiben bis zum Schließen |
| Anzahl | Höchstens drei gleichzeitig, der älteste geht zuerst |

Bewegung: erscheint mit 8 px Weg nach oben in `slow` `enter`, geht in `fast` `exit`.

Keine Toasts für Fehler, die eine Entscheidung brauchen. Dafür ist ein Dialog oder eine Meldung am Ort des Problems richtig.

## Laden

| Situation | Darstellung |
| --- | --- |
| Unter 300 ms | Nichts anzeigen |
| Aktion auf einem Button | Spinner im Button, Text in Verlaufsform, Button gesperrt |
| Bereich lädt Inhalt | Skeleton in der Form des späteren Inhalts |
| Dauer bekannt | Fortschrittsbalken 4 px mit Prozentangabe |
| Dauer unbekannt | Unbestimmter Balken oder Spinner mit kurzem Text (`Geräte werden gesucht`) |

- Spinner 16 px, 2 px Linie, eine Umdrehung in `spin`, linear.
- Fortschrittsbalken: Spur `surface.controlHover`, Balken `accent.default`, rund.
- Skeleton: Flächen in `surface.input`, sanftes Schimmern über `loop`. Inhalt blendet danach in `normal` ein.
- Bei reduzierter Bewegung schimmert nichts und der unbestimmte Balken steht still.

## Leerer Zustand

Zentriert im Bereich: Symbol in einer 40 px Fläche, Titel `heading`, ein Satz in `small` und `text.muted`, optional eine Aktion. Der Text sagt, wann sich der Bereich füllt oder was man tun kann.

## Fehlerzustand

Wie der leere Zustand, Symbolfläche in `status.dangerSubtle`. Der Text nennt die Ursache, wenn bekannt, und was mit den Daten passiert. Aktion `Erneut versuchen`. Technische Details gehören ins Protokoll oder in einen aufklappbaren Bereich.

## Feldfehler

Direkt unter dem Feld, `caption` in `status.danger` mit Fehlersymbol. Siehe [forms.md](forms.md).
