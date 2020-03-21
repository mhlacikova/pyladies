plaintext = input('Zadaj text: ')
pismena = list(plaintext)
asko = {}
ciphertext = ''

for i in range(len(pismena)):
    asko[i] = ord(pismena[i])
    if (asko[i] > 64 and asko[i] < 91) or (asko[i] > 96 and asko[i] < 123):
        asko[i] = asko[i] + 1
    else:
        asko[i] = asko[i]
    ciphertext = ciphertext + chr(asko[i])

print(ciphertext)
