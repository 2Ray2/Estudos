pares = 0
numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite novamente um numero: ')),
           int(input('Digite mais um numero: ')))
print(f'''Você digitou os valores {numeros}
O numero 9 apareceu {numeros.count(9)} vezes
{f'O numero 3 apareceu na {numeros.index(3) + 1}ª' if 3 in numeros else 'O numero 3 não foi digitado'}
E os numeros pares são ''',end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
