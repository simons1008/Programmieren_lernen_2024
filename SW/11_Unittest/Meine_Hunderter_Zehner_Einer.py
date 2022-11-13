# Aufgabe der Funktion ist die Berechnung der Hunderter, Zehner, Einer
# in einer 3-stelligen Ganzzahl

# Input der Funktion ist die dreistellige Ganzzahl
# Output der Funktion ist die Liste mit der Anzahl der Hunderter, Zehner, Einer

# Funktion mit Datentyp
def hunderter_zehner_einer(ganzzahl: int) -> list[int]:
    anzahl_h = ganzzahl // 100
    rest_h = ganzzahl % 100

    anzahl_z = rest_h // 10
    rest_z = rest_h % 10

    anzahl_e = rest_z
    anzahl_liste = [anzahl_h, anzahl_z, anzahl_e]
    return anzahl_liste

# Input und Output initialisieren
ganzzahlen_liste = [0, 10, 100, 109, 200, 290, 900, 999]
hze_liste = []

# Output erstellen 
for x in ganzzahlen_liste: 
    hze_liste.append(hunderter_zehner_einer(x))

# Ergebnisse drucken (ohne Formatierung)
print("Ganzzahl Hunderter Zehner Einer")
for i in range(len(ganzzahlen_liste)):
    print(ganzzahlen_liste[i], end = ' ')
    print(hze_liste[i])

### Ergebnisse drucken (mit Formatierung)
##print("Ganzzahl Hunderter Zehner Einer") 
##for i in range(len(ganzzahlen_liste)):
##    print("{:5d}  {:5d}   {:5d}   {:5d}".format(ganzzahlen_liste[i],
##                                              hze_liste[i][0],
##                                              hze_liste[i][1],
##                                              hze_liste[i][2]))
