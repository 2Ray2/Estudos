tupla = ('zero', 'Um', 'Dois', 'Três', 'Quatro',
         'Cinco', 'Seis', 'Sete', 'Oito',
         'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
         'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
         'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente.Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {tupla[n]}')