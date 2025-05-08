# Zuordnung:
# Python List-of-list <-> Turtle Screen

# Bibliothek importieren
from turtle import *
import time

# Fenstergröße
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 400

# Datei mit Irrgarten
maze_filename = "maze2.txt"

# Irrgarten-Datei lesen, Anzahl Zeilen und Spalten zurückgeben
def read_maze_file(maze_filename):
    with open(maze_filename, "r") as maze_file:
        maze_list = [
            [ch for ch in line.rstrip("\n")]
            for line in maze_file.readlines()
        ]
        rows_in_maze = len(maze_list)
        columns_in_maze = len(maze_list[0])
        return maze_list, rows_in_maze, columns_in_maze

# Fenstergröße und Koordinatensystem definieren
def setup_screen():
    # Fenster definieren
    setup(SCREEN_WIDTH, SCREEN_HEIGTH)
    mode("world")
    # Fensterobjekt erstellen
    screen = Screen()
    # Koordinatensystem definieren
    # der Quadrate erscheint
    screen.setworldcoordinates(0, 0, columns_in_maze, rows_in_maze)

# Quadrat zeichnen
def DrawSquare(x, y, length=1):
    # keine Spur bei Bewegung zeichnen
    penup()
    # linke untere Ecke des Quadrats
    goto(x, y)
     # nach oben
    setheading(90)
    # Spur bei Bewegung zeichnen
    pendown()
    # Randfarbe
    color("orange")
    # Füllfarbe
    fillcolor("orange")
    # Quadrat zeichnen
    begin_fill()
    for n in range(0, 4):
        forward(length)
        right(90)
    end_fill()

# Transformiere List-of-list Zeilen in Turtle Screen y-Koordinaten
def transform(row):
    # Zeilen von oben nach unten <-> y-Koordinaten von unten nach oben 
    return (rows_in_maze - 1) - row

# Irrgarten zeichnen
def draw_maze():
    # schnell
    speed(10)
    # Turtle Animation ausschalten
    tracer(0)
    # List-of-list zeileweise lesen
    for row in range(rows_in_maze):
        # Zeile spaltenweise lesen 
        for col in range(columns_in_maze):
            if maze_list[row][col] == "+":
                # col ist x-Achse, row ist y-Achse
                DrawSquare(col, transform(row))
    
# Turtle bewegen   
def move_turtle(x, y):
    # keine Spur bei Bewegung zeichnen
    penup()
    # zentrieren
    x += 0.5
    y += 0.5
    # drehen und nach x, y
    setheading(towards(x, y))
    goto(x, y)

# TESTS
# Irrgarten einlesen und in Turtle Screen anzeigen
maze_list, rows_in_maze, columns_in_maze = read_maze_file(maze_filename)
setup_screen()
draw_maze()

# Turtle definieren 
color("black")
fillcolor("blue")
shape("turtle")
# Animation einschalten
tracer(1)
# keine Spur bei Bewegung zeichnen
penup()
# Turtle bewegen
# schnell
speed(10)
move_turtle(0, 0)
time.sleep(2)
move_turtle(columns_in_maze - 1, rows_in_maze - 1)
time.sleep(2)
# List-of-list zeilenweise lesen
for row in range(rows_in_maze):
    # Zeile spaltenweise lesen und Turtle bewegen
    for col in range(columns_in_maze):
        # col ist x-Achse, row ist y-Achse
        move_turtle(col, transform(row))
    # ganze Zeile drucken
    print(maze_list[row])

# mainloop
done()
