# numpy array einlesen und plotten, unterste Zeile löschen
# numpy array an Zeile mit 15 anhängen, plotten

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Input:  numpy-Datei
fp_in = 'H_0_rerechts.npy'

# Output: numpy-Datei
fp_out = 'H_0_rerechts_runter.npy'

# Datei einlesen
gray = np.load(fp_in)

# numpy Array drucken
print(repr(gray))
print("shape: ", gray.shape)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# unterste Zeile löschen
gray = np.delete(gray, 15, 0)

# numpy array an Zeile mit 15 anhängen
gray = np.append([[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]], gray, 0)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# numpy array schreiben
np.save(fp_out, gray)
