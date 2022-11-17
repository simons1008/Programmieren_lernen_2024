# Aufgabe der Funktion ist die Berechnung der Kosten von zwei Internet-Tarifen

# Input der Funktion flatrate ist die Anzahl der Monate
# Output der Funktion flatrate sind aufgelaufenen Kosten in EUR

# Funktion mit Datentyp
def flatrate(monate: int) -> float:
    kosten = monate * 8.99
    return kosten

# Input der Funktion volumentarif ist die Liste mit dem Verbrauch
# Output der Funktion volumentarif sind die aufgelaufenen Kosten in EUR

# Funktion mit Datentyp
def volumentarif(verbrauch: list[float]) -> float:
    kosten = 0
    for x in verbrauch:
        kosten += x * 6.5
    return kosten

# Input und Output initialisieren
monate = ["Mai", "Juni", "Juli"]
mein_verbrauch = [1.2, 1.5, 2]
kosten1 = []
kosten2 = []

# Output erstellen
for i in range(1,4):
    kosten1.append(flatrate(i))
    kosten2.append(volumentarif(mein_verbrauch[0:i]))


# Ergebnisse drucken
print("Bis Monat  Flatrate  Volumentarif") 
for i in range(3):
    print("{:5s} {:5.2f} {:5.2f}".format(monate[i], kosten1[i], kosten2[i]))
