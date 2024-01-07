# Gezielte Adressierung im numpy Array

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np

# Erzeuge numpy Array mit 7 Zeilen und 5 Spalten
# Fülle alle Element mit weiß
matrix = np.full((7,5), 15)

# Funktion stellt die numpy-Arrays grafisch dar
def plot_image(img):
    plt.imshow(img, cmap="gray")
    plt.colorbar()
    plt.show()

# Überschrift
print("\nSchwarzer Punkt")

# Schwarzer Punkt in der Mitte
matrix[3, 2] = 0

# Lösung prüfen
plot_image(matrix)

# Weiter?
input("Weiter?")

# Überschrift
print("\nQuadrat")

# Quadrat als Rahmen
matrix[2, 1:4] = 4
matrix[3, 1] = 4
matrix[3, 3] = 4
matrix[4, 1:4] = 4

# Lösung prüfen
plot_image(matrix)

# Weiter?
input("Weiter?")

# Überschrift
print("\nNoch ein Quadrat")

# Quadrat als Rahmen
matrix[1, 0:6] = 8
matrix[2:5, 0] = 8
matrix[2:5, 4] = 8
matrix[5, 0:6] = 8

# Lösung prüfen
plot_image(matrix)

# Weiter?
input("Weiter?")
