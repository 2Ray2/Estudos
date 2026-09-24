n = 0
produtos = ['Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mocila', 120.32, 'Canetas', 22.30, 'Livro', 34.90]
print('—' * 50)
print(f'{'Listagem de Produtos':^48}')
print('—' * 50)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='R$')
    else:
        print(f'{produtos[i]:>7.2f}')
print('—' * 50)