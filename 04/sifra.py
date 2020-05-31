# Kontrola vstupu
while True:
    try:
         key = int(input('Zadaj kluc: '))
         break     
    except ValueError:
        print('Kluc musi byt cislo! Skus znovu...')


# Kodovanie
plaintext = input('Zadaj text: ')
pismena = list(plaintext)
asko = {}
ciphertext = ''

for i in range(len(pismena)):
    asko[i] = ord(pismena[i])
    if (asko[i] > 64 and asko[i] < 91) or (asko[i] > 96 and asko[i] < 123):
        asko[i] = asko[i] + key
    else:
        asko[i] = asko[i]
    ciphertext = ciphertext + chr(asko[i])

print('Kodovany text: ',ciphertext)

