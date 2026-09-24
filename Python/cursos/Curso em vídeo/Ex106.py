from colorama import init, Fore, Back, Style
init()
while True:
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + '—' * 40)
    print(f'{"SISTEMA DE AJUDA PYHELP":^40}')
    print('—' * 40)
    funcao = input(Fore.RESET + Back.RESET + 'Função das bibliotecas: ')
    if funcao.lower() in 'fim':
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + '—' * 40)
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + f'{"Fim":^38}')
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + '—' * 40)
        break
    else:
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + '—' * 40)
        print(f'Acessando o manual de comandos do {funcao.capitalize()}')
        print('—' * 40)
        print(help(funcao))