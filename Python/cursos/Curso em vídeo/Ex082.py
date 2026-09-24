par = []
impar = []
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    n = input('Você deseja continuar digitando valores?: ')
    if n in 'Nn':
        break
for i in lista:
    if i % 2 == 0:
        par += [i]
    else:
        impar += [i]
print('-' * 30)
print(f'''Está é sua lista {lista}
Está é sua listar só com os numeros pares {par}
E está é so com o impares {impar}''')