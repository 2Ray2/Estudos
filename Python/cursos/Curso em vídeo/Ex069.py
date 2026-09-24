homems = maiores = mulheres = 0
while True:
    print('—' * 20)
    print('Cadastre uma pessoa')
    print('—' * 20)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()[0]
    while sexo != 'M' and sexo != 'F':
        if sexo != 'M' or 'F':
            sexo = input('Sexo [M/F]: ').upper()[0]
    if sexo == 'M':
        homems += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if idade >= 18:
        maiores += 1
    continuar = input('Você que continuar? [N/S]: ').upper().split()[0]
    if continuar == 'N':
        break
print('—' * 20)
print(f'''O total de pessoas com mais de 18 anos são :{maiores}
Ao todo temos {homems} homems cadastrados 
E temos {mulheres} mulheres maiores de 20 anos''')
