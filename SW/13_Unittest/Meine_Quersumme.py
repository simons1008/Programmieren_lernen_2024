# Aufgabe der Funktion ist die Berechnung der Quersumme einer 3-stelligen Ganzzahl

# Input der Funktion ist die dreistellige Ganzzahl
# Output der Funktion ist die Quersumme der Ganzzahl

# Funktion mit Datentyp
def quersumme(ganzzahl: int) -> int:
    anzahl_h = ganzzahl // 100
    rest_h = ganzzahl % 100

    anzahl_z = rest_h // 10
    rest_z = rest_h % 10

    anzahl_e = rest_z
    quersumme = anzahl_h + anzahl_z + anzahl_e
    return quersumme

# Input und Output initialisieren
ganzzahlen_liste = [0, 10, 100, 109, 200, 290, 900, 999]
quersummen_liste = []

# Output erstellen 
for x in ganzzahlen_liste: 
    quersummen_liste.append(quersumme(x))

# Ergebnisse drucken
print("Ganzzahl Quersumme") 
for i in range(len(ganzzahlen_liste)):
    print("{:5d}  {:5d}".format(ganzzahlen_liste[i], quersummen_liste[i]))
