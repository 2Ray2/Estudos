pa = 1
pt = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
termo = pt
while pa <= 10:
    print(termo, end=' ⇾ ')
    termo = pt + pa * ra
    pa += 1
print('Acabou!')