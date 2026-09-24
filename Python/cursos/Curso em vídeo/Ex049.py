n = int(input('Digite o numero da tabuada: '))
print('-' * 12)
print('Taboada {}'.format(n))
for m in range(1, 11):
    print('{} x {} = {}'.format(n, m, n * m))
print('-' * 12)