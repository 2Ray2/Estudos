no = (input('Digite o seu nome completo: '))
print('''O seu nome completo é {}
Seu nome em minusculas {}
Seu nome em maiusculas {}
Quantas letras tem seu nome {}
E a quantidade de letras que seu primeiro nome tem {}
'''.format(no, no.lower(), no.upper(), len(no.replace(" ", '')), len(no.split()[0])))
