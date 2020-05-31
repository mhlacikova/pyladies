zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

chybne = []
spravne = []
opravene = []
meno = []

for i in range(len(zaznamy)):
    meno = zaznamy[i].split()
    if (meno[0].islower() == True) or (meno[1].islower() == True) :
        chybne = chybne + [zaznamy[i]]
        opravene = opravene + [zaznamy[i].title()]
    else:
        spravne = spravne + [zaznamy[i]]

print('Chybne zaznamy: ',chybne)
print('Spravne zaznamy: ',spravne)
print('Opravene zaznamy: ',opravene)
