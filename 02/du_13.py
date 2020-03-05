rychlost = float(input('Ahoj! Povedz mi, akou rýchlosťou sa pohybuješ a ja ti poviem, ktoré zviera sa pohybuje rovnakou rýchlosťou, ako ty. \nZadaj rýchlosť: '))

if rychlost >= 160:
    print('Naozaj ideš tak rýchlo? Môžeš dostať pokutu! Skús menšiu rýchlosť.')
elif rychlost >= 130:
    print('Waw! Pohybuješ sa tak rýchlo, ako orol počas lovu! \nDávaj si pozor!')
elif rychlost >= 110:
    print('Waw! Momentálne ideš rýchlosťou geparda počas behu!')
elif rychlost >= 90:
    print('Oooo! Je ze teba gazela!')
elif rychlost >= 80:
    print('Oooo! Je ze teba Klokan!')
elif rychlost >= 75:
    print('Si rýchly/a ako zebra!')
elif rychlost >= 70:
    print('Pohybuješ sa tak rýchlo, ako kosatka pláva!')
elif rychlost >= 65:
    print('Máš rýchlosť leva!')
elif rychlost >= 50:
    print('Oooo! Je ze teba žirafa!')
elif rychlost >= 40:
    print('Oooo! Je ze teba nosorožec!')
elif rychlost >= 35:
    print('Oooo! Je ze teba slon!')
elif rychlost >= 20:
    print('Presne takto rýchlo dokáže ísť ťava!')
elif rychlost >= 15:
    print('Letíš rýchlosťou čmeliaka!')
elif rychlost >= 8:
    print('Tatkto rýchlo pláva kapor!')
elif rychlost >= 5:
    print('Tatkto rýchlo sa pohybuje chobotnica!')
elif rychlost >= 3.2:
    print('Je z teba dikobraz!')
elif rychlost >= 0.05:
    print('Tatkto rýchlo chodí korytnačka!')
elif rychlost >= 0:
    print('Skutočne? Takto pomaly chodí len slimák!')
else:
    print('Nemôžeš sa predsa pohybovať zápornou rýchlosťou!')