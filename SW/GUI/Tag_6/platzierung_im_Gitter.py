# GUI über das Modul tkinter
# Platzierung der Elemente über grid() 

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Textausgabe erzeugen
label1 = tk.Label(root, text="Hallo Welt", bg="orange", font = ("Arial", "24"))

# im Gitter platzieren
label1.grid(row=0, column=0)

# Textausgabe erzeugen
label2 = tk.Label(root, text="R1 / C1", bg="lightgreen", font = ("Arial", "24"))

# im Gitter platzieren
label2.grid(row=1, column=1)

# Textausgabe erzeugen
label3 = tk.Label(root, text="R2 / C2", bg="lightblue", font = ("Arial", "24"))

# im Gitter platzieren
label3.grid(row=2, column=2)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()

