cont = 0
maiores = 0
menores = 0
import datetime
data = datetime.date.today().year
for i in range(1, 8):
    nasci = int(input('Digite a data de nascimento da {} pessoa: '.format(i)))
    cont += 1
    ida = data - nasci
    if ida >= 21:
        maiores += 1
    else:
        menores +=1
print('''Entre todos os {} existem 
{} maiores de idade e {} menores de idade'''.format(cont, maiores, menores))
