# Zeichne ein Quadrat

# Modul für die Turtle-Grafik importieren
from turtle import *

# Bildschirmobjekt erzeugen
screen = Screen()

# Turtle Geschwindigkeit: langsamste
speed(1)

# Strichstärke setzen
width(3)

# Stiftfarbe setzen
color("green")

# Quadrat
for i in range(4):
    forward(100)
    left(90)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()


