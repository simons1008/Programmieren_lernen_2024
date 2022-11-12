# Aufgabe der Funktion ist die Addition aller Einkäufe aus einer Liste

# Input der Funktion ist der Kassenzettel mit den Preisen in GBP
# Output der Funktion ist die Summe der Preise in GBP

# Funktion mit Datentyp
def summiere(kassenzettel: list[float]) -> float:
    summe = 0
    for x in kassenzettel:
        summe += x
    return summe

# Input und Output initialisieren
mein_kassenzettel = [9.0, 11.99, 12.99, 24.99]
alle_einkaeufe = 0
ohne_weste = 0

# Output erstellen
alle_einkaeufe = summiere(mein_kassenzettel)
ohne_weste = summiere(mein_kassenzettel[0:3])

# Ergebnisse drucken
print("Alle Einkäufe") 
for i in range(len(mein_kassenzettel)):
    print("{:5.2f}".format(mein_kassenzettel[i]))
print("Summe")
print("{:5.2f}".format(alle_einkaeufe))

print("")

print("Ohne Weste") 
for i in range(len(mein_kassenzettel[0:3])):
    print("{:5.2f}".format(mein_kassenzettel[i]))
print("Summe")
print("{:5.2f}".format(ohne_weste))
