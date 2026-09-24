def escreva(palavra):
    contador = 0
    for letra in palavra:
        contador += 2
    print('—' * contador)
    print(f'{palavra:^{contador}}')
    print('—' * contador)


palavra = input('Digite uma palavra: ')
escreva(palavra)