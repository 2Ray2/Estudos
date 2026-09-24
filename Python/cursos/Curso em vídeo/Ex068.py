from random import randint
vitoria = 0
while True:
    print('—' * 25)
    print('Vamos jogar par ou impar')
    print('—' * 25)
    n = int(input('Digite um valor: '))
    jogador = input('Par ou impar?[P/I]: ').upper()[0]
    maquina = randint(0, 10)
    soma = n + maquina
    if jogador == 'P' and soma % 2 == 0:
        print('''Você VENCEU !
Vamos joga novamente...''')
        print(f'A maquina escoleu {maquina} e você {n}')
        vitoria += 1
    elif jogador == 'I' and soma % 2 == 1:
        print('''Você VENCEU !
Vamos joga novamente...''')
        print(f'A maquina escoleu {maquina} e você {n}')
        vitoria += 1
    else:
        print(f'A maquina escoleu {maquina} e você {n}')
        print(f'''Voce PEDEU !
GAME OVER ! Você venceu {vitoria} vezes.''')
        break