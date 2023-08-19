# Vergleich von zwei Geraden:
# Gerade 1: Mit der Perzeptron Lernregel und skalierten Daten berechnet
#           Gewichte mit dem Skalierungsfaktor angepasst
# Gerade 2: Mit der Perzeptron Lernregel und Original-Daten berechnet

# Bibliothek importieren
import numpy as np
import matplotlib.pyplot as plt

# x0-Koordination von zwei Punkten
x0 = np.array([1.07729281, 43.8505338])

# x1-Koordinaten mit den Gewichten von Gerade 1
w = np.array([ 0.0149354,   0.01687117, -0.79328084])
x1 = -(w[0] * x0 + w[2]) / w[1]
plt.plot(x0, x1, label='Gewichte nach Skalierung, 3 Epochen, angepasst')

# x1-Koordination mit den Gewichten von Gerade 2
w = ([   68.69092228,    57.37244752, -3146.79328084])
x1 = -(w[0] * x0 + w[2]) / w[1]
plt.plot(x0, x1, label='Gewichte nach 9000 Epochen')

# Anzeigen
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.show()
