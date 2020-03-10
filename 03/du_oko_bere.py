from random import randrange
print('Vitam ta v hre Oko bere! \nCielom hry je ziskat co najviac bodov, maximalne vsak 21. \nV pripade, ze ziskas viac bodov, prehravas. \nTahaj a neboj sa riskovat!')

body = 0
print('Tvoj aktualny pocet bodov je:',body)
vstup = input('Chces potiahnut kartu? Napis ano/nie: ')

while vstup == 'ano':
    body = body + randrange(2,10)
    print('Tvoj aktualny pocet bodov je:',body)
    if body > 21:
        print('Prehral si!')
        break
    elif body < 21:
        print('Este skus tahat!')
        vstup = input('Chces potiahnut kartu? Napis ano/nie: ')
        if vstup == 'nie':
            break
    else:
        print('Gratulujem! Vyhral si!')
        break

if vstup == 'nie':
    print('Tvoj aktualny pocet bodov je:',body)
    print('Mohol si sa viac snazit a riskovat!')

elif not (vstup == 'ano') or (vstup == 'nie'):
     print('Nerozumiem')

else:
    print('Dakujem za hru.')