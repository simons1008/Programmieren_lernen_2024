# Periodisch Smiley umschalten

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Funktion zum Umschalten
def smiley_umschalten():
    global umschalt
    # Bildausgabe erzeugen
    label = tk.Label(root, image=bild[umschalt%3])
    # Bild im Gitter platzieren
    label.grid(row = 0, column = 1)
    # Umschaltvariable um 1 erhöhen
    umschalt += 1
    # nach 1000 Millisekunden erneut die Funktion aufrufen
    root.after(1000, smiley_umschalten)
    
# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Umschaltvariable initialisieren
umschalt = 0

# Liste mit Bildern erzeugen
bild = []
bild.append(tk.PhotoImage(file="slightly_smiling_face.png"))
bild.append(tk.PhotoImage(file="neutral_face.png"))
bild.append(tk.PhotoImage(file="slightly_frowning_face.png"))

# Funktion zum ersten Mal aufrufen
smiley_umschalten()

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()


