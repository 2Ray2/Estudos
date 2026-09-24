while True:
    print('—' * 80)
    n = int(input('Digite um numero para saber sua tabuada (Digite um numero negativo para parar): '))
    print('—' * 80)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
print('Encerando progama, volte sempre!')
