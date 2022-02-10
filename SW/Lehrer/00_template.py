# Quelle: http://www.coding4you.at/python/turtle.html

from turtle import Screen, Turtle

def motion(event):
    canvas.unbind("<Motion>")
    x = event.x
    y = event.y
    turtle.clear()
    #---- Änderungen hier machen
    #---- Zeichenoperationen sollen x,y verwenden (Mausposition)
    turtle.write(str(x) + " " + str(y), False)
    turtle.rt(y//3)
    turtle.fd(x)
    turtle.bk(x)
    turtle.lt(y//3)
    #---- Nach diesem Block soll die Turtle wieder am selben Punkt stehen.
    #-----------------------------
    screen.update()
    canvas.bind("<Motion>", motion)

screen = Screen()
screen.setup(600, 600)
screen.tracer(0,0)
turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.pensize(2)
canvas = screen.getcanvas()
canvas.bind("<Motion>", motion)
screen.mainloop()






