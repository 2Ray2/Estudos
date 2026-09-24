from random import randint
from time import sleep
tentativas = 0
n = -1
m = randint(0, 10)
while n != m:
    n = int(input('Tente adivnha que numero a maquina está pensando entre 0 a 10: '))
    print('<<<PRECESANDO>>>')
    tentativas += 1
    sleep(1)
    if n != m:
        if n > m:
            print('Menos...')
        sleep(0.2)
        if n < m:
            print('Mais...')
        sleep(0.2)
print('''Parabens você acertou ψ(｀∇´)ψ
Você precisou de {} tentativas para acertar'''.format(tentativas))
