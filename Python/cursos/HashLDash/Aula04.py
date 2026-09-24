letras = ['A', 'C',  'F',  'H',  'J']

for i in range(len(letras)):
    print(f'{letras[i]}\n')

#Esse codigo analisa as letras da lista "Letras" e mostra cada uma.

for i in letras:
    print(f'{i}\n')

#Esse codigo faz a mesma coisa que o de cima, muito mais limpo, sendo mais facil de ler.

letras2 = ['B', 'D', 'G', 'I', 'K']

for i in range(len(letras)):
    print(letras[i], letras2[i])

#Esse codigo junta dois valores de ambas as listas.

for i in zip(letras, letras2):
    print(i)

#Agora esse codigo faz a mesma coisa que o anterior sem ser tão complexo quanto, usando apenas uma função 'zip',
#quem junta dois valores de diferentes listas até que uma das listas acabe.

colunas = 5
linhas = 5

acho = False
for linha in range(linhas):
    for coluna in range(colunas):
        if linha == 3 and coluna == 3:
            print('Acho a linha 3 e a coluna 3!')
            acho = True
    if acho == True:
        break

#Nesse codigo temos um for para analisar a linha e outro for para analisar a coluna, mas o problema desse codigo
#é quando achar a 3 linha e a 3 coluna, você tera que fazer uma variavel e depois fazer um if para fechar esse codigo.

for linha, coluna in ((li, co) for li in range(linhas) for co in range(colunas)):
    if linha == 3 and coluna == 3:
        print('Achou a 3 linha e achou a 3 coluna!')
        break

#Esse codigo funciona igual o de cima só que muito mais limpo, e sem precisar criar uma variavel para fecha-lo.

