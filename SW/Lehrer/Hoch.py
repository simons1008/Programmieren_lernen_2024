# numpy array einlesen und plotten, oberste Zeile löschen
# Zeile mit 15 anhängen, plotten

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Input:  numpy-Datei
fp_in = 'U_0_rerechts.npy'

# Output: numpy-Datei
fp_out = 'U_0_rerechts_hoch.npy'

# Datei einlesen
gray = np.load(fp_in)

# numpy Array drucken
print(repr(gray))
print("shape: ", gray.shape)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# oberste Zeile löschen
gray = np.delete(gray, 0, 0)

# Zeile mit 15 anhängen
gray = np.append(gray, [[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]], 0)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# numpy array schreiben
np.save(fp_out, gray)
