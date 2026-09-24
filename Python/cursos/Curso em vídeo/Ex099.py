def maior(* num):
    print('Analisando os valores...')
    print(f'''{numeros} foram informados {len(numeros)} valores ao total.
O maior valor informado foi o {max(numeros)}''')
    print('—' * 40)


lista_de_numeros = []
numeros = []
print('—' * 40)
print(f'{"Cadastro de Valores":^38}')
print('—' * 40)
while True:
    while True:
        numero = int(input('Digite um numero (999 para parrar): '))
        if numero == 999:
            break
        else:
            numeros.append(numero)
    continuar = input('Quer adicionar mais uma lista de numeros?: ')
    if continuar in 'Nn':
        lista_de_numeros.append(numeros[:])
        numeros.clear()
        break
    else:
        lista_de_numeros.append(numeros[:])
        numeros.clear()
print('—' * 40)
for numeros in lista_de_numeros:
    maior(numeros)