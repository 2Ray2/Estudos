n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('A soma de todos os {} numeros é {}'.format(cont, soma))
print('Acabou')