with open('aula02.txt', 'r') as file:
   txt = file.read()


def leia(txt):
   '''Analisa o texto (txt) e colocar em 'carac' todos os valores que apareceram no texto
   e tambem mostra quantas vezes cada caracter apareceu no texto.'''
   carac = []
   contador = []
   for c in txt:
      if not c in carac:
         carac.append(c)
         contador.append(1)
      else:
         index = carac.index(c)
         contador[index] += 1
   print(f'{carac}\n{contador}')


def leia1(txt):
   '''Analisa o texto (txt) e colocar em 'carac' todos os valores que apareceram no texto
   e tambem mostra quantas vezes cada caracter apareceu no texto.'''

   carac = set()  # o 'set' tamem pode ser representado como cara = {valor1 , valor2, valor3, valor4} muito semelhante a um dicionario.
   
   for c in txt:
      carac.add(c)
   
   list(carac)

   contador = [txt.count(c) for c in carac]

   print(f'letras = {carac}\nQuantidade de cada letra = {contador}')


def leia2(txt):
   '''Analisa o texto (txt) e colocar em 'carac' todos os valores que apareceram no texto
   e tambem mostra quantas vezes cada caracter apareceu no texto.'''

   carac = set(c for c in txt) 
   
   list(carac)

   contador = [txt.count(c) for c in carac]

   print(f'letras = {carac}\nQuantidade de cada letra = {contador}')


def leia3(txt):
   '''Analisa o texto (txt) e colocar em 'carac' todos os valores que apareceram no texto
   e tambem mostra quantas vezes cada caracter apareceu no texto.'''

   return {c: txt.count(c) for c in set(txt)}


print(leia3(txt))