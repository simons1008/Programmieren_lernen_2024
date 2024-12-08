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
monate_liste = [1, 2, 3]
verbrauch_liste = [1.2, 1.5, 2]
kosten1 = []
kosten2 = []

# Output erstellen
for i in range(len(monate_liste)):
    # Input der Funktion flatrate ist eine Zahl
    kosten1.append(flatrate(monate_liste[i]))
    # Input der Funktion volumentarif ist eine Liste 
    kosten2.append(volumentarif(verbrauch_liste[0:i+1]))

# Ergebnisse drucken
print("Flatrate \t Volumentarif") 
for i in range(len(monate_liste)):
    print(kosten1[i], "\t\t", kosten2[i])

# Bibliothek importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(monate_liste, kosten1)
plt.plot(monate_liste, kosten2)
plt.show()
