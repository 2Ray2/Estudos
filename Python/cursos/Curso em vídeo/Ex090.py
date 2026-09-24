aluno = {'nome': input('Qual é o nome do aluno?: '), 'média': float(input(f'Qual é a média do {aluno}: '))}
print(f'''O nome do aluno é {aluno["nome"]}
Sua média é {aluno["média"]}''')
if aluno["média"] >= 7:
    print('Sua situação é APROVADO')
elif aluno["média"] >= 5:
    print('Sua situação é RECUPERAÇÃO')
else:
    print('Sua situação é REPROVADO')
