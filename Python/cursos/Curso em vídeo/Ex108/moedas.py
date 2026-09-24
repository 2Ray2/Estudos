def metade(x):
    """
    param x: Transforma o valor (x) em sua metade.
    return: Valor pela metade.
    """
    x /= 2
    return format(f'R${x}')


def dobro(x):
    """
    param x: Dobra o valor (x).
    retunt: O dobro de (x) formatado em real (R$).
    """
    x *= 2
    return format(f'R${x}')


def porcem(x, y):
    """
    param x: Porcentagem a ser calculado.
    param y: Valor a descobrir a porcentagem.
    return: Valor (y) mais a porcentagem (x).
    """
    z = ((x / 100) * y) + y
    return format(f'R${z}')


def formatar(x):
    """
    return: Retorna o valor (x) formatado em real (R$).
    """
    return format(f'R${x}')
