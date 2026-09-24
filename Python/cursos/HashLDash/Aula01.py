lista = []
for i in range(1, 11): # Maneira comum
    lista.append(i)
print(lista)

print()

lista1 = [c for c in range(1, 11)] #List comprehensions
print(lista)

print()

lista2 = [v for v in "macaco"] #List comprehensions
print(lista2)

print()

lista3 = [[t for t in range(4)] for e in range(3)]
print(lista3)