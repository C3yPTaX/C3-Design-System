# Tabellen und Listen

## Tabelle

| Eigenschaft | Wert |
| --- | --- |
| Kopfzeile | 36 px, `caption` in Semibold, `text.muted`, Linie darunter `border.default` |
| Zeile | 40 px, kompakt 32 px |
| Zeilenlinie | 1 px `border.subtle` |
| Text | `body`. Erste Spalte `text.primary`, weitere `text.secondary` |
| Zellabstand | 12 px seitlich, erste und letzte Spalte 16 px |
| Hover | Fläche `surface.input` mit 70 Prozent Deckkraft, `fast` |
| Ausgewählt | Fläche `accent.subtle`, erste Spalte in `accent.text` |

Regeln:

- Keine Zebrastreifen und keine senkrechten Linien.
- Text linksbündig, Zahlen rechtsbündig mit gleich breiten Ziffern.
- Status als Badge in einer eigenen Spalte.
- Zeilenaktionen rechts: höchstens eine sichtbare Aktion als kleiner Button, der Rest im Aktionsmenü. Die Aktionsspalte hat eine feste Breite, damit nichts springt.
- Spaltenköpfe sind kurz und vollständig. Lange Werte in Zellen dürfen umbrechen oder die Tabelle scrollt waagerecht. Beschriftungen werden nicht abgeschnitten.
- Über der Tabelle eine Werkzeugleiste: Suche links (240 px), Filter daneben, seltene Aktionen rechts.
- Unter der Tabelle die Anzahl der Einträge in `caption`.
- Neue Einträge erscheinen oben, blenden ein und behalten für einen Moment den Hintergrund `accent.subtle`, der dann ausklingt.
- Leere Tabelle zeigt den leeren Zustand aus [feedback.md](feedback.md), keine leere Kopfzeile.

## Liste

Für einfache Abfolgen wie Aktivität, Benachrichtigungen oder Dateien.

- Eintrag mindestens 48 px, Trennlinie `border.subtle`, letzter Eintrag ohne Linie.
- Links ein 28 px Symbol in `surface.control` (bei Status in der passenden Statusfläche), dann Text in `small`, rechts Zeit oder Wert in `caption`.
- Wichtige Begriffe im Text dürfen in Semibold und `text.primary` stehen.
- Klickbare Einträge bekommen Hover wie Tabellenzeilen und einen Radius `sm`.

## Kennzahlen

Kennzahlen stehen in Karten nebeneinander: Beschriftung `small` in `text.muted`, Wert `display`, darunter eine Zeile Kontext in `caption`. Positive Entwicklung darf in `status.success` stehen, sonst bleibt alles neutral. Keine Diagramme ohne Achsen und Beschriftung.
