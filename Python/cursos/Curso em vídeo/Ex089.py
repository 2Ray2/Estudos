alunos = []
media = contador = 0
aluno = []
while True:
    nome = input('Nome: ').capitalize()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    contador += 1
    continuar = input('Quer continuar?: ')
    if continuar in 'Nn':
        break
print('—' * 30)
print('Número     Nome     Média')
print('—' * 30)
for c in range(contador):
    print(f'{c:<10}{alunos[c][0]:>5}{alunos[c][3]:>8}')
print('—' * 30)
while True:
    mostrar = int(input('Voce quer ver a nota de qual aluno? (Digite 999 para parar): '))
    if mostrar == 999:
        break
    else:
        print(f'As notas de {alunos[mostrar][0]} são {alunos[mostrar][1], alunos[mostrar][2]}'
              .replace('(', '').replace(')', ''))
