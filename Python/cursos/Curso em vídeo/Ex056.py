total_idade = 0                     # Para armazenar todas as idades
homem_velho = 0                     # Para calcular o homem mais velho
mulher_20 = 0                       # Para calcular quantas mulheres tem idade menor que 20
nome_homem_mais_velho = ''          # Para armazenar o nome do homem mais velho
for i in range(1, 6):
    print('----- {}° PESSOA -----'.format(i + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    total_idade += idade
    sexo = input('Sexo [M/F]: ').upper()
    if i == 1 and sexo == 'M':
        if idade > homem_velho:
            homem_velho = idade
            nome_homem_mais_velho = nome
    if sexo == 'F':
        if idade < 20:
            mulher_20 += 1
media_idade = total_idade / 5       # Calcular a media de idade
print('''A média de idade do grupo é {}
O homem mais velho tem {} anos e se chama {}
E ao todo são {} mulheres menores de 20 anos '''.format(media_idade, homem_velho, nome_homem_mais_velho, mulher_20))
