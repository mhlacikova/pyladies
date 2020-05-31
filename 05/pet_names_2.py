mena = {'Benny':'pes','Liza':'macka','Larry':'pasavec'}

#1
mena['Leo'] = 'lev'
for kluc,hodnota in mena.items():
    print('{} je {}'.format(kluc,hodnota))

#2
del mena['Leo']
for kluc,hodnota in mena.items():
    print('{} je {}'.format(kluc,hodnota))
