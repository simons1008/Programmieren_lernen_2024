# Schreibe ein Programm mit GUI, das die drei Smileys (von Aufgabe 8) diagonal anzeigt.
# Die Bilderzeugung und die Platzierung des Smileys sollen in eine Funktion ausgelagert werden.
# Hinweis: Der Aufruf tk.PhotoImage() muss im Hauptprogramm stehen.

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Funktion gibt ein Bild aus
def bildausgabe(bild, zeile: int, spalte: int):
    label = tk.Label(root, image = bild)
    label.grid(row=zeile, column=spalte)

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Bild-Widgets erzeugen
bild1 = tk.PhotoImage(file="slightly_smiling_face.png")
bild2 = tk.PhotoImage(file="neutral_face.png")
bild3 = tk.PhotoImage(file="slightly_frowning_face.png")

# Bild-Widgets in Liste schreiben
bild = []
bild.append(bild1)
bild.append(bild2)
bild.append(bild3)

# Gewünschte Zeile und Spalte in Liste schreiben
zeile = [0, 1, 2]
spalte = [0, 1, 2]

# Bildausgabe erzeugen und im Gitter platzieren
for i in range(3):
    bildausgabe(bild[i], zeile[i], spalte[i])

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
