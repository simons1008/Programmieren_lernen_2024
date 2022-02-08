# Matrix erzeugen mit numpy: nd array Objekt
# numpy arbeitet schnell und bietet viele nützliche Funktionen

# Modul für die Bearbeitung von Arrays importieren
import numpy as np

# Erzeugt ein Array mit 5 Zeilen und 8 Spalten 
# Füllt alle Elemente mit "__"
# Bestimmt den Datentyp aus dem Füllwert
Matrix = np.full((5, 8), "__")

# Drucke die Matrix
print("\nInitialisierung")
print(Matrix)

# Drucke den Datentyp
print("Datentyp", Matrix.dtype)

# Zeilen adressieren
print("\n1. Element jeder Zeile beschreiben")
Matrix[0, 0] = "A1"
Matrix[1, 0] = "A2"
Matrix[2, 0] = "A3"
Matrix[3, 0] = "A4"
Matrix[4, 0] = "A5"

# Drucke die Matrix
print(Matrix)

# Liste erneut initialisieren und drucken
Matrix = np.full((5, 8), "__")
print("\nInitialisierung")
print(Matrix)

# Spalten adressieren
print("\n1. Element jeder Spalte beschreiben")
Matrix[0, 0] = "A1"
Matrix[0, 1] = "B1"
Matrix[0, 2] = "C1"
Matrix[0, 3] = "D1"
Matrix[0, 4] = "E1"
Matrix[0, 5] = "F1"
Matrix[0, 6] = "G1"
Matrix[0, 7] = "H1"

# Drucke die Matrix
print(Matrix)

# Langen String ins letzte Element schreiben - wird abgeschnitten!
print("\nlangen String schreiben")
Matrix[4, 7] = "langer String"

# Drucke die Matrix
print(Matrix)
