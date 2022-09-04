# Funktionen zur Berechnung der Kosten von zwei Stromtarifen 

# monatliche Kosten für Tarif Watt für wenig berechnen
# Funktion mit Datentyp
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 8.2 + verbrauch * 0.16
    return kosten

# monatliche Kosten für Tarif Billig-Strom berechnen
# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 4.9 + verbrauch * 0.19
    return kosten

# Ergebnisse berechnen
# Listen initialisieren
verbrauch = range(0, 300, 50)
kosten1 = []
kosten2 = []

# Listen mit den Kosten der beiden Tarife erstellen
for x in verbrauch:
    kosten1.append(watt_fuer_wenig(x))
    kosten2.append(billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch  Watt für wenig  Billig-Strom")
for i in range(len(verbrauch)):
    print("{:10.2f} {:15.2f} {:13.2f}".format(verbrauch[i], kosten1[i], kosten2[i]))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(verbrauch, kosten1)
plt.plot(verbrauch, kosten2)
plt.show()
