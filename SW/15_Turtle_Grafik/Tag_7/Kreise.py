# Verschiedene Kreise zeichnen

# Modul für die Turtle-Grafik importieren
import turtle

# Bildschirmobjekt erzeugen
screen = turtle.Screen()

# Bildschirmgröße setzen
screen.setup(500, 500)

# Strichstärke setzen
turtle.width(5)

# Kreis mit 50 Pixel Radius
turtle.circle(50)

# Stift abheben, an Position platzieren, aufsetzen
turtle.up()
turtle.goto(100,100)
turtle.down()

# Stiftfarbe setzen
turtle.color('orange')

# Kreis mit 50 Pixel Radius
turtle.circle(50)

# Stift abheben, an Position platzieren, aufsetzen
turtle.up()
turtle.goto(-100, -100)
turtle.down()

# Stiftfarbe setzen
turtle.color('red')

# Kreisausschnitt mit 50 Pixel Radius und 90 Grad (Viertelkreis)
turtle.circle(50,90)

# Stift abheben, an Position platzieren, aufsetzen
turtle.up()
turtle.goto(-200, 150)
turtle.down()

# Stiftfarbe setzen
turtle.color('green')

# Text schreiben
turtle.write('Turtle ist super', font=('Arial', 24))

# Turtle unsichtbar machen
turtle.hideturtle()

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
