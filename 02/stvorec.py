# Tento program pocita obsah a obvod stvorca so zvolenou stranou

a = float(input('Zadaj dlzku strany stvorca v cm:'))
cislo_ok = a > 0
if cislo_ok:
    obvod = 4*a
    obsah = a*a
    print('Obvod stvorca so stranou', a, 'cm je',obvod,'cm')
    print('Obsah stvorca so stranou', a, 'cm je',obsah,'cm2')
else:
    print('Cislo nesmie byt negativne!')

print('Vdaka za pouzitie geometrickej kalkulacky!')
