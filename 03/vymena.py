retaz = input('Zadaj retazec:')
poz = int(input('Zadaj poziciu, ktoru chces vymenit:'))
zmena = input('Zadaj pozadovanu zmenu:')

novy = retaz[:poz-1] + zmena + retaz[poz:]
# posunute, lebo bezne clovek nevie, ze sa inexuje od 0

print('Zmeneny retazec je:',novy)