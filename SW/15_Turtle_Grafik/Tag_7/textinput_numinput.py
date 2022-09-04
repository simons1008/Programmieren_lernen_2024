# Demonstration von textinput und numinput

# Modul für die Turtle-Grafik importieren
from turtle import *

# Bildschirmobjekt erzeugen
screen = Screen()

# Strichstärke setzen
width(3)

# Stiftfarbe setzen
color("blue")

# Name abfragen
name = screen.textinput("textinput", "Wie heißt du?")

# Stift abheben, an Position platzieren, aufsetzen
up()
goto(-200, 0)

# Name schreiben und Turtle ans Ende bewegen 
write("Name: " + name + "   ", move=True, font=("Arial", 24))

# Klasse abfragen
klasse = screen.numinput("numinput", "In welcher Klasse bist du?", minval=1, maxval=13)

# In Integer umwandeln
klasse = int(klasse)

# Klasse schreiben und Turtle ans Ende bewegen
write("Klasse: " + str(klasse), move=True, font=("Arial", 24))

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()



