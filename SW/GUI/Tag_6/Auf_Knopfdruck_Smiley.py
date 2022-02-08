# Auf Knopfdruck: Smiley

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Funktion für Schaltfläche 1
def aktionSF1():
    global umschalt
    # Bildausgabe erzeugen
    label = tk.Label(root, image=bild[umschalt%3])
    # Bild im Gitter platzieren
    label.grid(row = 0, column = 1)
    # Umschaltvariable um 1 erhöhen
    umschalt += 1
    
# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Schaltfläche erzeugen und im Gitter platzieren
schaltf1 = tk.Button(root, text="Zeige dich", font = ("arial", 25), command=aktionSF1)
schaltf1.grid(row = 0, column = 0)

# Umschaltvariable initialisieren
umschalt = 0

# Liste mit Bildern erzeugen
bild = []
bild.append(tk.PhotoImage(file="slightly_smiling_face.png"))
bild.append(tk.PhotoImage(file="neutral_face.png"))
bild.append(tk.PhotoImage(file="slightly_frowning_face.png"))

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()


