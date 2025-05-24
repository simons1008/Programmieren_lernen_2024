# Programm erzeugt ein Fenster und setzt die Wände eines Irrgartens hinein
# Modul für die Turtle-Grafik importieren
import turtle
# Zeichen für Wand und Freiraum
OBSTACLE = "+"
BLANK = " "
# Irrgarten-Klasse 
class Maze:
    """Klasse für den Bau eines Irrgartens"""
    # Methoden der Klasse
    def __init__(self):
        self.maze_list =\
        [['+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+','+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
         ['+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+','+']]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        print(self.rows_in_maze, self.columns_in_maze)
        # turtle Objekt erzeugen und Aussehen festlegen 
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        # Koordinaten des Fensters festlegen
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(0, 0, self.columns_in_maze, self.rows_in_maze)
    # Transformiere die Zeilennummer (row)
    def transform(self, row):
        # Zeilen der Liste laufen von oben nach unten
        # y Koordinaten des Fensters laufen von unten nach oben 
        return (self.rows_in_maze - 1) - row
    # Zeichne ein ausgefülltes Rechteck
    def draw_box(self, x, y, color):
        self.t.up() # Stift hoch
        self.t.goto(x, y)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down() # Stift runter
        self.t.begin_fill()
        # Rechteck zeichnen und füllen
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
    def draw_maze(self):
        # Animation des Roboters ausschalten
        self.wn.tracer(0)
        # Setze Wände in das Fenster. Die Farben 'white', 'black', 'red',
        # 'green', 'blue', 'cyan', 'yellow' und 'magenta' sind verfügbar.
        for row in range(self.rows_in_maze):
            for col in range(self.columns_in_maze):
                if self.maze_list[row][col] == OBSTACLE:
                    self.draw_box(col, self.transform(row), "orange")
        # Farbe des Roboters
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        # Animation des Roboters einschalten
        self.wn.tracer(1)
# Instanz erzeugen
my_maze = Maze()
# Irrgarten zeichnen
my_maze.draw_maze()
my_maze.t.up() # Stift hoch
# Schildkröte in Home-Position
my_maze.t.home()
# Turtle event loop
my_maze.wn.mainloop()
