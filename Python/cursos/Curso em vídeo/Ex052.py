from sympy import isprime
n = int(input('Digite um valor para saber se ele é ou não primo: '))
if isprime(n):
    print('Esse numero é primo')
else:
    print('Esse numero não é primo')
