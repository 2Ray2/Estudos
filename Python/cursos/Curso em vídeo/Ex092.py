import datetime
ano = datetime.datetime.today().year
dados = {}
dados['Nome'] = input('Qual é o seu nome?: ')
dados['Idade'] = int(input('Em que ano você nasceu?: '))
dados['Ocupação'] = input('Você está trabalhando atualmente?:[Sim/Não] ')
dados['Anos'] = ano - dados['Idade']
if dados['Ocupação'][0] in 'Ss':
    dados['Trabalho'] = input('É quarteira assinada?:[Sim/Não] ')
    if dados['Trabalho'][0] in 'Ss':
        dados['CTPS'] = int(input('Digite sua carteira de trabalho: '))
    else:
        dados['Emprego'] = input('Em que emprego você trabalha?: ')
        dados['CTPS'] = 0
    dados['Salario'] = int(input('Quanto você recebe?: '))
    dados['Data de trabalho'] = int(input('E em que ano você começou a trabalhar?: '))
    dados['Aposentadoria'] = 35 - (ano - dados['Data de trabalho'])
    print('—' * 40)
    print(f'''O seu nome é {dados['Nome']}
Você tem {dados['Anos']} anos de idade
Sua carteira de trabalho é {dados['CTPS']}
Foi contratado em {dados['Data de trabalho']}
Recebe R${dados['Salario']}
E irá se aposentar em {dados['Aposentadoria']} anos''')
else:
    print('—' * 40)
    print(f'''Seu nome é {dados['Nome']}
E tem {dados['Anos']} anos de idade''')