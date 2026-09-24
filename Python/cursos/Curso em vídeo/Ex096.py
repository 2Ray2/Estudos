def área(a, b):
    resultado = a * b
    print(f'A área de um terreno {a} x {b} é {resultado:.2f}m²')


def linha():
    print('—' * 30)


linha()
print(f'{"Controle de Terrenos":^30}')
linha()
larugura = float(input('Qual é a largura do terreno?: '))
comprimento = float(input('Qual é o comprimento do terreno?: '))
área(larugura, comprimento)
