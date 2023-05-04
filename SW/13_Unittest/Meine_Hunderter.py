# Aufgabe der Funktion ist die Berechnung der Hunderter in einer 3-stelligen Ganzzahl

# Input der Funktion ist die dreistellige Ganzzahl
# Output der Funktion ist die Anzahl der Hunderter

# Funktion mit Datentyp
def hunderter(ganzzahl: int) -> int:
    anzahl = ganzzahl // 100
    return anzahl

# Input und Output initialisieren
ganzzahlen_liste = [0, 10, 100, 109, 200, 290, 900, 999]
hunderter_liste = []

# Output erstellen
for x in ganzzahlen_liste: 
    hunderter_liste.append(hunderter(x))

# Ergebnisse drucken
print("Ganzzahl    Hunderter") 
for i in range(len(ganzzahlen_liste)):
    print("{:5d} {:5d}".format(ganzzahlen_liste[i], hunderter_liste[i]))
