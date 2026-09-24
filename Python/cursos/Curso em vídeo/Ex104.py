def leiaint(str):
    numero = input(str)
    while not numero.isnumeric():
        numero = input('ERRO!Digite um valor: ')
    print(f'Você digitou o valor {numero}')

numero = leiaint('Digite um valor: ')