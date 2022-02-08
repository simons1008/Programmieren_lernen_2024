# Zeichne ein gefülltes rechtwinkliges Dreieck

# Modul für die Turtle-Grafik importieren
import turtle

# Bildschirmobjekt erzeugen
screen = turtle.Screen()

# Turtle-Geschwindigkeit setzen
turtle.speed(1)

# Hintergrundfarbe des Bildschirms setzen
turtle.bgcolor('black')

# Stiftfarbe setzen
turtle.color('yellow')

# Strichstärke setzen
turtle.width(10)

# Gefüllte Form starten
turtle.begin_fill()

# Vorwärts 100 Schritte
turtle.forward(100)

# Rechtsherum drehen um 90 Grad
turtle.right(90)

# Vorwärts 100 Schritte
turtle.forward(100)

# Füllfarbe setzen
turtle.color('orange')

# Gefüllte Form beenden
turtle.end_fill()

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
