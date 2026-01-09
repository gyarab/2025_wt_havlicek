from turtle import *
from math import *
from random import *




def draw_house(a):
    b = sqrt(2) * a
    left(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(135)
    forward(b)
    right(90)
    forward(b/2)
    right(90)
    forward(b/2)
    right(90)   
    forward(b)
    left(135)
    forward(a)

for i in range(10):
    draw_house(randint(50, 150))
    right(36)

exitonclick()