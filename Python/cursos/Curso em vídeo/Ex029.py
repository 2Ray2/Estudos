km = int(input('A quantos quilometros o carro estava? '))
if km <= 80:
    print('O carro estava na velocidade permitida')
else:
    preco = (km - 80) * 7
    print('''O carro estava acima da velocidade permitidan\na multa vai ser de R${:.2f}'''.format(preco))
