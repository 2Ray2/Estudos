from time import sleep
lista = []
cont = ''
while cont != 'N':
    n = int(input('Digite um numero: '))
    if n not in lista:
        sleep(0.5)
        print('Valor adicionado com sucesso...')
        sleep(0.5)
        lista.append(n)
    else:
        sleep(0.5)
        print('Valor duplicado! Não vou adicionar...')
        sleep(0.5)
    cont = input('Você quer continuar?:[S/N] ').upper().split()[0]
    while cont != 'N' and cont != 'S':
        cont = input('Opção incorreta!Você quer continuar?:[S/N] ').upper().split()[0]
        if cont == 'N':
            break
print('-' * 30)
print(f'O valores digitados foram {sorted(lista)}')
