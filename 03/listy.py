from turtle import speed,penup,pendown,left, right,forward,exitonclick,pencolor
from random import randrange
speed(0)

# stonka
left(180)
pencolor('green')

for i in range(5):
    for j in range(20):
        right(5)
        forward(2)
    left(15)     
    for k in range(20):
        left(5)
        forward(2)

exitonclick()