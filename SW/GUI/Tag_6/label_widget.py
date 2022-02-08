# GUI über das Modul tkinter
# Demonstration des Label-Widgets 

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()
root.title("Label Widget Demo")

# Breite und Höhe des Fensters festlegen
root.geometry("320x200")

# Textausgabe erzeugen
label1 = tk.Label(root, text="Hallo Welt")

# in GUI Elemente einbetten
label1.pack(side="left")

# Bildausgabe erzeugen
bild1 = tk.PhotoImage(file="biene.png")
label2 = tk.Label(root, image=bild1)

# in GUI Elemente einbetten
label2.pack(side="right")

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()

