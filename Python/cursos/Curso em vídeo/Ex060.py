n = int(input('Digite um valor para saber sua Fatoial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))