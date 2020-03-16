from turtle import penup,pendown,left, right,forward,exitonclick
import math

left(180)
penup()
forward(300)
left(180)

strana = 50
for i in range(5):
    pendown()
    forward(math.sqrt(2*(strana**2)))
    left(135)
    forward(strana)
    left(90)
    forward(strana)
    right(135)

    forward(math.sqrt(2*(strana**2)))
    right(135)
    forward(strana)
    right(90)
    forward(strana)

    right(180)
    forward(strana)
    right(90)
    forward(strana)
    left(135)
    forward(math.sqrt(2*(strana**2)))
    left(135)
    forward(strana)

    right(180)
    forward(strana)
    left(135)
    forward(math.sqrt(2*(strana**2)))

    right(135)
    forward(strana)
    right(90)
    forward(strana)

    right(45)
    forward(math.sqrt(2*(strana**2)))
    left(90)
    forward(strana)

exitonclick()
