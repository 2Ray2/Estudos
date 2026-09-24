r1 = float(input('Digite uma reta: '))
r2 = float(input('Digite outra reta: '))
r3 = float(input('Digite uma terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Essa retas PODEM FORMAR um triangulo.', end='')
    if r1 == r2 == r3:
        print('O triangulo formado é um EQUÍLATERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triangulo formado é um ESÓSCELES')
    else:
        print('O trangulo formado é um ESCALENO')
else:
    print('Essa retas NÃO PODEM forar um triangulo')
