print('=-=' * 10)
print('Emprestimo De Casas')
print('=-=' * 10)
valor = float(input('Digite o valor da casa:R$'))
salario = float(input('Digite o seu salario:R$'))
anos = int(input('Digite quantos anos você vai pagar essa casa: '))
prest = valor / (anos * 12)
por = salario * 30 / 100
if prest > por:
    print('O emprestimo foi NEGADO pois passa dos 30% permitido')
else:
    print('O emprestimo foi APROVADO')
