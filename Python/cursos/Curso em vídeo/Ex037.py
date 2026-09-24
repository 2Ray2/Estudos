print('=-=' * 10)
print('Converçor de bases numericas')
print('=-=' * 10)
n = int(input('Digite um numero para a converção: '))
o = int(input('''Digite [ 1 ]Binário [ 2 ]octal [ 3 ]hexadecimal
'''))
if o == 1:
    n1 = bin(n)[2:]
    print('O numero {} convertido para Binário é {}'.format(n, n1))
elif o == 2:
    n1 = oct(n)[2:]
    print('O numero {} convertido para Octal é {}'.format(n, n1))
elif o == 3:
    n1 = hex(n)[2:]
    print('O numero {} convertido para hexadecimal é {}'.format(n, n1))
else:
    print('Opção inconpativel')
