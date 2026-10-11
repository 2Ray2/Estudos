caracteres = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
    "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

caracteres_shift = [] 
caracteres_shift_pa = []
palavra = input("Digite um palavra: ")
nova_palavra = ""
shift = 7
index = 0

for c in range(7, 62):
    caracteres_shift.append(caracteres[c])

for n in range(0, 7):
    caracteres_shift.append(caracteres[n])

for b in range(0, 62, 2):
    caracteres_shift_pa.append(caracteres_shift[b])

for g in range(1, 62, 2):
    caracteres_shift_pa.append(caracteres_shift[g])

for a in palavra:
    index = caracteres.index(a)
    nova_palavra += f"{caracteres_shift_pa[index]}"

print(nova_palavra)