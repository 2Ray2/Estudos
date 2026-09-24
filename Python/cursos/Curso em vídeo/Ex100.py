from random import randint
from time import sleep
numeros = []


def sorteia():
    for c in range(1, 6):
        numeros.append(randint(1, 10))


sorteia()
print(f'Os numeros sorteados foram ', end='')
for cont, numero in enumerate(numeros):
    print(numeros[cont], end=' ')
    #sleep(0.5)
print()
numeros_pares = []


def somapar():
    for number in numeros:
        if number % 2 == 0:
            numeros_pares.append(numero)


somapar()
print(f'Somando os numeros pares de ', end='')
for numero in numeros:
    print(numero, end=' ')
print(f'temos {sum(numeros_pares)}')