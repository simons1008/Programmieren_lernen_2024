# Drei Smileys im Gitter darstellen

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Die Darstellung besteht aus:
# - dem Bild
# - der Zeile im Gitter
# - der Spalte im Gitter

# Funktion erzeugt Bildausgabe und platziert im Gitter
def bildausgabe(bild, zeile: int, spalte:int):
    label = tk.Label(root, image=bild)
    label.grid(row=zeile, column=spalte)

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Eingangswerte für die Funktion erzeugen
bild = []
bild.append(tk.PhotoImage(file="slightly_smiling_face.png"))
bild.append(tk.PhotoImage(file="neutral_face.png"))
bild.append(tk.PhotoImage(file="slightly_frowning_face.png"))

# Bildausgaben erzeugen und im Gitter platzieren
for i in range(len(bild)):
    bildausgabe(bild[i], i, i)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
