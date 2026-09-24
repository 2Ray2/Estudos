algo = input('Digite algo: ')
print('''
Algo é somente espaços? {}
Algo é um numero? {}
Algo é alfabetico? {}
Algo é alfanumerico? {}
Algo está em maiusculas? {}
Algo está em minusculas? {}
Algo está capitalizado? {}
'''.format(algo.isspace(), algo.isnumeric(),
algo.isalpha(), algo.isalnum(), algo.isupper(), algo.islower(), algo.isprintable()))