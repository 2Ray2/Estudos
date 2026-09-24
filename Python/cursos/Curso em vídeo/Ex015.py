d = int(input('Quantos dias você usou o carro? '))
km = float(input('Quantos Km você rodou? '))
va = d * 60 + km * 0.15
print('O total a pagar é R${:.2f}'.format(va))
