def ficha(nome, gols):
    print(f'O jogador {nome.capitalize()} fez {gols} gol(s).')


nome = input('Nome do jogador: ')
gols = input('Quantos gols o jogador fez?: ')
if len(gols.replace(' ', '')) == 0 or not gols.isnumeric():
    gols=0
if len(nome.replace(' ', '')) == 0:
    nome = '<desconhecido>'
ficha(nome, gols)
