# Abstrahierte Funktion zum Vergleich der Kosten von Stromtarifen

# monatliche Kosten für einen Stromtarif mit Grundgebühr und Verbrauchskosten berechnen
# Funktion mit Datentyp
def stromtarif_kosten(grundgebuehr: float,
                      verbrauchskosten: float,
                      verbrauch: float) -> float:
    kosten = grundgebuehr + verbrauchskosten * verbrauch
    return kosten

# Ergebnisse berechnen
# Listen initialisieren
verbrauch = range(0, 150, 10)
kosten1 = []
kosten2 = []

# Listen mit den Kosten der beiden Tarife erstellen
for x in verbrauch:
    kosten1.append(stromtarif_kosten(13.5, 0.75, x)) # Tarif Watt für wenig
    kosten2.append(stromtarif_kosten(9.2, 0.81, x)) # Tarif Billig-Strom

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
