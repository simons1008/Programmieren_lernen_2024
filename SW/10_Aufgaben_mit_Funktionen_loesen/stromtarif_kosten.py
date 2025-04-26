# Programm vergleicht die Kosten von zwei Stromtarifen 

# monatliche Kosten für Tarif Watt für wenig berechnen
# Funktion mit Datentyp
def watt_fuer_wenig(verbrauch: float) -> float:
    kosten = 13.5 + verbrauch * 0.75
    return kosten

# monatliche Kosten für Tarif Billig-Strom berechnen
# Funktion mit Datentyp
def billig_strom(verbrauch: float) -> float:
    kosten = 9.2 + verbrauch * 0.81
    return kosten

# Ergebnisse berechnen
# Listen initialisieren
verbrauch = range(0, 150, 10)
kosten1 = []
kosten2 = []

# Listen mit den Kosten der beiden Tarife erstellen
for x in verbrauch:
    kosten1.append(watt_fuer_wenig(x))
    kosten2.append(billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch  Watt für wenig  Billig-Strom")
for x, y, z in zip(verbrauch, kosten1, kosten2):
    print("{:10.2f} {:15.2f} {:13.2f}".format(x, y, z))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(verbrauch, kosten1)
plt.plot(verbrauch, kosten2)
plt.show()
