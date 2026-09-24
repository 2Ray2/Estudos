from  time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    sleep(1)
    opcao = int(input('''O que você quer fazer com esses numeros?
     [ 1 ] Somar
     [ 2 ] Multiplicar
     [ 3 ] Maior
     [ 4 ] Novos numeros
     [ 5 ] Sair do programa
>>>>>>> '''))
    if opcao == 1:
        soma = n1 + n2
        print('Essa é a soma dos numeros {}'.format(soma))
        sleep(1)
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação dos numeros {} e {} resulta em {}'.format(n1, n2, multiplicacao))
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print('O numero {} é maior que o numero {}'.format(n1, n2))
        else:
            print('O numero {} é maior que o numero {}'.format(n2, n1))
        sleep(1)
    elif opcao == 4:
        n1 = int(input('Digite os novos valores: '))
        n2 = int(input('Digite os novos valores: '))
        sleep(0.5)
    elif opcao == 5:
        print('Finalizando o programa')
        sleep(1)
        print('Programa finalizado, volte sempre!')
    else:
        print('Opção invalida tente novamente')
