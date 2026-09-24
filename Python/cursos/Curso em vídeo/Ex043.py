peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc >= 18.5:
    print('Você está no peso IDEAL!')
elif imc > 25:
    print('Você está em SOBREPESO!')
elif imc > 30:
    print('Você está OBSIDADE')
else:
    print('Você está em OBSIDADE MORBIDA')
