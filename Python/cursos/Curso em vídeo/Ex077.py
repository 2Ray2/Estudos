palavras = ('APRENDER', 'ESTUDAR', 'AMOR', 'FELICIDADE',
            'ESFORÇO', 'DISPOSIÇÃO', 'DISCIPLINA', 'NASCIMENTO',
            'SAUDADES', 'DIFICULDADES','FUTURO','FAMILIA')
vogais = ['A', 'E', 'I', 'O', 'U']
for palavra in palavras:
    print(f'Na palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=' ')
    print()