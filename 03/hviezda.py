from turtle import penup,pendown,left, right,forward,exitonclick

# snehove vlocky
for i in range(10):
    for j in range(9):
        pendown()
        left(120)
        forward(10)
        left(120)
        forward(10)
        right(120)
        forward(10)

    penup()
    forward(randrange(20,50))


exitonclick()