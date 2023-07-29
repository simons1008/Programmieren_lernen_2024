# Aufgabe der Funktion ist die Addition aller Einkäufe aus einer Liste
# und die Umrechnung der Summe in EUR (1 GBP = 1,21 EUR)

# Input der Funktion ist der Kassenzettel mit den Preisen in GBP
# Output der Funktion ist die Summe der Preise in EUR

# Funktion mit Datentyp
def summiere(kassenzettel: list[float]) -> float:
    summe = 0
    for x in kassenzettel:
        summe += x
    eur = summe * 1.21
    return eur

# Input und Output initialisieren
mein_kassenzettel = [9.0, 11.99, 12.99, 24.99]
alle_einkaeufe = 0
ohne_weste = 0

# Output erstellen
alle_einkaeufe = summiere(mein_kassenzettel)
ohne_weste = summiere(mein_kassenzettel[0:3])

# Ergebnisse drucken
print("Alle Käufe EUR: {:5.2f}".format(alle_einkaeufe))
print("Ohne Weste EUR: {:5.2f}".format(ohne_weste))
