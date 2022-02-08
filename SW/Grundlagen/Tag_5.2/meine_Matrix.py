# Matrix erzeugen: Liste von Listen

# Modul für den schönen Ausdruck (pretty print) importieren
import pprint

# Erzeugt eine Liste, die 5 Listen mit je 8 Elementen enthält
# Füllt alle Elemente mit "__"
breite = 8  # Buchstaben A bis H
hoehe = 5   # Zahlen     1 bis 5
Matrix = [["__" for x in range(breite)] for y in range(hoehe)]

# Drucke die Matrix
print("\nInitialisierung")
pprint.pprint(Matrix)

# Zeilen adressieren
print("\n1. Element jeder Zeile beschreiben")
Matrix[0][0] = "A1"
Matrix[1][0] = "A2"
Matrix[2][0] = "A3"
Matrix[3][0] = "A4"
Matrix[4][0] = "A5"

# Drucke die Matrix
pprint.pprint(Matrix)

# Liste erneut initialisieren und drucken
Matrix = [["__" for x in range(breite)] for y in range(hoehe)]
print("\nInitialisierung")
pprint.pprint(Matrix)

# Spalten adressieren
print("\n1. Element jeder Spalte beschreiben")
Matrix[0][0] = "A1"
Matrix[0][1] = "B1"
Matrix[0][2] = "C1"
Matrix[0][3] = "D1"
Matrix[0][4] = "E1"
Matrix[0][5] = "F1"
Matrix[0][6] = "G1"
Matrix[0][7] = "H1"

# Drucke die Matrix
pprint.pprint(Matrix)

# Langen String ins letzte Element schreiben - bleibt erhalten!
print("\nLangen String schreiben")
Matrix[4][7] = "langer String"

# Drucke die Matrix
pprint.pprint(Matrix)
