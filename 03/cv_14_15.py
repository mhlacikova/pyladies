from turtle import speed,penup,pendown,left, right,forward,exitonclick,pencolor, pensize
from random import randrange
speed(0)

# ruza
strana = 0.8
uhol = 110 #110 je ruza

for i in range(150):
    pencolor('red')
    forward(strana)
    left(180-uhol)
    strana  = strana + 0.6

# stonka
right(150)
pencolor('green')
forward(3)
for i in range(20):
    if i%2 == 0:
        dlzka1 = randrange(10,15)
        forward(10)
        left(240)
        forward(dlzka1)
        left(180)
        forward(dlzka1)
        right(60)
    else:
        dlzka2 = randrange(15,20)
        forward(10)
        right(240)
        forward(dlzka2)
        right(180)
        forward(dlzka2)
        left(60)
    right(3)


penup()
forward(10)
right(90)
forward(150)

# oranzovy kvet
for i in range(18):
    pendown()
    pensize(2)
    pencolor('orange')
    for j in range(4):
        forward(50)
        left(90)
    left(20)

# stonka
left(150)
pencolor('green')
pensize(2)
forward(135)
right(180)

for i in range(2):
    for j in range(65):
        right(1)
        forward(2)
    right(115)     
    for k in range(65):
        right(1)
        forward(2)

left(50)
penup()
forward(230)
left(90)
forward(40)

# modry kvietok
for i in range(5):
    pendown()
    pensize(5)
    pencolor('blue')
    for j in range(40):
        right(1)
        forward(1)
    right(130)     
    for k in range(40):
        right(1)
        forward(1)

# stonka
left(180)
pencolor('green')
pensize(2)
for i in range(3):
    for j in range(20):
        right(5)
        forward(2)
    left(50)     
    for k in range(20):
        left(5)
        forward(2)

exitonclick()