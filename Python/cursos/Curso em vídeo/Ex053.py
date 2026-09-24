pala = input('Digite uma palavra: ').replace(' ', '')
inv = pala[::-1]
print('A inversão da palavra {} é {}'.format(pala, inv))
if pala == inv:
    print('Essa palavra é um palíndromo')
else:
    print('Essa palavra não é um palíndromo')
