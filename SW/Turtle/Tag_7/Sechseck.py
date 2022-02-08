# Zeichne ein Sechseck

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

# Sechseck
for i in range(6):
    forward(100)
    left(60)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
