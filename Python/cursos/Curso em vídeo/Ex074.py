from random import randint
tupla = [randint(1, 10) for i in range(5)]
numeros = sorted(tupla, reverse=True)
print(f'''Os valores sorteados são os {tupla}
O maior numero da ordem é o {numeros[0]}
E o menor é o {numeros[3]}''')