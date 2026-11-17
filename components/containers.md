# Karten, Panels und Dialoge

## Karte

| Eigenschaft | Wert |
| --- | --- |
| Fläche | `surface.card` |
| Rahmen | 1 px `border.subtle` |
| Radius | `lg` |
| Innenabstand | 20 px |
| Abstand zwischen Karten | 16 px |
| Schatten | keiner |

Kopfzeile: Titel `heading` links, optionale Aktion (Ghost-Button klein) rechts, 16 px Abstand zum Inhalt. Untertitel in `small` und `text.muted` direkt unter dem Titel.

**Interaktive Karte** (die ganze Karte ist klickbar): Beim Hover hebt sie sich um 2 px, der Rahmen wird `border.strong`, Schatten `sm`. Dauer `normal` mit `enter`. Nicht klickbare Karten reagieren nicht auf Hover.

Karten werden nicht verschachtelt. Innerhalb einer Karte gliedern Trennlinien (`border.subtle`) oder Abstände.

## Panel

Ein Panel ist ein fester Bereich des Fensters wie Seitenleiste, Eigenschaftenleiste oder Statusleiste. Fläche `bg.subtle`, abgegrenzt durch eine 1 px Linie in `border.subtle`, ohne Radius.

## Dialog

| Eigenschaft | Wert |
| --- | --- |
| Breite | 400 bis 560 px, Standard 460 px |
| Fläche | `surface.card` |
| Rahmen | 1 px `border.default` |
| Radius | `xl` |
| Schatten | `lg` |
| Abdunklung | `bg.overlay` |
| Kopf | Titel `heading`, optional Untertitel `small`. Schließen-Symbol rechts oben |
| Inhalt | 20 px oben und unten, 24 px seitlich, Felder mit 16 px Abstand |
| Fuß | Trennlinie oben, Buttons rechtsbündig mit 8 px Abstand, Hauptaktion ganz rechts |

Verhalten:

- Fokus springt beim Öffnen in das erste Feld oder auf die sichere Aktion. Tab bleibt im Dialog. Beim Schließen kehrt der Fokus zum Auslöser zurück.
- Escape und Klick auf die Abdunklung schließen, außer bei ungespeicherten Eingaben.
- Bestätigungsdialoge für destruktive Aktionen: Titel als Frage (`Profil löschen?`), ein Satz zu den Folgen, Buttons `Abbrechen` und die konkrete Aktion (`Löschen`) als destruktiver Button.
- Keine Dialoge für reine Erfolgsmeldungen. Dafür gibt es Toasts.

Bewegung: Abdunklung blendet in `slow` ein. Der Dialog blendet gleichzeitig ein, wächst von 0,97 auf 1 und rückt 8 px nach oben, `slow` mit `enter`. Schließen in `fast` mit `exit`. In WinForms nur über `Form.Opacity`.
