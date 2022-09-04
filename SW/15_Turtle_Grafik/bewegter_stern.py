# Quelle: http://www.coding4you.at/python/turtle.html
# Der nicht ausgeführte Code wurde entfernt

from turtle import Screen, Turtle

def motion(event):
    canvas.unbind("<Motion>")
    x = event.x
    y = event.y
    turtle.clear()
    num = x // 10
    for i in range(num):
        turtle.fd(y)
        turtle.bk(y)
        turtle.lt(360/num)
    turtle.pu()
    #turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pd()
    screen.update()
    canvas.bind("<Motion>", motion)

screen = Screen()
screen.setup(600, 600)
screen.tracer(0,0)
turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.pensize(2)
#turtle.pu()
canvas = screen.getcanvas()
canvas.bind("<Motion>", motion)
screen.mainloop()






