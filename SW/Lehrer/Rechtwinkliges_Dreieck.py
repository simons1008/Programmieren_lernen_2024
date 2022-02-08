# Rechtwinkliges Dreieck zeichnen

# Modul für die Turtle-Grafik importieren
import turtle

# Bildschirmobjekt erzeugen
screen = turtle.Screen()

print(screen.screensize())

# Stiftfarbe setzen
turtle.color('green')

# Strichstärke setzen
turtle.width(5)

# Vorwärts 100 Schritte
turtle.forward(100)

# Rechtsherum drehen um 90 Grad
turtle.right(90)

# Vorwärts 100 Schritte
turtle.forward(100)

# Rechtsherum drehen um 135 Grad
turtle.right(135)

# Vorwärts 141 Schritte
turtle.forward(141)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
