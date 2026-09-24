from random import randint
from time import sleep
jogadores = {}
cont = 0
print(f'{"Sorteando jogos":^40}')
for c in range(1, 5):
    sleep(1)
    dado = randint(1, 6)
    jogadores[f'jogador{c}'] = dado
    print(f'O jogador{c} tirou {dado}')
sleep(1)
ordem = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print(f'{"A ordem por numero":^40}')
for j, v in ordem.items():
    cont += 1
    sleep(1)
    print(f'{cont}° é o {j} que tirou {v}')
print()