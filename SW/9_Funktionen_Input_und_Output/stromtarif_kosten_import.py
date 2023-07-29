# Funktionen zur Berechnung der Kosten von zwei Stromtarifen 

# Funktionen importieren
import watt_fuer_wenig
import billig_strom 

# Ergebnisse berechnen
# Listen initialisieren
verbrauch = range(0, 150, 10)
kosten1 = []
kosten2 = []

# Listen mit den Kosten der beiden Tarife erstellen
for x in verbrauch:
    kosten1.append(watt_fuer_wenig.watt_fuer_wenig(x))
    kosten2.append(billig_strom.billig_strom(x))

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
