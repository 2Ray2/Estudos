sedula50 = sedula20 = sedula10 = sedula1 = valor = 0
print('==' * 20)
print('{:^40}'.format('CAIXA REGISTRADORA'))
print('==' * 20)
n = int(input('Quanto você quer sacar?:R$'))
if n < 0:
    print('Valor inserido incompativel ')
else:
    while n != valor:
        if valor + 50 <= n:
            valor += 50
            sedula50 += 1
        if valor + 50 > n:
            while valor + 20 <= n:
                valor += 20
                sedula20 += 1
            if valor + 20 > n:
                while valor + 10 <= n:
                    valor += 10
                    sedula10 += 1
                if valor + 10 > n:
                    while valor + 1 <= n:
                        valor += 1
                        sedula1 += 1
print(f'''Total de sedulas de R$50 são {sedula50}
Total de sedulas de R$20 são {sedula20}
Total de sedulas de R$10 são {sedula10}
Total de sedulas de R$1 são {sedula1}''')
