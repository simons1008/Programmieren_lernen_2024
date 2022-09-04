# GUI über das Modul tkinter
# Demonstration von Schaltflächen  

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Funktion für Schaltfläche 1
def aktionSF1():
    # Steuervariable auslesen und neu setzen
    zaehler.set(zaehler.get() + 1)

# Funktion für Schaltfläche 2
def aktionSF2():
    # Steuervariable auslesen und neu setzen
    zaehler.set(zaehler.get() - 1)

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Textausgabe erzeugen und im Gitter platzieren
label1 = tk.Label(root, text="Hallo Welt", bg="orange", font = ("arial", 25))
label1.grid(row = 0, column = 1)

# Steuervariable erzeugen und initialisieren
zaehler = tk.IntVar()
zaehler.set(0)

# Textausgabe erzeugen und im Gitter platzieren
# Der Wert der Steuervariable wird angezeigt 
label2 = tk.Label(root, textvariable=zaehler, bg="green", font = ("arial", 25))
label2.grid(row = 2, column = 1)

# Schaltfläche erzeugen und im Gitter platzieren
schaltf1 = tk.Button(root, text="größer", font = ("arial", 25), command=aktionSF1)
schaltf1.grid(row = 1, column = 0)

# Schaltfläche erzeugen und im Gitter platzieren
schaltf2 = tk.Button(root, text="kleiner", font = ("arial", 25), command=aktionSF2)
schaltf2.grid(row = 1, column = 2)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
