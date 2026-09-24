n = '0000'
n1 = input('Digite um numero de no maximo 4 digitos: ')
n2 = n + n1
n3 = list(n2[::-1])
print('''Sua unidade é {}
Dezena {}
Centena {}
Milhar {}'''.format(n3[0], n3[1], n3[2], n3[3], n3[4]))
n4 = int(''.join(n3))