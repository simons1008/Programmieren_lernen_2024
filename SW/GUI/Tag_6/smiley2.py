# Drei Smileys nebeneinander darstellen

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Bildausgabe erzeugen
bild1 = tk.PhotoImage(file="slightly_smiling_face.png")
label1 = tk.Label(root, image=bild1)

# im Gitter platzieren
label1.grid(row=0, column=0)

# Bildausgabe erzeugen
bild2 = tk.PhotoImage(file="neutral_face.png")
label2 = tk.Label(root, image=bild2)

# im Gitter platzieren
label2.grid(row=0, column=1)

# Bildausgabe erzeugen
bild3 = tk.PhotoImage(file="slightly_frowning_face.png")
label3 = tk.Label(root, image=bild3)

# im Gitter platzieren
label3.grid(row=0, column=2)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
