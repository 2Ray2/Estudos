from math import hypot
co = float(input('Digite o valor do cateco oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('Calculando o valor de {} e {} a ipotenusa é {:.2f}'.format(co, ca, hypot(co, ca)))