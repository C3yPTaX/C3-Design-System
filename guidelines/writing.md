# Sprache und Texte

Texte sollen klingen, als hätte sie ein Mensch mit Sorgfalt geschrieben. Kurz, klar, freundlich und vollständig lesbar.

## Grundsätze

1. **Kurz.** Eine Beschriftung ist ein bis drei Wörter. Ein Hinweis ist ein Satz, höchstens zwei.
2. **Konkret.** Sag, was passiert ist und was man tun kann. Nicht, dass etwas passiert ist.
3. **Einmal.** Jede Information steht an genau einer Stelle. Keine Wiederholungen in Untertitel, Tooltip und Hinweis.
4. **Vollständig lesbar.** Beschriftungen werden nicht mit Auslassungspunkten abgeschnitten. Wenn der Platz nicht reicht, wird der Text kürzer oder das Layout breiter.
5. **Natürlich.** Du-Form in Produkten für Endnutzer, sachlich und ohne Ausrufezeichen.

## Zeichen

| Vermeiden | Stattdessen |
| --- | --- |
| Gedankenstriche (Halbgeviert- und Geviertstrich) als Satzzeichen | Punkt, Komma oder Doppelpunkt |
| Dekorative Doppel-Chevrons und doppelte Größer-als-Zeichen | Nichts, oder ein echtes Symbol mit Funktion |
| Pfeile als Schmuck vor Links oder Buttons | Klarer Text, gegebenenfalls ein Chevron-Symbol mit Funktion |
| Drei Punkte nach Ladetexten | `Wird geladen`, `Wird gespeichert` |
| Drei Punkte zum Abkürzen | Kürzerer Text |
| Emojis in der Oberfläche | Symbole aus dem Symbolsatz |
| Mehrere Ausrufezeichen | Kein Ausrufezeichen |

Funktionale Zeichen sind erlaubt: Bindestrich in zusammengesetzten Wörtern (`USB-Kabel`), Doppelpunkt, Schrägstrich in Pfaden, Prozentzeichen, `+` in Tastenkombinationen (`Strg+S`), ein Chevron-Symbol am Dropdown.

Ein Sonderfall sind Menüeinträge, die ein weiteres Fenster öffnen. Unter Windows ist es üblich, sie mit drei Punkten zu kennzeichnen. Wir verzichten darauf, weil der Dialog ohnehin sofort erscheint.

## Floskeln

Diese Formulierungen wirken generiert und werden gestrichen:

- `Willkommen bei`, `Entdecke`, `Tauche ein`, `nahtlos`, `mühelos`, `leistungsstark`, `revolutionär`
- `Bitte beachten Sie, dass`, `Es ist wichtig zu wissen`, `Hinweis:` vor jedem Hinweis
- `Erfolgreich erfolgreich`, also doppelte Bestätigungen in Titel und Text
- Überschriften mit Doppelpunkt und Untertitel (`Profile: Alles im Blick`)
- Aufzählungen von genau drei Adjektiven

## Muster

| Situation | Gut | Schlecht |
| --- | --- | --- |
| Button | `Speichern` | `Jetzt speichern!` |
| Hauptaktion mit Objekt | `Profil anlegen` | `Neues Profil erstellen und hinzufügen` |
| Laden | `Wird geladen` | `Lädt...` |
| Erfolg | Titel `Gespeichert`, Text `Die Einstellungen wurden übernommen.` | `Erfolg! Ihre Einstellungen wurden erfolgreich gespeichert.` |
| Fehler | `Der Ordner ist schreibgeschützt.` | `Ein unerwarteter Fehler ist aufgetreten.` |
| Fehler mit Lösung | `Controller B antwortet nicht. Prüfe das USB-Kabel.` | `Fehler 0x80004005` |
| Feldfehler | `Bitte einen Namen eingeben.` | `Ungültige Eingabe` |
| Leerer Zustand | Titel `Noch kein Verlauf`, Text `Sobald ein Profil verwendet wird, erscheinen die Sitzungen hier.` | `Hier gibt es leider noch nichts zu sehen.` |
| Bestätigung | Titel `Profil löschen?`, Button `Löschen` | Titel `Sind Sie sicher?`, Button `OK` |

## Technische Details

- Fehlercodes gehören in ein aufklappbares Detail oder ins Protokoll, nicht in die Hauptmeldung.
- Datum: `12. Nov.`, `Heute, 09:42`, `Gestern`. Uhrzeit immer zweistellig.
- Zahlen mit Einheit und schmalem Abstand: `250 ms`, `15 %` (in Fließtext `15 Prozent`).
- Dateipfade und Werte in Monospace.
