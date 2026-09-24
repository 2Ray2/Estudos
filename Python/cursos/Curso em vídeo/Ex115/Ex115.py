from bibliotecas import validação

while True:

    validação.titulo('-', 'MENU PRINCIPAL')

    print('\033[33m1\033[0m - \033[34mVer pessoas cadastradas.\033[0m ')
    print('\033[33m2\033[0m - \033[34mCadastrar nova pessoa.\033[0m ')
    print('\033[33m3\033[0m - \033[34mSair do sistema.\033[0m ')
    print('-' * 42)

    opcao = validação.verificar([1, 2, 3], ipt='\033[32mSua opção?:\033[0m ')

    if opcao == 1:
        validação.titulo('-', 'PESSOAS CADASTRADAS')
        validação.tabela()

    elif opcao == 2:
        validação.titulo('-', 'CADASTRO DE PESSOA')
        validação.cadastro()

    else:
        validação.titulo('-', 'SAINDO DO PROGRAMA')
        print('Volte sempre!')
        exit()
