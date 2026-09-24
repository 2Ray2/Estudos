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
