# Vier Dinosaurier im Gitter darstellen

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Die Darstellung besteht aus:
# - dem Bild
# - der Zeile im Gitter
# - der Spalte im Gitter

# Funktion erzeugt Bildausgabe und platziert im Gitter
def bildausgabe(bild, zeile: int, spalte: int):
    label = tk.Label(root, image = bild)
    label.grid(row = zeile, column = spalte)

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Image-Objekte erzeugen
bild1 = tk.PhotoImage(file="dinosaur_1.png")
bild2 = tk.PhotoImage(file="dinosaur_2.png")
bild3 = tk.PhotoImage(file="dinosaur_3.png")
bild4 = tk.PhotoImage(file="dinosaur_4.png")

# Liste mit Image-Objekten
bild = [bild1, bild2, bild3, bild4]

# Funktion im Loop aufrufen
for i in range(len(bild)):
    bildausgabe(bild[i], i, i)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
