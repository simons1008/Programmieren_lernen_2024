# Zweidimensionale numpy-Arrays grafisch darstellen

# Bibliotheken importieren
import matplotlib.pyplot as plt
import numpy as np

# zweidimensionale Arrays mit Grauwerten anlegen
# Grauwert 15 -> weiß, 0 -> schwarz
eins = np.array([[15, 15,  0, 15, 15],
                 [15,  0,  0, 15, 15],
                 [15, 15,  0, 15, 15],
                 [15, 15,  0, 15, 15],
                 [15, 15,  0, 15, 15],
                 [15, 15,  0, 15, 15],
                 [15,  0,  0,  0, 15]])

zwei = np.array([[15,  0,  0,  0, 15],
                 [ 0, 15, 15, 15,  0],
                 [15, 15, 15, 15,  0],
                 [15,  0,  0,  0, 15],
                 [ 0, 15, 15, 15, 15],
                 [ 0, 15, 15, 15, 15],
                 [ 0,  0,  0,  0,  0]])

drei = np.array([[15,  0,  0,  0, 15],
                 [ 0, 15, 15, 15,  0],
                 [15, 15, 15, 15,  0],
                 [15,  0,  0,  0, 15],
                 [15, 15, 15, 15,  0],
                 [ 0, 15, 15, 15,  0],
                 [15,  0,  0,  0, 15]])

# Funktion stellt die numpy-Arrays grafisch dar
def plot_image(img):
    plt.imshow(img, cmap="gray")
    plt.colorbar()
    plt.show()

# Überschrift
print("\nZahlen in Schwarzweiß")

# Plot-Funktion für jedes Array aufrufen
plot_image(eins)
plot_image(zwei)
plot_image(drei)

# Weiter?
input("Weiter?")

# Überschrift
print("\nZahlen mit Grauwerten")
            
# Zahl Eins mit einem hellen senkrechten Strich
eins[:, 2] = 6

# Zahl Zwei mit einem hellen waagerechten Fuß
zwei[6, :] = 9

# Zahl Drei mit einem hellen waagerechten Mittelstrich
drei[3, 1:4] = 12

# Plot-Funktion für jedes Array aufrufen
plot_image(eins)
plot_image(zwei)
plot_image(drei)

# Weiter?
input("Weiter?")

# Überschrift
print("\nZahlen mit Farbverläufen")

# Zahl Eins mit einem senkrechten Farbverlauf
eins[:, 2] = np.linspace(4, 12, 7)
print("Zahl Eins mit Farbverlauf")
print(eins)

# Zahl Zwei mit einem waagerechten Farbverlauf
zwei[6, :] = np.linspace(4, 12, 5)
print("Zahl Zwei mit Farbverlauf")
print(zwei)

# Zahl Drei mit einem waagerechten Farbverlauf 
drei[3, 1:4] = np.linspace(4, 12, 3)
print("Zahl Drei  mit Farbverlauf")
print(drei)

# Plot-Funktion für jedes Array aufrufen
plot_image(eins)
plot_image(zwei)
plot_image(drei)

# Weiter?
input("Weiter?")

# Überschrift
print("\nZahlen mit Fehlern")

# In jede Zahl einen Fehler einbauen
eins[3,0] = 0
zwei[4,4] = 4
drei[1,2] = 8

# Plot-Funktion für jedes Array aufrufen
plot_image(eins)
plot_image(zwei)
plot_image(drei)

# Weiter?
input("Weiter?")
