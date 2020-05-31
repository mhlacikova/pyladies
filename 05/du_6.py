# 6
zoznam = ['had','pes','andulka','kocka','kralik']

kluce = []
hodnoty = []

for i in range(len(zoznam)):
    kluce = kluce + [zoznam[i][0]]
    hodnoty = hodnoty + [zoznam[i][1:]]

slovnik ={}
for i in range(len(zoznam)):
    slovnik[i] = slovnik + {kluce[i]:hodnoty[i]}
print(slovnik)