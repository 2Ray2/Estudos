def leiaint(num):
    """
    Analisa se um valor é inteiro (int).
    param num: Valor a ser analisado.
    retun: Retorna o valor transformado em inteiro (int).
    """
    try:
        while True:
            inteiro = input(num).replace(' ', '')

            if len(inteiro) == 0:
                print('ERRO!\033[31mVocê não digitou nada!\033[0m')
                continue

            if inteiro.isalpha():
                print('ERRO!\033[31mVocê digitou letras!\033[0m')
                continue

            else:
                try:
                    return int(inteiro)
                    break

                except:
                    print('ERRO!\033[31mVocê digitou um numero, mas não inteiro.\033[0m')
                    continue

    except KeyboardInterrupt:
        print()
        print('\033[31mO usuario decidio não digitar esse numero.\033[0m')
        inteiro = 0
        return inteiro


def leiafloat(num):
    """
    Analisa se um valor é real (float).
    param num: Valor a ser analisado.
    return: Valor transformado em real (float).
    """
    try:
        while True:
            real = input(num).replace(' ', '').replace(',', '.')

            if len(real) == 0:
                print('ERRO!\033[31mVocê não digitou nada!\033[0m')
                continue

            if real.isalpha():
                print('ERRO!\033[31mVocê digitou letras!\033[0m')
                continue

            else:
                return float(real)
                break

    except KeyboardInterrupt:
        print()
        print('\033[31mO usuario decidio não digitar esse numero.\033[0m')
        real = 0
        return real
