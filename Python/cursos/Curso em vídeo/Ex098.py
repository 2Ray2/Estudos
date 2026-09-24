from time import sleep
def linha():
    print('—' * 40)


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if b > 0:
        for d in range(a, b + c, c):
            print(d, end='  ')
            #sleep(1)
    if b < 0:
        for d in range(b, a + c, c):
            print(d, end='  ')
            #sleep(1)
    if c < 0:
        for d in range(a, b + c, c):
            print(d, end='  ')
            #sleep(1)
    print('FIM!')


linha()
print('Contagem de 1 até 10 em 1 em 1.')
for i in range(1, 11):
    print(i, end='  ')
    #sleep(1)
print('FIM!')
linha()
print('Contagem de 10 até 0 de 2 em 2.')
for c in range(10, -2, -2):
    print(c, end='  ')
    #sleep(1)
print('FIM!')
linha()
print('Agora é a sua vez de personalizar a contagem.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(inicio, fim, passo)