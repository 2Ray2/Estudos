sa = float(input('Digite o seu salario:R$'))
if sa > 1250:
    por = (sa * 10) / 100
    print('Você recebeu um almento de 10% agora seu salario de R${:.2f} é R${:.2f}'.format(sa, sa + por))
if sa <= 1250:
    por = (sa * 15) / 100
    print('Você recebeu um almento de 15% agora seu salario de R${:.2f} é R${:.2f}'.format(sa, sa + por))
