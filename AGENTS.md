# Anweisungen für KI-Werkzeuge

Diese Datei richtet sich an Claude und andere KI-Entwicklungswerkzeuge, die eine Oberfläche nach dem C3yPTaX Design System gestalten oder dieses Repository bearbeiten. Die Regeln sind verbindlich.

## Lesereihenfolge

1. Diese Datei.
2. [DESIGN.md](DESIGN.md) für Haltung und Grundregeln.
3. [tokens/tokens.json](tokens/tokens.json) für alle konkreten Werte.
4. Die passende Komponentenspezifikation in [components/](components/).
5. [guidelines/platforms.md](guidelines/platforms.md) für die Umsetzung in der Zieltechnologie.
6. Bei Texten [guidelines/writing.md](guidelines/writing.md), bei Animationen [guidelines/motion.md](guidelines/motion.md), bei Logos und Icons [guidelines/branding.md](guidelines/branding.md).

Im Zweifel zeigt [examples/preview.html](examples/preview.html), wie das Ergebnis aussehen soll.

## Wenn du eine Oberfläche gestaltest

### Pflicht

- Werte ausschließlich aus den Tokens übernehmen. Keine eigenen Farben, Abstände, Radien oder Dauern erfinden. Fehlt ein Wert, den nächstliegenden Token nehmen und das im Ergebnis erwähnen.
- Token-Dateien ins Zielprojekt kopieren (`c3.css`, `c3-theme.ps1` oder Werte aus `tokens.json`) statt Hex-Werte im Code zu verstreuen.
- Dunkle, ruhige Flächen: `bg.canvas` als Fenster, `surface.card` für Karten, `surface.input` für Eingaben.
- Cyan (`accent.default`) nur für die eine Hauptaktion pro Bereich, für Fokus, Auswahl und aktive Navigation.
- Grün nur als Status (Erfolg, verbunden), nie als Dekoration.
- Jeder interaktive Zustand ist definiert: Hover, gedrückt, Fokus, deaktiviert, Laden, Fehler.
- Sichtbarer Tastaturfokus mit 2 px Ring in `border.focus`.
- Status immer mit Text oder Symbol, nie nur mit Farbe.
- Animationen nur mit den Motion-Tokens, 80 bis 250 ms, kleine Wege. Reduzierte Bewegung respektieren.
- Programmicon aus `assets/icon/c3yptax.ico` für EXE, Fenster und Taskleiste.
- Systemschriften: Segoe UI unter Windows, Font-Stack aus `font.family.ui` im Web.

### Verboten

- Neon-Flächen, Glow um Karten oder Text, dauerhaft pulsierende oder leuchtende Elemente.
- HUD-Elemente, Fadenkreuze, Schaltkreislinien, Scanlinien oder Chip-Rahmen in gewöhnlichen Oberflächen. Diese Motive gehören nur ins Logo.
- Wallpaper oder Logos als Hintergrund hinter Formularen, Tabellen oder Text.
- Farbverläufe auf Flächen und Buttons.
- Bounce, Überschwingen, große Zooms, Animationen über 250 ms (Ausnahmen: Ladeschleifen, Ausklingen neuer Tabellenzeilen).
- Animationsbibliotheken für einfache Übergänge.
- Eigenes Ordnersymbol für den Ordner `App` oder andere Ordner, keine `desktop.ini`.
- Die Schrift des Logos in der Oberfläche nachbauen.
- Webfonts nachladen.
- Großbuchstaben-Überschriften, gesperrter Text, Bold statt Semibold.
- Abgeschnittene Beschriftungen mit Auslassungspunkten (auch `TextFormatFlags.EndEllipsis` in WinForms).

## Texte

Texte in Oberflächen, Dokumentation, Commits und Pull Requests folgen [guidelines/writing.md](guidelines/writing.md). Die wichtigsten Punkte:

- Kurz, konkret, natürlich. Beschriftungen ein bis drei Wörter, Hinweise ein Satz.
- Keine Gedankenstriche als Satzzeichen (weder Halbgeviert- noch Geviertstrich). Punkt oder Komma verwenden.
- Keine dekorativen Doppel-Chevrons, doppelten Größer-als-Zeichen oder Pfeile.
- Keine drei Punkte, weder als Ladeanzeige noch zum Abkürzen.
- Keine Floskeln wie `nahtlos`, `mühelos`, `Tauche ein`, `Willkommen bei`.
- Keine wiederholten Hinweise und keine künstlichen Überschriften mit Doppelpunkt und Untertitel.
- Sonderzeichen nur mit Funktion: Bindestrich in Wörtern, Doppelpunkt, Schrägstrich in Pfaden, `+` in Tastenkürzeln.

## Datenschutz

Keine privaten Namen, Anschriften, Telefonnummern, privaten E-Mail-Adressen, Gerätekennungen, Seriennummern oder andere personenbezogenen Daten in Code, Beispiele, Screenshots oder Dokumentation aufnehmen. Beispieldaten sind erfunden und neutral (`Controller A`, `Standardprofil`).

## Marke und Produkte

- `C3yPTaX` ist die Marke, `C3-Name` ist ein Produkt. Fenstertitel zeigen den Produktnamen.
- Das Design-System bleibt produktneutral. Produktspezifische Farben, Texte oder Komponenten gehören ins jeweilige Produkt.

## Wenn du dieses Repository bearbeitest

- `assets/originals/` niemals verändern. Neue Originale hinzufügen und `SHA256SUMS` ergänzen.
- Designwerte nur in `tokens/tokens.json` ändern, danach `python scripts/build-tokens.py`. Die generierten Dateien nicht von Hand bearbeiten.
- Abgeleitete Grafiken nur über `python scripts/build-assets.py` erzeugen.
- Vor jedem Commit `python scripts/check.py` ausführen. Es muss ohne Fehler durchlaufen.
- Keine doppelte Dokumentation: Werte stehen in den Tokens, Regeln in DESIGN.md, Details in `guidelines/` und `components/`. Neue Inhalte an der passenden Stelle ergänzen statt neue Dateien anzulegen.
- Änderungen an Farben oder Kontrasten in `scripts/check.py` mit abdecken, wenn neue Farbkombinationen entstehen.

## Abnahme einer Oberfläche

Bevor du eine Oberfläche als fertig meldest:

- [ ] Alle Farben, Abstände, Radien und Dauern stammen aus den Tokens.
- [ ] Pro Bereich höchstens eine primäre Aktion.
- [ ] Hover, Fokus, deaktiviert, Laden und Fehler sind umgesetzt.
- [ ] Bedienung per Tastatur funktioniert.
- [ ] Keine abgeschnittenen Texte, auch bei 150 Prozent Skalierung.
- [ ] Texte erfüllen die Sprachregeln.
- [ ] Animationen sind kurz, weich und bei reduzierter Bewegung abgeschaltet.
- [ ] Programmicon gesetzt, kein Ordnersymbol.
- [ ] Keine personenbezogenen Daten.
