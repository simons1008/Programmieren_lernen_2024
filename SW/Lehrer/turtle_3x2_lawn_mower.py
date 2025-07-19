# Der Roboter soll jeden Punkt der Fläche erreichen
# Der Roboter soll möglichst wenig doppelte Wege machen
# Die Darstellung "Roboter fährt - Turtle folgt" basiert auf der Quelle:  
# https://runestone.academy/ns/books/published/pythonds3/Recursion/ExploringaMaze.html
# Die "heading properties" werden durch Dictionarys angegeben. Quelle:
# https://gist.github.com/maxrothman/92eb8470408a047b1f6815a4a444d727
# Das Abfahren der Fläche in Streifen wurde hier vorgeschlagen:
# http://allegrobotics.com/mowingAlgorithm.html
# Die Turtle-Ausrichtung wird durch das Dictionary "angle_of" bestimmt
# Die Bewegung des Roboters wird durch das Dictionary "sequences" vorgegeben
# Ende der Suche bei WATER oder EXIT

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
angle_of  = {"up": 90     , "down": -90    , "left": 180   , "right": 0     }

# sequences
snake_right        = {"odd": "u_turn_right", "even": "u_turn_left" }
needle_point_right = {"odd": "u_turn"      , "even": "u_turn_left"}
needle_head_right  = {"odd": "u_turn_right", "even": "u_turn"      }
snake_left         = {"odd": "u_turn_left" , "even": "u_turn_right"}
needle_point_left  = {"odd": "u_turn"      , "even": "u_turn_right" }
needle_head_left   = {"odd": "u_turn_left" , "even": "u_turn"      }


#########################
## Meine Einstellungen ##
# heading
my_heading = "up"

# sequence
my_sequence = snake_right
##########################

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

    def adjust_turtle(self, heading):
        self.t.speed(10)
        # adjust turtle
        self.t.setheading(angle_of[heading])

    def look_forward(self, start_row, start_col, heading):
        # im Exit nicht nach vorne schauen!
        if self.is_exit(start_row, start_col) == True:
            return EXIT
        else:
            return self.maze_list[start_row + delta_row[heading]]\
                             [start_col + delta_col[heading]]

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

def is_odd(count):
    return count%2 == 1

def search_from(maze, start_row, start_col):
    # Spur bis zum Start verbergen
    maze.t.up()
    maze.update_position(start_row, start_col, BLANK)
    # Spur einschalten
    maze.t.down()
    # Roboter-Ausrichtung
    heading = my_heading
    # Turtle-Ausrichtung
    maze.adjust_turtle(heading)
    # Kollisions-Zähler
    collision_count = 0

    while maze.is_exit(start_row, start_col) == False:
        # solange vorne frei ist
        while maze.look_forward(start_row, start_col, heading) == BLANK:
            start_row, start_col = maze.one_step(start_row, start_col, heading)
            maze.update_position(start_row, start_col)
        # Kollision: Zähler erhöhen
        collision_count += 1
        # Wasser gefunden?
        if maze.look_forward(start_row, start_col, heading) == WATER:
            print("Wasser gefunden!!")
            break      
        # Exit erreicht?
        elif maze.is_exit(start_row, start_col) == True:
            break

        # sequence key bestimmen
        if is_odd(collision_count):
            my_collision = "odd"
        else:
            my_collision = "even"
            
        # my_sequence[my_collision] ausführen
        if my_sequence[my_collision] == "u_turn_right":
            # drehen
            heading = maze.turn_right(heading)
            # vorne frei: 1 Schritt vorwärts
            if maze.look_forward(start_row, start_col, heading) == BLANK:
                start_row, start_col = maze.one_step(start_row, start_col, heading)
                maze.update_position(start_row, start_col)
            # Wasser gefunden?
            if maze.look_forward(start_row, start_col, heading) == WATER:
                print("Wasser gefunden!!")
                break      
            # drehen
            heading = maze.turn_right(heading)                  
        elif my_sequence[my_collision] == "u_turn":
            # auf der Stelle drehen
            heading = maze.turn_right(heading)
            heading = maze.turn_right(heading)
        elif my_sequence[my_collision] == "u_turn_left":
            # drehen
            heading = maze.turn_left(heading)
            # vorne frei: 1 Schritt vorwärts
            if maze.look_forward(start_row, start_col, heading) == BLANK:
                start_row, start_col = maze.one_step(start_row, start_col, heading)
                maze.update_position(start_row, start_col)
            # Wasser gefunden?
            if maze.look_forward(start_row, start_col, heading) == WATER:
                print("Wasser gefunden!!")
                break      
            # drehen
            heading = maze.turn_left(heading)                  
        else:
            print("ERROR: unsupported sequence value")
    # Ende der while-Schleife
    print("Ende erreicht!")
    print(collision_count, "Kollisionen")


my_maze = Maze("maze5.txt")
my_maze.draw_maze()
my_maze.t.home()
search_from(my_maze, my_maze.start_row, my_maze.start_col)

my_maze.wn.mainloop()
