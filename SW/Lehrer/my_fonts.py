# Liste der Fonts auf meinem PC ausgeben

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# tkinter Font Wrapper importieren
import tkinter.font as tkFont

# Modul für den schönen Ausdruck importieren
import pprint

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Font Familien als Tupel bekommen
my_font = tkFont.families()

# Tupel der Font Familien ausdrucken
pprint.pprint(my_font)

# Fenster schließen
root.destroy()
