jogador = {'Gols': [], 'Nome': input('Qual é o nome do jogador?: '),
           'Partidas': int(input(f'Quantas partidas o jogador jogou?: '))}
for i in range(0, jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Quantos Gols o jogador fez na {i}° partida?: ')))
print(f'''O jogador {jogador['Nome']} jogou {jogador['Partidas']} jogo''')
for c in range(0, jogador['Partidas']):
    print(f'''=> Na partida {c} ele fez {jogador['Gols'][c]} gols''')
print(f'E fez um total de {sum(jogador['Gols'])} gols')
