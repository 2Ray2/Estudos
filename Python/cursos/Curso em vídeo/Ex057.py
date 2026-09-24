sexo = 'A'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ').upper())
    if sexo != 'M' and sexo != 'F':
        print('Opção inexistente. Por favor, tente novamente!')
print('FIM!')