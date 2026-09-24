pt = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
for c in range(10):
    termo = pt + c * ra
    print(termo, end=' ⇾ ')
print('FIM!')
