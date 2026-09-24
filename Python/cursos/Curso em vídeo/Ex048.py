soma = 0
conta = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        conta += 1
        soma += c
print('A soma dos {} é {}'.format(conta, soma))