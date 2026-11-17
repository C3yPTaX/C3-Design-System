# Navigation, Tabs und Menüs

## Fensteraufbau

```
+--------------------------------------------------+
| Titelleiste 44 px   Icon  Produktname            |
+------------+-------------------------------------+
| Seiten-    | Seitentitel               Aktionen  |
| leiste     |                                     |
| 232 px     | Inhalt                              |
|            |                                     |
| Status     |                                     |
+------------+-------------------------------------+
```

Kleine Werkzeuge mit wenigen Funktionen brauchen keine Seitenleiste. Dann gliedern Tabs unter dem Seitentitel.

## Seitenleiste

| Eigenschaft | Wert |
| --- | --- |
| Breite | 232 px |
| Fläche | `bg.subtle`, rechts 1 px `border.subtle` |
| Innenabstand | 12 px |
| Eintrag | 36 px hoch, Radius `sm`, Symbol 16 px plus Text `body` |
| Abschnittstitel | `caption`, `text.muted`, normale Schreibweise |
| Normal | Text `text.secondary`, Symbol `text.muted` |
| Hover | Fläche `surface.card`, Text `text.primary` |
| Aktiv | Fläche `accent.subtle`, 3 px Leiste links in `accent.default`, Symbol `accent.text` |

Die aktive Markierung gleitet beim Wechsel zum neuen Eintrag (`normal`, `standard`). Zähler rechts im Eintrag als kleine runde Marke in `surface.control`. Unten in der Seitenleiste dürfen Verbindungsstatus und Version stehen.

Höchstens sieben Einträge pro Abschnitt. Einstellungen und Hilfe stehen unten.

## Tabs

| Eigenschaft | Wert |
| --- | --- |
| Höhe | 40 px |
| Schrift | `label` |
| Normal | `text.muted` |
| Hover | `text.primary` |
| Aktiv | `text.primary` mit 2 px Unterstrich in `accent.default` |
| Linie unter allen Tabs | 1 px `border.subtle` |

- Tabs wechseln Ansichten desselben Inhalts. Sie lösen keine Aktionen aus.
- Der Unterstrich gleitet zum neuen Tab, der neue Inhalt blendet ein und rückt 4 px hoch (`normal`).
- Tastatur: Pfeiltasten links und rechts wechseln den Tab.
- Höchstens sechs Tabs. Beschriftungen ein Wort, höchstens zwei.

## Menüs

Kontextmenüs und Aktionsmenüs (Button mit drei Punkten) teilen sich das Aussehen des Dropdowns:

- Popover mit `surface.popover`, Rahmen `border.strong`, Radius `md`, Schatten `md`, mindestens 180 px breit.
- Einträge 32 px hoch mit Symbol in `text.muted`. Tastenkürzel rechtsbündig in `caption`.
- Gruppen durch eine Trennlinie. Destruktive Einträge stehen zuletzt und sind in `status.danger`.
- Das Menü öffnet am Auslöser, bündig zur rechten Kante, und klappt nach oben, wenn unten kein Platz ist.
- Klick außerhalb, Escape oder Scrollen schließt.

Bewegung: wie Dropdown. Öffnen `normal` `enter`, Schließen `fast` `exit`.

## Titelleiste

Die native Titelleiste von Windows wird dunkel geschaltet (siehe [platforms.md](../guidelines/platforms.md)). Wenn eine eigene Titelleiste gezeichnet wird: 44 px hoch, `bg.subtle`, Icon 20 px, Produktname in `label`, Fensterknöpfe 46 px breit, Schließen beim Hover in `status.dangerSolid`.
