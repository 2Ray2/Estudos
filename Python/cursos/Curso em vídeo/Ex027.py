n = input('Digite seu nome: ').strip()
print('''Seu nome completo é {}
Seu primeiro nome é {}
Seu ultimo nome é {}
'''.format(n, n.split()[0], n.split()[-1]))