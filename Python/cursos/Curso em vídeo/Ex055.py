maior = float('-inf')
menor = float('inf')
for i in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso lida foi {:.2f}Kg e o menor foi {:.2f}Kg'.format(maior, menor))