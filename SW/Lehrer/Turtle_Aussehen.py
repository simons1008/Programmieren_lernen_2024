# Die Turtle hat das Aussehen eines Balls

# Modul für die Turtle-Grafik importieren
import turtle

# Bildschirmobjekt erzeugen
screen = turtle.Screen()

# GIF-Bild laden
image = "intro_ball.gif"

# Turtle-Aussehen zur Aussehen-Liste hinzufügen
# Note: Image shapes do not rotate when turning the turtle,
# so they do not display the heading of the turtle! 
screen.addshape(image)

# Turtle-Aussehen festlegen
turtle.shape(image)

# Quadrat zeichnen
for i in range(4):
    # Vorwärts 200 Schritte
    turtle.forward(200)
    # Rechtsherum drehen um 90 Grad
    turtle.right(90)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
