valor = float(input('Digite o valor do produto:R$'))
forma = int(input('''Qual vai ser a forma de pagamento
[ 1 ] Á vista em cheque:10% de desconto
[ 2 ] Á vista no cartão:5% de desconto
[ 3 ] Até 2x no cartão:preço normal
[ 4 ] Até 4x no cartão:juros de 20%
'''))
if forma == 1:
    preco = valor - (valor * 10) / 100
    print('O valor do produto vai ser R${:.2f}'.format(preco))
elif forma == 2:
    preco = (valor * 5) / 100
    print('O valor do produto vai ser R${:.2f}'.format(preco))
elif forma == 3:
    par = int(input('Digite quantas pacelas voce deseja: '))
    valor = valor / par
    print('O valor das parcelas vai ser de R${:.2f}'.format(valor))
elif forma == 4:
    par = int(input('Digite quantas parcelas voce deseja: '))
    preco = (valor * 20) / 100
    valor = preco / par
    print('O valor das parcelas vai ser de R${:.2f}'.format(valor))
else:
    print('O meio de pagamento não cadastrado por favor tente novamente!')
