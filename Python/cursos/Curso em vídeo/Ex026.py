f = input('Digite uma frase: ').upper().strip()
print('''Na sua fras tem {} letras "A"
A primeira vez que ela aparece e na pocição {}
E na ultima vez nha picoção {}'''.format(f.count('A'), f.find('A') + 1, f.rfind('A') + 1))