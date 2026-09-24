pa = 1
pt = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
termo = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while pa <= total:
        print(termo, end=' ⇾ ')
        termo = pt + pa * ra
        pa += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')