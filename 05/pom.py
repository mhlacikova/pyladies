zoznam= ['pes','kocka','kralik','had']

# 1
slovo = input('Zadaj slovo: ')

if slovo in zoznam:
    print('Je to tam!')
else:
    print('Slovo nie je v zozname.')

print(slovo in zoznam)