def metade(x, form=False):
    """
     param x: Transforma o valor (x) em sua metade.
     param form: Formata o valor para moeda. (opcional)
     return: Valor pela metade.
     """
    x /= 2
    if form is True:
        return format(f'R${x:.2f}').replace('.', ',')
    else:
        return x


def dobro(x, form=False):
    """
    param x: Dobra o valor (x).
    param form: Formata o valor para moeda. (opcional)
    retunt: O dobro de (x) formatado em real (R$).
    """
    x *= 2
    if form is True:
        return format(f'R${x:.2f}').replace('.', ',')
    else:
        return x


def porcem(x, y, form=False):
    """
    param x: Porcentagem a ser calculado.
    param y: Valor a descobrir a porcentagem.
    param form: Formata o valor para moeda. (opcional)
    return: Valor (y) mais a porcentagem (x).
    """
    z = ((x / 100) * y) + y
    if form is True:
        return format(f'R${z:.2f}').replace('.', ',')
    else:
        return z


def formatar(x):
    """
    return: Retorna o valor (x) formatado em real (R$).
    """
    return format(f'R${x:.2f}').replace('.', ',')


def resumo(x, y, z):
    """
    param x: Valor a ser analisado
    param y: Primeiro aumento.
    param z: Segundo aumento.
    """
    print('—' * 40)
    print(f'{"Resumo do valor.":^40}')
    print('—' * 40)
    print(f'Preço analisado:{formatar(x):>10}')
    print(f'Dobro do preço: {dobro(x, True):>10}')
    print(f'Metade do preço:{metade(x, True):>9}')
    print(f'{y}% de aumento:{porcem(y, x, True):>11}')
    print(f'{z}% de aumento:{porcem(z, x, True):>11}')
    print('—' * 40)