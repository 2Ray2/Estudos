expre = str(input('Digite sua expressão: '))
pilha1 = 0
pilha2 = 0
for caracter in expre:
    if caracter == '(':
        pilha1 += 1
    elif caracter == ')':
        pilha2 += 1
print(pilha1, pilha2)
if pilha1 == pilha2 and '('[0] in expre:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida!')
print(expre[0])