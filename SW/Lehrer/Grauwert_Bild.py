# RGB Bild einlesen und plotten, in Grauwert Bild konvertieren und plotten
# Nochmal RGB Bild einlesen, Bildpunkte reduzieren, in Grauwert Bild konvertieren
# Auflösung reduzieren, plotten, numpy Array schreiben

# Quelle: https://matplotlib.org/stable/tutorials/introductory/images.html

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Input:  Bild-Datei
fp = 'H_0_rechts.png'

# Output: numpy-Datei
fp_np = 'H_0_rechts.npy'

# Bild einlesen
img = np.asarray(Image.open(fp))

# numpy Array drucken
print(repr(img))
print("shape: ", img.shape)

# Bild plotten
imgplot = plt.imshow(img, cmap = 'gray')
plt.show()

# Nur eine Komponente von RGB verwenden 
# We currently have an RGB image.  Since R, G, and B are all similar
# (see for yourself above or in your data), we can just pick one
# channel of our data using array slicing
gray = img[:, :, 0]

# numpy Array drucken
print(repr(gray))
print("shape: ", gray.shape)

# Bild plotten [vgl. help(plt.imshow)]
# The input may either be actual RGB(A) data, or 2D scalar data, which
# will be rendered as a pseudocolor image. For displaying a grayscale
# image set up the colormapping using the parameters
# ``cmap='gray', vmin=0, vmax=255``.
plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.show()

# Histogramm plotten
# Sometimes you want to enhance the contrast in your image, or expand
# the contrast in a particular region while sacrificing the detail in
# colors that don't vary much, or don't matter.  A good tool to find
# interesting regions is the histogram.
plt.hist(gray.ravel(), bins=range(256), fc='k', ec='k')
plt.show()

# Bildpunkte reduzieren
# Let's take our image and shrink it.  We're effectively discarding pixels,
# only keeping a select few.  Now when we plot it, that data gets blown
# up to the size on your screen.  The old pixels aren't there anymore,
# and the computer has to draw in pixels to fill that space.
# We'll use the Pillow library that we used to load the image also to resize
# the image.
img = Image.open(fp)
out = img.resize((16, 16))
#img.thumbnail((16, 16))

# in numpy Array konvertieren
out = np.asarray(out)

# Nur eine Komponente von RGB verwenden
gray = out[:, :, 0]

# Auflösung reduzieren
gray = gray// 16

# numpy Array drucken
print(repr(gray))
print("shape: ", gray.shape)

# Bild plotten [vgl. help(plt.imshow)]
plt.imshow(gray, cmap='gray')
plt.colorbar()
plt.show()

# Histogramm plotten
# Sometimes you want to enhance the contrast in your image, or expand
# the contrast in a particular region while sacrificing the detail in
# colors that don't vary much, or don't matter.  A good tool to find
# interesting regions is the histogram.
plt.hist(gray.ravel(), bins=range(16), fc='k', ec='k')
plt.show()

# numpy-Datei schreiben
np.save(fp_np, gray)
