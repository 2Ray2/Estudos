def fatorial(a, show):
    """
    :param a: O numero a ser calculado.
    :param show: Mostrar o processo de calculo. (Opcional)
    :return: O valor fatorial de a
    """
    i = 1
    for c in range(num, 0, -1):
        i *= c
        if show == True:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
    print(i)


num = int(input('Qual é o numero que você deseja saber a fatorial?: '))
mostrar = input('Você quer ver o processo de calculo?: ')
print('—' * 40)
if mostrar not in 'SsNn':
    while mostrar not in 'SsNn':
        mostrar = input('ERRO!Você quer ver o processo de calculo?: ')
if mostrar in 'Ss':
    fatorial(a=num, show=True)
elif mostrar in 'Nn':
    fatorial(a=num, show=False)
print('—' * 40)
help(fatorial)
