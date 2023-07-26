# Vergleich der Muster von zwei 5x7 Matrizen

# Ziffern bestehen aus Zeilen mit dem Symbol 
# Schwarzer Kreis: U+25CF

# Definition von Mustern
eins = [
"  ●  ",
" ●●  ",
"  ●  ",
"  ●  ",
"  ●  ",
"  ●  ",
" ●●● "]

zwei = [
" ●●● ",
"●   ●",
"    ●",
" ●●● ",
"●    ",
"●    ",
"●●●●●"]

drei = [
" ●●● ",
"●   ●",
"    ●",
" ●●● ",
"    ●",
"●   ●",
" ●●● "]

# Funktion zählt die passenden Zeilen der Muster
def passende_zeilen(muster1: list[str], muster2: list[str]) -> int:
    zaehler = 0
    for i in range(7):
        if muster1[i] == muster2[i]:
            zaehler += 1
    return zaehler

# Funktion erkennt die Zahlen anhand der "minimum" passenden Zeilen im Muster
def erkannte_zahlen(muster: list[str], minimum: int) -> str:
    # Vorbelegung
    antwort = "Erkannte zahl(en):"
    erkannt = False

    # Prüfe auf bekannte Zahl
    if passende_zeilen(muster, eins) >= minimum:
        antwort += " 1"
        erkannt = True
    if passende_zeilen(muster, zwei) >= minimum:
        antwort += " 2"
        erkannt = True
    if passende_zeilen(muster, drei) >= minimum:
        antwort += " 3"
        erkannt = True

    # Wenn keine Zahl erkannt
    if erkannt == False:
        antwort += " keine"

    # gib antwort
    return antwort

# Muster zum Test der Funktion
muster = [
" ●●● ",
"●   ●",
"    ●",
" ●●● ",
"     ",
"●    ",
"●●●●●"]
