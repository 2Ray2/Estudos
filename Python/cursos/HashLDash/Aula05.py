def fibonacci(num):
    a = -1
    b = 1
    for c in range(num):
        c = a + b
        a = b
        b = c
    return print(f'{c}')

#Esse codigo calcula qual valor está na posição (num), então esse codigo pega um numero, e transforma esse numero em
#uma posição na sequencia de fibonacci. (Esse foi eu que fiz :))

fibonacci(4)


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#Esse codigo faz a mesma coisa que o de cima, só que com uma jogada de mestre, na sequencia de fibonacci, o proximo numero
#é determinado pelo seu ultimo e pelo seu penultimo, exemplo: ultimo = 0 + penultimo = 1 = numero de fibonacci = 2
#com isso o codigo analisa se ('n' a posição do numero) é igual a 1 ou 2, que tem valores simples sendo 1 = 0 e 2 = 1 
#e se não for 1 nem 2 ele vai calcular a fibonacci de n - 2 = ultimo e de n - 1 = penultimo e depois vai somar esses dois valores
#sendo o resultado a fibonacci do numero. Genial!


print(fib(4))