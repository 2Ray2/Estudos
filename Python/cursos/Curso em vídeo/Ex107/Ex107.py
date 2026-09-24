import moedas
valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor:.2f} é R${moedas.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${moedas.dobro(valor):.2f}')
print(f'Aumentando seu produto em 10% fica R${moedas.porcem(10, valor) + valor:.2f}')
print(f'Aumentando seu produto em 13% fica R${moedas.porcem(13, valor) + valor:.2f}')