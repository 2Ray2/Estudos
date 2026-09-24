from random import randint
from time import sleep
jogos = []
numeros = []
quantidade = int(input('Quantos jogos você quer que eu sorteio ?: '))
for i in range(quantidade):
    for c in range(6):
        numero = randint(1, 60)
        if c > 0:
            while numero in numeros:
                numero = randint(1, 60)
        numeros.append(numero)
    jogos.append(numeros[:])
    numeros.clear()
print(f'{f" Sorteando {quantidade} jogos ":=^30}')
for k in range(quantidade):
    print(f'Jogo {k + 1}: {jogos[k]}')
    sleep(1)
sleep(1)
print(f'{"Boa Sorte":=^30}')