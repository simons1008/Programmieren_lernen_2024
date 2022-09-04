# Zeichne Strahlen

# Importiere alle Methoden des Moduls turtle
from turtle import *

# Bildschirmobjekt erzeugen
screen = Screen()

# Strichstärke setzen
width(3)

# Anzahl der Strahlen
n = 10

# Länge des ersten Strahls
erste_laenge = 10

# Länge des Strahls initialisieren
laenge = erste_laenge

# Strahlen mit wachsender Länge zeichnen
for i in range(n):
    forward(laenge)
    backward(laenge)
    left(360/n)
    laenge += erste_laenge

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
