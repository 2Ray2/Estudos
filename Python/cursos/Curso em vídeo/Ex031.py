km = float(input('Quantos quilometros vai ter a sua viagem? '))
if km <= 200:
    preço = km * 0.50
    print('O preço da viagem vai ser de R${:.2f}'.format(preço))
else:
    preço = km * 0.45
    print('O preço da viagem vai ser de R${:.2f}'.format(preço))
