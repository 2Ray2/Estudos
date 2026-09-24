lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite um valor para colocar na posição {c}°: ')))
print(f'Você digitoi os seguintes valores {lista}')
print(f'O maior valor foi o {max(lista)} que apareceu nas seguintes posiçoes ', end='')
for posi, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posi + 1}...', end='')
print()
print(f'O menor valor foi o {min(lista)} que aparece nas seguintes posiçoes ', end='')
for posi, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posi + 1}...', end='')
