# monatliche Kosten für Tarif Watt für wenig berechnen (Schritt 1)

# Funktion mit Datentyp (Schritt 3 und Schritt 5)
def billig_strom(verbrauch: float) -> float:
    kosten = 9.2 + verbrauch * 0.81
    return kosten

# Ergebnisse berechnen, Liste initialisieren (Ab hier: Schritt 6)
verbrauch = range(0, 150, 10)
kosten1 = []

# Listen mit den Kosten des Tarifs erstellen
for x in verbrauch:
    kosten1.append(billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch  Watt für wenig")
for i in range(len(verbrauch)):
    print("{:10.2f} {:15.2f}".format(verbrauch[i], kosten1[i]))    

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(verbrauch, kosten1)
plt.show()
