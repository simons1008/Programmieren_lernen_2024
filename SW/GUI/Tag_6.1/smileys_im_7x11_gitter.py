# Schreibe ein Programm mit GUI, das drei Smileys in einem Gitter
# von 7 Zeilen und 11 Spalten anzeigt. Platziere:
# - das erste Smiley in der oberen linken Ecke
# - das zweite Smiley im Zentrum
# - das dritte Smiley in der unteren rechten Ecke
# Hinweis: Die Smileys sind 72 Pixel breit und 72 Pixel hoch.  

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Bildausgabe erzeugen
bild1 = tk.PhotoImage(file="slightly_smiling_face.png")
label1 = tk.Label(root, image=bild1)

# Bildausgabe erzeugen
bild2 = tk.PhotoImage(file="neutral_face.png")
label2 = tk.Label(root, image=bild2)

# Bildausgabe erzeugen
bild3 = tk.PhotoImage(file="slightly_frowning_face.png")
label3 = tk.Label(root, image=bild3)

# Gitter konfigurieren
# 7 Zeilen, 80 Pixel hoch 
for i in range(7):
    root.rowconfigure(i, minsize=80)
# 11 Spalten, 80 Pixel breit
for i in range(11):
    root.columnconfigure(i, minsize=80)

### Platziere die Smileys
label1.grid(row=0, column=0)
label2.grid(row=3, column=5)
label3.grid(row=6, column=10)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()
