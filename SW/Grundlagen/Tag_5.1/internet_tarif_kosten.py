# Funktionen zur Berechnung der Kosten von zwei Internet-Tarifen

# Funktionen importieren
import flatrate as flat
import volumentarif as vol

# Ergebnisse berechnen
# Listen initialisieren
kosten1 = []
kosten2 = []

# Kosten beim Flatrate-Tarif (Mai, Juni, Juli)
for x in range(1,4):
    kosten1.append(flat.flatrate(x))

# Verbrauch beim Volunmentarif (Mai, Juni, Juli)
verbrauch = [1.2, 1.5, 2]

# Kosten beim Volumen-Tarif
kosten2.append(vol.volumentarif(verbrauch[0:1]))
kosten2.append(vol.volumentarif(verbrauch[0:2]))
kosten2.append(vol.volumentarif(verbrauch))

# Liste der Monate
monat = ["Mai ", "Juni", "Juli"]

# Ergebnisse drucken
print(" Bis Monat  Flatrate-Tarif   Volumentarif")
for i in range(3):
    print("{:>10s} {:15.2f} {:14.2f}".format(monat[i], kosten1[i], kosten2[i]))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(monat, kosten1)
plt.plot(monat, kosten2)
plt.show()
