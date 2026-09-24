from calendar import isleap
n = int(input('Digite um ano qualquer: '))
if isleap(n) == True:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')