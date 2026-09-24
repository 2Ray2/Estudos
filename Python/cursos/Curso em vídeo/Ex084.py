dados = []
pessoas = []
maior = float('-inf')
menor = float('inf')
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()
    cont = input('Desejá continuar?: ')
    if cont in 'Nn':
        break
print(f'O total de pessoas registradas foi de {len(pessoas)}')
print(f'E o maior peso registrado foi de {maior}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end='')
print()
print(f'E o menor peso registrado foi de {menor}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end='')
print()