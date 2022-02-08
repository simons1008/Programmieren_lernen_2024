# Kurzbeschreibung: Den Ladezustand des Akkus eines Elektroautos bestimmen

# Datenanalyse: Der Ladezustand wird aus folgenden Werten berechnet:
# - alter Ladezustand
# - Dauer
# - Änderung
# Alle Werte werden als Ganzzahlen angegeben

# Funktion definieren: Name - Eingabewert - Rückgabewert
def ladezustand(alter_ladezustand: int, dauer: int, aenderung: int) -> int:
    # Rumpf
    # Berechnung
    neuer_ladezustand = alter_ladezustand + dauer * aenderung
    return neuer_ladezustand

# Aus der Tabelle
dauer = [2, 13, 5, 16, 2, 1]

# Zeitachse
# Beginn der ersten Fahrt
zeit = [0]
for i in range(len(dauer)):
    zeit.append(zeit[i] + dauer[i])

# Aus der Tabelle
aenderung = [-33, 5, -18, 5, -33, 40]

# Ladezustands-Achse
# Ladezustand zu Beginn der ersten Fahrt
ladung = [100]
for i in range(len(dauer)):
    ladung.append(ladezustand(ladung[i], dauer[i], aenderung[i]))

# Modul für das Plotten von Graphen importieren
import matplotlib.pyplot as plt

# Ergebnisse plotten
plt.plot(zeit, ladung)
plt.show()
