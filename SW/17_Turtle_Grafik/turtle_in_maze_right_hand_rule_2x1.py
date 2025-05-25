# Quelle: https://runestone.academy/ns/books/published/pythonds3/Recursion/ExploringaMaze.html
# Geändert: setworldcoordinates mit Ursprung in der linken unteren Ecke
#           self.x_translate und self.y_translate entfallen
#           neue Funktion transform(self, row)
#           draw_centered_box ersetzt durch draw_box
#           move_turtle bewegt Turtle in die Mitte der Box
#           search_from() arbeitet mit der Rechten-Hand-Regel
#           Aufruf von mainloop hinzugefügt

import turtle
import time

START = "S"
OBSTACLE = "+"
BLANK = " "

# heading properties
right_of  = {"up": "right", "down": "left" , "left": "up"  , "right": "down"}
left_of   = {"up": "left" , "down": "right", "left": "down", "right": "up"  }
delta_row = {"up": -1     , "down": 1      , "left": 0     , "right": 0     }
delta_col = {"up": 0      , "down": 0      , "left": -1    , "right": 1     }

class Maze:
    def __init__(self, maze_filename):
        with open(maze_filename, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.rstrip("\n")]
                for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break

        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setup(800, 400)
        self.wn.setworldcoordinates(0, 0, self.columns_in_maze, self.rows_in_maze)
  
    def transform(self, row):
        # rows from top to bottom <-> y coordinates from bottom to top 
        return (self.rows_in_maze - 1) - row

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for row in range(self.rows_in_maze):
            for col in range(self.columns_in_maze):
                if self.maze_list[row][col] == OBSTACLE:
                    self.draw_box(
                        col, self.transform(row), "orange"
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
        self.move_turtle(col, self.transform(row))

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]

    def init_search(self):
        self.t.speed(3)
        self.t.setheading(90)
        heading = "up"
        time.sleep(1)
        return heading

    def look_forward(self, start_row, start_col, heading):
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

    # solange kein Exit und vorne frei ist
    while maze.is_exit(start_row, start_col) == False\
      and maze.look_forward(start_row, start_col, heading) == BLANK:
        start_row, start_col = maze.one_step(start_row, start_col, heading)
        maze.update_position(start_row, start_col)
    # drehen, damit rechte Hand an der Wand ist
    heading = maze.turn_left(heading)

    # Drehungen zählen
    turn_count = 1

    # Folge der Wand bis Exit
    while maze.is_exit(start_row, start_col) == False:
        
        # solange vorne frei und die Wand rechts ist
        while maze.look_forward(start_row, start_col, heading) == BLANK\
          and maze.look_right(start_row, start_col, heading) == OBSTACLE:
            start_row, start_col = maze.one_step(start_row, start_col, heading)
            maze.update_position(start_row, start_col)

        # wenn die Wand nicht mehr rechts ist
        if maze.look_right(start_row, start_col, heading) == BLANK:
            # drehen und 1 Schritt vorwärts, damit rechte Hand an der Wand ist
            heading = maze.turn_right(heading)
            turn_count += 1
            start_row, start_col = maze.one_step(start_row, start_col, heading)
            maze.update_position(start_row, start_col)

        # wenn vorne eine Wand ist
        elif maze.look_forward(start_row, start_col, heading) == OBSTACLE:
            # drehen, damit rechte Hand an der Wand ist
            heading = maze.turn_left(heading)
            turn_count += 1

    # Ende der while-Schleife
    print("Exit found!")
    print(turn_count, "Drehungen")


my_maze = Maze("maze3.txt")
my_maze.draw_maze()
my_maze.t.home()
search_from(my_maze, my_maze.start_row, my_maze.start_col)

my_maze.wn.mainloop()
