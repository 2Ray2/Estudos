matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = valores_terceira_coluna = valor_segunda_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Digite um valor para adicionar a matriz [{linha}, {coluna}]: '))
        matriz[linha][coluna] = n
        print(matriz)
print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linhas in range(0, 3):
    for colunas in range(0, 3):
        if matriz[linhas][colunas] % 2 == 0:
            pares += matriz[linhas][colunas]
        if colunas == 2:
            valores_terceira_coluna += matriz[linhas][colunas]
        if linhas == 1:
            if matriz[linhas][colunas] > valor_segunda_linha:
                valor_segunda_linha = matriz[linhas][colunas]
print(f'A soma de todos os valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {valores_terceira_coluna}')
print(f'O maior valor da segunda linha é {valor_segunda_linha}')
