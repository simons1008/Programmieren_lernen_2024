# Scale a Turtle drawing
# Although Python's turtle graphics provide all the usual transformations
# (scale, shear, tilt, etc.) for the turtle image itself, it doesn't
# provide them for the images it draws!
# Rather than add a scaling factor to every drawing routine you define,
# let's try to manipulate the image scale independent of your drawing
# routines:
# Quelle: https://stackoverflow.com/questions/36224422/python-turtle-positional-errors/36660290#36660290
#
# What does the turtle.setworldcoordinates function do?
# I believe setworldcoordinates() allows you to select a coordinate system
# that's more convenient for your problem. For example, suppose you don't
# want (0,0) in the center of the screen. Instead of incorporating an
# offset, you can use setworldcoordinates() to move it to a corner if that
# works better for you. You can also set up coordinate systems that have a
# different scaling factor in the horizontal vs. the verical.
# https://stackoverflow.com/questions/37154189/what-does-the-turtle-setworldcoordinates-function-do
from turtle import *
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

def DrawSquare(length=1):

    oldPos = pos()
    setheading(0)
    pendown()

    for n in range(0, 4):
        forward(length)
        left(90)

    setpos(oldPos)

def Scale(x=1, y=1):
    screen = Screen()
    screen.setworldcoordinates(- (SCREEN_WIDTH / (x * 2)), - (SCREEN_HEIGHT / (y * 2)), (SCREEN_WIDTH / (x * 2)), (SCREEN_HEIGHT / (y * 2)))

setup(SCREEN_WIDTH, SCREEN_HEIGHT)
mode("world")

penup()
goto(-25, -25)

# TESTS

Scale(1, 1) # normal size
DrawSquare(50)
time.sleep(2)

Scale(1, 2)  # twice as tall
time.sleep(2)

Scale(2, 1)  # twice as wide
time.sleep(2)

Scale(2, 2)  # twice as big
time.sleep(2)

Scale(1, 1)  # back to normal

done()
