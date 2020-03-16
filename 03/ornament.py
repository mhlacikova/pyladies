# ulohy 6,7,8,9
from turtle import left, right,forward,exitonclick

# hranata spirala
strana = 1
uhol = 120

for i in range(7*8):
    forward(strana)
    left(180-uhol)
    strana  = strana + 1
    
exitonclick()

# spirala
strana = 1
uhol = 160 #110 je ruza

for i in range(250):
    forward(strana)
    left(180-uhol)
    strana  = strana + 0.1
    
exitonclick()