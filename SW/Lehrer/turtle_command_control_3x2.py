# Quelle: https://runestone.academy/ns/books/published/pythonds3/Recursion/ExploringaMaze.html
# Geändert: "maze_list aus Datei lesen" mit zwei Schleifen codiert
#           "Start in maze_list suchen" mit zwei verschachtelten Schleifen codiert
#           Funktion __getitem__() entfällt
#           setworldcoordinates mit Ursprung in der linken unteren Ecke
#           self.x_translate und self.y_translate entfallen
#           neue Funktion from_bottom(self, row)
#           draw_centered_box ersetzt durch draw_box
#           move_turtle bewegt Turtle in die Mitte der Box
#           search_from() arbeitet Kommandos
#           Aufruf von mainloop hinzugefügt
#           WATER hinzugefügt

import turtle
import time

START = "S"
OBSTACLE = "+"
BLANK = " "
EXIT = "E"
WATER = "W" 

# heading properties
right_of  = {"up": "right", "down": "left" , "left": "up"  , "right": "down"}
left_of   = {"up": "left" , "down": "right", "left": "down", "right": "up"  }
delta_row = {"up": -1     , "down": 1      , "left": 0     , "right": 0     }
delta_col = {"up": 0      , "down": 0      , "left": -1    , "right": 1     }

# commands
# zum Wasser 1
my_command = ["steps, 5", "turn_left", "steps, 4", "turn_right", "steps, 3", "turn_right", "steps, 4", "turn_left", "steps, 4"]
# zum Wasser 2
#my_command = ["steps, 4", "turn_left", "steps, 5", "turn_right", "steps, 8", "turn_right", "steps, 5"]
# zum Ausgang
#my_command = ["steps, 4", "turn_left", "steps, 5", "turn_right", "steps, 11", "turn_left", "steps, 4"]
# zur Wand
#my_command = ["steps, 4", "turn_left", "steps, 5", "turn_right", "steps, 14"]


class Maze:
    def __init__(self, maze_filename):
        self.maze_list = []
        with open(maze_filename, "r") as maze_file:
            self.lines = maze_file.readlines()
            for line in self.lines:
                self.maze_list.append([ch for ch in line.rstrip("\n")])
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        print("rows_in_maze =", self.rows_in_maze, "columns_in_maze =", self.columns_in_maze)
        # Start in maze_list suchen
        for row in range(self.rows_in_maze):
            for col in range(self.columns_in_maze):
                if self.maze_list[row][col] == START:
                    self.start_row = row
                    self.start_col = col
                    break

        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setup(900, 600)
        self.wn.setworldcoordinates(0, 0, self.columns_in_maze, self.rows_in_maze)
  
    def from_bottom(self, row):
        # rows from top to bottom <-> y coordinates from bottom to top 
        return (self.rows_in_maze - 1) - row

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for row in range(self.rows_in_maze):
            for col in range(self.columns_in_maze):
                if self.maze_list[row][col] == OBSTACLE:
                    self.draw_box(
                        col, self.from_bottom(row), "orange"
                    )
                elif self.maze_list[row][col] == WATER:
                    self.draw_box(
                        col, self.from_bottom(row), "lightblue"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_box(self, x, y, color):
        self.t.up()
        self.t.goto(x, y)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        #self.t.up()
        x += 0.5
        y += 0.5
        self.t.setheading(self.t.towards(x, y))
        self.t.goto(x, y)

    def update_position(self, row, col, val=None):
        # delete START character
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, self.from_bottom(row))

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def init_search(self):
        self.t.speed(3)
        self.t.setheading(90)
        heading = "up"
        time.sleep(1)
        return heading

    def look_forward(self, start_row, start_col, heading):
        # im Exit nicht nach vorne schauen!
        if self.is_exit(start_row, start_col) == True:
            return EXIT
        else:
            return self.maze_list[start_row + delta_row[heading]]\
                                 [start_col + delta_col[heading]]

    def look_right(self, start_row, start_col, heading):
        return self.maze_list[start_row + delta_row[right_of[heading]]]\
                             [start_col + delta_col[right_of[heading]]]
       
    def one_step(self, start_row, start_col, heading):
        start_row += delta_row[heading]
        start_col += delta_col[heading]
        return start_row, start_col

    def turn_right(self, heading):
        self.t.right(90)
        return right_of[heading]
    
    def turn_left(self, heading):
        self.t.left(90)
        return left_of[heading]

def search_from(maze, start_row, start_col):
    # Spur bis zum Start verbergen
    maze.t.up()
    maze.update_position(start_row, start_col, BLANK)
    # Spur einschalten
    maze.t.down()
    heading = maze.init_search()

    # Drehungen zählen
    turn_count = 0

    # Führe Kommands aus
    for cmd in my_command:
        my_list = cmd.split(",")
        if my_list[0] == "steps":
            for i in range(int(my_list[1])):
                if maze.look_forward(start_row, start_col, heading) == BLANK:
                    start_row, start_col = maze.one_step(start_row, start_col, heading)
                    maze.update_position(start_row, start_col)
                else:
                    print("cannot move in this direction")
                    break
        elif my_list[0] == "turn_right":
            heading = maze.turn_right(heading)
            turn_count += 1
        elif my_list[0] == "turn_left":
            heading = maze.turn_left(heading)
            turn_count += 1
        else:
            print("unbekanntes Kommando")
    # Ende der Kommando-Schleife

    # Ergebnis prüfen
    if maze.is_exit(start_row, start_col) == True:
        print("Ausgang erreicht")
    elif maze.look_forward(start_row, start_col, heading) == WATER:
        print("Wasser gefunden")
    elif maze.look_forward(start_row, start_col, heading) == OBSTACLE:
        print("An der Wand!")
    else:
        print("Normales Ende der Kommando-Schleife")

    # Anzahl der Drehungen ausgeben
    print(turn_count, "Drehungen")

my_maze = Maze("lawn5-1.txt")
my_maze.draw_maze()
my_maze.t.home()
search_from(my_maze, my_maze.start_row, my_maze.start_col)

my_maze.wn.mainloop()
