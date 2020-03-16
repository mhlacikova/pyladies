# ulohy 6,7,8,9
from turtle import left, right,forward,exitonclick
pocet = int(input('Zadaj pocet uhlov: '))

strana = 200/pocet
uhol = 180*(1-2/pocet)

for i in range(pocet):
    forward(strana)
    left(180-uhol)
    


exitonclick()