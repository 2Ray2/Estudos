menor = maior =media = soma = cont = 0
mais = ''
while mais != 'N':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    mais = input('Digite "Não" para parar e "Sim" para continuar: ').upper().split()[0]
    if mais == 'N':
        mais = 'N'
        print('~'* 50)
    elif mais == 'S':
        mais = 'S'
        print('~' * 50)
    else:
        print('Resposta incompativel')
media = soma / cont
print('''Foram digitados {} numeros e a media deles é {:.2f}
O maior entre eles é {} e o menor é {}'''.format(cont, media, maior, menor))
