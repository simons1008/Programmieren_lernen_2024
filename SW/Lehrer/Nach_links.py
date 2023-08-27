# numpy array einlesen und plotten, linke Spalte löschen
# Spaltenvektor mit 15 anhängen, plotten

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Input:  numpy-Datei
fp_in = 'H_0_lilinks.npy'

# Output: numpy-Datei
fp_out = 'H_0_lilinks_nali.npy'

# Datei einlesen
gray = np.load(fp_in)

# numpy Array drucken
print(repr(gray))
print("shape: ", gray.shape)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# linke Spalte löschen
gray = np.delete(gray, 0, 1)

# Spaltenvektor mit 15 anhängen
gray = np.append(gray, np.atleast_2d([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]).T, 1)

# Bild plotten
imgplot = plt.imshow(gray, cmap = 'gray')
plt.show()

# numpy array schreiben
np.save(fp_out, gray)
