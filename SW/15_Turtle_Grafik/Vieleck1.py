# Zeichne ein regelmäßiges Vieleck

# Für ein Vieleck mit n Ecken dreht sich Turtle n-mal um den Winkel 360/n nach links
def vieleck(n: int):
    # Winkel berechnen
    winkel = 360/n
    # Winkel angeben
    write(winkel)
    # Vieleck zeichnen
    for i in range(n):
        forward(100)
        left(winkel)

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

# Anzahl der Ecken abfragen
n = screen.numinput("numinput", "Bitte Anzahl der Ecken eingeben:", minval=1, maxval=10)

# In Integer umwandeln
n = int(n)

# Vieleck zeichnen
vieleck(n)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
