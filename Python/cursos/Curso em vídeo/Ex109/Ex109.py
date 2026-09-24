import moedas
valor = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.formatar(valor)} é {moedas.metade(valor, True)}')
print(f'O dobro de {moedas.formatar(valor)} é {moedas.dobro(valor, True)}')
print(f'Aumentando seu produto em 10% fica {moedas.porcem(10, valor, True)}')
print(f'Aumentando seu produto em 13% fica {moedas.porcem(13, valor, True)}')
