# # 0
# zoznam= ['pes','kocka','kralik','had']

# # 1
# vyp = []
# for i in range(len(zoznam)):
#     if len(zoznam[i]) < 5:
#         vyp = vyp + [zoznam[i]]
# print(vyp)

# # 2
# kackove = []
# for i in range(len(zoznam)):
#     if 'k' in zoznam[i][0]:
#         kackove = kackove + [zoznam[i]]
# print(kackove)

# # 3
# slovo = input('Zadaj slovo: ')
# if slovo in zoznam:
#     print('Je to tam!')
# else:
#     print('Slovo nie je v zozname.')

# # 4
# prvy = ['pes','macka','klokan','slon']
# druhy = ['pes','koala','vtak','slon']
# vprvom = []
# vdruhom = []
# oba = []

# for i in range(len(prvy)):
#     if prvy[i] in druhy:
#         oba = oba + [prvy[i]]
#     else:
#         vprvom = vprvom + [prvy[i]]
#         vdruhom = vdruhom + [druhy[i]]

# print('V oboch zoznamoch su: ',oba)
# print('V prvom zozname su: ',vprvom)
# print('V druhom zozname su: ',vdruhom)

# # 5
# zoznam.sort()
# print(zoznam)

# 6
zoznam = ['had','pes','andulka','kocka','kralik']
kluce = []
hodnoty []
for i in range(len(zoznam)):
    kluce = kluce + [zoznam[i][0]]
    hodnoty = hodnoty + [zoznam[i][1:]]
print(kluce)
print(hodnoty)


