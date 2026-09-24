from random import shuffle
a1 = input('Digite o nome do aluno: ').title()
a2 = input('Digite o nome do segundo aluno: ').title()
a3 = input('Digite o nome do terceiro aluno: ').title()
a4 = input('Digite o nome do quarto aluno: ').title()
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de apresentação vai ser {}'.format(alunos))
