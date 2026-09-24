lista = []
rep = '_'
while rep not in 'Nn':
    lista.append(input('Digite um valor: '))
    rep = input('Você deseja continuar digitando?: ')
    if rep in 'Nn':
        break
    elif rep in 'Ss':
        continue
    else:
        while rep not in 'SsNn':
            rep = input('Opção incorreta.Você deseja continuar digitando?:' )
            if rep in 'Nn':
                break
            elif rep in 'Ss':
                continue
lista_decrescente = sorted(lista, reverse=True)
print(f'''Essa é sua lisata {lista}
Essa é sua lista ordenada em decrecência {lista_decrescente}
E na sua lisata tem {len(lista)} numeros''')
if 5 in lista:
    print('E na sua lista há sim o numero 5')
else:
    print('Na sua lista não tem o numero 5')
