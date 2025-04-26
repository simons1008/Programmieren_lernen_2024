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
verbrauch_liste = range(0, 160, 10)
kosten_liste1 = []
kosten_liste2 = []

# Listen mit den Kosten der beiden Tarife erstellen
for x in verbrauch_liste:
    kosten_liste1.append(stromtarif_kosten(15.6, 0.32, x)) # Tarif Watt für wenig
    kosten_liste2.append(stromtarif_kosten(12.8, 0.36, x)) # Tarif Billig-Strom

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
