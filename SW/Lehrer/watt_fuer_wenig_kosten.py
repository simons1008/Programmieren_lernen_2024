# monatliche Kosten für Tarif Watt für wenig berechnen (Schritt 1)

# Funktion mit Datentyp (Schritt 3 und Schritt 5)
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 8.2 + verbrauch * 0.16
    return kosten

# Ergebnisse berechnen, Liste initialisieren (Ab hier: Schritt 6)
verbrauch = range(0, 300, 50)
kosten1 = []

# Listen mit den Kosten des Tarifs erstellen
for x in verbrauch:
    kosten1.append(watt_fuer_wenig(x))

# Ergebnisse drucken
print(" Verbrauch  Watt für wenig")
for i in range(len(verbrauch)):
    print("{:10.2f} {:15.2f}".format(verbrauch[i], kosten1[i]))    

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(verbrauch, kosten1)
plt.show()
