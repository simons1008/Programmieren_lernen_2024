# Vergleich der Muster von zwei 5x7 Matrizen

# Ziffern bestehen aus Zeilen mit dem Symbol 
# Schwarzer Kreis: U+25CF

# Definition von Mustern
null = [
" ●●● ",
"●   ●",
"●   ●",
"●   ●",
"●   ●",
"●   ●",
" ●●● "]

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

vier = [
"   ● ",
"  ●● ",
" ● ● ",
"●  ● ",
"●●●●●",
"   ● ",
"   ● "]

fuenf = [
"●●●●●",
"●    ",
"●●●● ",
"    ●",
"    ●",
"●   ●",
" ●●● "]

sechs = [
" ●●● ",
"●    ",
"●    ",
"●●●● ",
"●   ●",
"●   ●",
" ●●● "]

sieben = [
"●●●●●",
"    ●",
"   ● ",
"  ●  ",
"  ●  ",
"  ●  ",
"  ●  "]

acht = [
" ●●● ",
"●   ●",
"●   ●",
" ●●● ",
"●   ●",
"●   ●",
" ●●● "]

neun = [
" ●●● ",
"●   ●",
"●   ●",
" ●●●●",
"    ●",
"    ●",
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
    antwort = "Erkannte zahl(en): "
    erkannt = False

    # Prüfe auf bekannte Zahl
    if passende_zeilen(muster, null) >= minimum:
        antwort += "0 "
        erkannt = True
    if passende_zeilen(muster, eins) >= minimum:
        antwort += "1 "
        erkannt = True
    if passende_zeilen(muster, zwei) >= minimum:
        antwort += "2 "
        erkannt = True
    if passende_zeilen(muster, drei) >= minimum:
        antwort += "3 "
        erkannt = True
    if passende_zeilen(muster, vier) >= minimum:
        antwort += "4 "
        erkannt = True
    if passende_zeilen(muster, fuenf) >= minimum:
        antwort += "5 "
        erkannt = True
    if passende_zeilen(muster, sechs) >= minimum:
        antwort += "6 "
        erkannt = True
    if passende_zeilen(muster, sieben) >= minimum:
        antwort += "7 "
        erkannt = True
    if passende_zeilen(muster, acht) >= minimum:
        antwort += "8 "
        erkannt = True
    if passende_zeilen(muster, neun) >= minimum:
        antwort += "9 "
        erkannt = True

    # Wenn keine Zahl erkannt
    if erkannt == False:
        antwort += "keine "

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

# Funktion aufrufen
antwort = erkannte_zahlen(muster, 1)
print(antwort)

# Antwort aufspalten
bestandteile = antwort.split()
print(bestandteile)

# Erkannte Zahlen als Integer drucken
i = 2
if bestandteile[i] != "keine":
    while i < len(bestandteile):
        print("zahl =", int(bestandteile[i]))
        i += 1
