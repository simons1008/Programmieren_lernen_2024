# numpy array einlesen und plotten, rechte Spalte löschen
# numpy array an Spaltenvektor mit 15 anhängen, plotten

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Input:  numpy-Datei
fp_in = 'U_0_rerechts.npy'

# Output: numpy-Datei
fp_out = 'U_0_rerechts_nare.npy'

# Datei einlesen
gray = np.load(fp_in)

# numpy Array drucken
print(repr(gray))
print("shape: ", gray.shape)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# rechte Spalte löschen
gray = np.delete(gray, 15, 1)

# numpy array an Spaltenvektor mit 15 anhängen
gray = np.append(np.atleast_2d([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]).T, gray, 1)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# numpy array schreiben
np.save(fp_out, gray)
