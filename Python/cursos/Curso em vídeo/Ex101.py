import datetime
hoje = datetime.date.today().year


def voto():
    nascimento = int(input('Em que ano você nasceu?: '))
    anos = hoje - nascimento
    if 16 <= anos < 18 or anos >= 70:
        print(f'Com {anos} anos : Voto opcional.')
    elif anos >= 18:
        print(f'Com {anos} anos : Voto obrigatorio.')
    else:
        print(f'Com {anos} anos: Não vota.')


voto()