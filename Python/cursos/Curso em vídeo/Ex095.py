jogadores = []
while True:
    jogador = {}
    jogador['Gols'] = []
    jogador['Nome'] = str(input('Qual é o nome do jogador?: '))
    jogador['Partidas'] = int(input('Quantas partidas o jogador jogou?: '))
    for i in range(1, jogador['Partidas'] + 1):
        jogador['Gols'].append(int(input(f'Quantos gols o jogador fez na {i}° partida?: ')))
    continuar = input('Quer adicionar mais algum jogador?: ')
    jogadores.append(jogador)
    if continuar[0] not in 'SsNn':
        while continuar[0] not in 'SsNn':
            print('Resposta invalida.', end='')
            continuar = input('Quer adicionar mais algum jogador?: ')
    if continuar[0] in 'Nn':
        break
print('—' * 60)
print(f'{"Cod ":<3}' f'{"Nome":<20}' f'{"Gols":<22}' f'{"Total":<25}')
print('—' * 60)
contador = 0
for jogador in jogadores:
    print(f'{contador:>3} ' f'{jogador['Nome']:<20}' f'{str(jogador['Gols']):<24}' f'{sum(jogador['Gols']):<20}')
    contador += 1
print('—' * 60)
while True:
    mostrar = int(input('Quer ver os dados de qual jogador? (999 para parar): '))
    if mostrar == 999:
        break
    elif mostrar < 0 or mostrar > len(jogadores):
        print(f'ERRO! Não existe jogador com o codigo {mostrar}')
    else:
        jogador = jogadores[mostrar]
        print(f'Essa são as informaçoes do jogador {jogador['Nome']}')
        for i, gols in enumerate(jogador['Gols'], start=1):
            print(f'Na {i}° o jogador fez {gols} gols')