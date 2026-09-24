pessoas = list()
while True:
    pessoa = {}
    pessoa['Nome'] = input('Nome: ').capitalize()
    pessoa['Sexo'] = input('Sexo [M/F]: ').capitalize()
    if pessoa['Sexo'] not in 'MmFf':
        while pessoa['Sexo'] not in 'MmFf':
            pessoa['Sexo'] = input('Invalido.Sexo [M/F]: ').capitalize()
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    continuar = input('Quer continuar?: ')
    if continuar[0] not in 'SsNn':
        while continuar[0] not in 'SsNn':
            continuar = input('Invalido.Quer continuar? [Sim/Não]: ')
    if continuar in 'Nn':
        break
contador_de_pessoas = 0
idade_de_todas_as_pessoas = 0
for pessoa in pessoas:
    contador_de_pessoas += 1
    idade_de_todas_as_pessoas += pessoa['Idade']
media_de_idade_das_pessoas = idade_de_todas_as_pessoas / contador_de_pessoas
print(f'''-Foram cadastradas um total de {contador_de_pessoas} de pessoas
-A média de idade das pessoas é {media_de_idade_das_pessoas:.2f}''')
print('-E as mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['Sexo'] in 'Ff':
        print(f'{pessoa['Nome']} ', end= ' ')
print()
print('-E essa é a lista de pessoas acima da média de idade')
print()
for pessoa in pessoas:
    if pessoa['Idade'] > media_de_idade_das_pessoas:
        print(f'Nome {pessoa['Nome']} do sexo {pessoa['Sexo']} com idade de {pessoa['Idade']}')
        print()
