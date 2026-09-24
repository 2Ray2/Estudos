import datetime
anos = int(input('Digite o seu ano de nascimento: '))
data = datetime.datetime.now()
ano = data.year
idade = int(ano) - anos
if idade <= 9:
    print('Você é um nadador(a) MIRIM')
elif idade <=14:
    print('Você é um nadador(a) INFANTIL')
elif idade <= 19:
    print('Você é um nadador(a) JUNIOR')
elif idade <= 20:
    print('Você é um nadador(a) SÊNIOR')
else:
    print('Você é um nadador MASTER')
