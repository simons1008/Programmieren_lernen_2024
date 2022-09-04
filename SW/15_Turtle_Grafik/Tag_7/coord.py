# Quelle: http://www.coding4you.at/python/turtle.html
from turtle import *

setup(500, 500)
shape("turtle")

# Kreuz beim Ursprung zeichnen
fd(10)
bk(20)
fd(10)
lt(90)
fd(10)
bk(20)
fd(10)
rt(90)

# Winkel von 30 Grad zeichnen
setheading(30)
pu()
fd(100)
pd()
fd(100)
bk(100)
rt(30)
fd(100)
bk(100)
lt(30)









