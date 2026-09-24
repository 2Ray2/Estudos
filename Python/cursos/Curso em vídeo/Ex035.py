r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1:
    print('Essa retas podem formar um triangulo!')
else:
    print('Essas retas não podem formar um triangulo!')
