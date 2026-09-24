mil = soma = barato = 0
nome = ' '
print('—' * 20)
print('CAIXA REGISTRADORA')
print('—' * 20)
while True:
    pro = input('Nome do produto: ')
    valor = int(input('Preço:R$'))
    if soma == 0:
        barato = valor
        nome = pro
    soma += valor
    if valor > 1000:
        mil += 1
    cont = input('Quer continuar [N/S]: ').upper().split()[0]
    if cont != 'N' and cont != 'S':
        while cont != 'N' and cont != 'S':
            cont = input('Quer continuar [N/S]: ').upper().split()[0]
    if cont == 'N':
        break
    print('—' * 20)
print('—' * 10, end='')
print(' FIM DO PROGRAMA ', end='')
print('—' * 10)
print(f'''A soma de todos os produtos é R${soma:.2f}
Existem {mil} produtos com o valor maior que R$1000
O poduto com o menor valor é {nome} e custa R${barato:.2f}''')
