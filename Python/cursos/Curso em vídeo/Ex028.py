from random import randint
from time import sleep
e = int(input('Tente adivinhar o numero de 0 a 5: '))
n = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if e == n:
    print('Parabens voce acertou o numero :)')
else:
    print('Não foi dessa vez :(')
print('O numero certo era ', n)