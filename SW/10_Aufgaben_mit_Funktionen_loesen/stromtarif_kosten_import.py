# Funktionen zur Berechnung der Kosten von zwei Stromtarifen 

# Funktionen importieren
import watt_fuer_wenig
import billig_strom 

# Ergebnisse berechnen
# Listen initialisieren
verbrauch_liste = range(0, 150, 10)
kosten_liste1 = []
kosten_liste2 = []

# Listen mit den Kosten der beiden Tarife erstellen
for x in verbrauch_liste:
    kosten_liste1.append(watt_fuer_wenig.watt_fuer_wenig(x))
    kosten_liste2.append(billig_strom.billig_strom(x))

# Ergebnisse drucken
print(" Verbrauch  Watt für wenig  Billig-Strom")
for x, y, z in zip(verbrauch_liste, kosten_liste1, kosten_liste2):
    print("{:10.2f} {:15.2f} {:13.2f}".format(x, y, z))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(verbrauch_liste, kosten_liste1)
plt.plot(verbrauch_liste, kosten_liste2)
plt.xlabel("Verbrauch")
plt.ylabel("monatliche Kosten")
plt.show()
