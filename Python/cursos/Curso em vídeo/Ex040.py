n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a segunda nota '))
n = (n1 + n2) / 2
if n >= 7:
    print('APROVADO, parabens você passou direto!')
elif n >= 5:
    print('RECUPERAÇÃO, você está de recuperação ainda da pra passar')
else:
    print('REPROVADO, você não passou, tente novamente mais tarde')
