n = 0
for c in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        n += num
print('A soma de todos os numeros pares é {}'.format(n))
