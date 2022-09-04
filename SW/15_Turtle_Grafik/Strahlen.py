# Zeichne Strahlen

# Importiere alle Methoden des Moduls turtle
from turtle import *

# Bildschirmobjekt erzeugen
screen = Screen()

# Strichstärke setzen
width(3)

# Strahlen zeichnen
for i in range(10):
    forward(150)
    backward(150)
    left(10)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()

