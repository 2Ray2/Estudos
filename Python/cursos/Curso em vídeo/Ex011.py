altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('''Sua parede tem {}m² de area
a quantidade de tinta usada vai ser de {}l'''.format(area, tinta))
