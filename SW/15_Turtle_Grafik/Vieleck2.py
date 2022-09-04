# Zeichne ein regelmäßiges Vieleck

# Benutzer fragen mit Fehlerbehandlung
def benutzereingabe() -> int:
    while True:
        n = input("Bitte Anzahl der Ecken eingeben: ")
        # Prüfe auf Ausnahme (Exception)
        try:
            n = int(n)
        # Ausnahme behandeln
        except ValueError:
            print("Bitte Zahl von 1 bis 10 eingeben")
        # keine Ausnahme
        else:
            # liegt n im Wertebereich
            if n >= 1 and n <= 10:
                return n
            # n liegt nicht im Wertebereich
            else:
                print("Zahl muss zwischen 1 und 10 liegen")

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
n = benutzereingabe()

# Vieleck zeichnen
vieleck(n)

# Hauptschleife, damit die Turtle-Grafik angezeigt wird
screen.mainloop()
