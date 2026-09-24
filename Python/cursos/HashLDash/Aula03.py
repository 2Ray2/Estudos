a = [c for c in range(300_000_000)]

for i in range(a):

   print(i)

# Com esse codigo, a maquina cria uma valor muito grande, que pode travar a maquina de que executalo.

a = (c for c in range(300_000_000))

for i in a:

    print(i)

# Mas se usarmos o () ao invez de [] criamos um gerador que gera um valor e dascarta os anteriores e os sucessores
# sem prejudicar o desenpenho da maquina de quem executa-lo.
#---------------------------------------------------------------------
letras = ['Abc', 'Def', 'Ghi', 'JKl', 'Mno', 'Pqr', 'Stu', 'Vwx','Yz'] * 50_000_000
#---------------------------------------------------------------------

def lerletras():
    resultado = []
    for letra in letras:
       if letra.startswith('A', 'G' 'V'):
           resultado.append(letra)
       return resultado
    

#Esse codigo tem o mesmo problema que o primeiro, quando lidamos com um numero muito grande de informações
#o uso de memoria do computador é muito grande, isso causa o travamento do computador.

def lerletras2():
    
    for letra in letras:
        if letra.startswith('A', 'G', 'V'):
            yield letra


for letra in lerletras2():
    print(letra)


#Com o metodo yield ele retorna apenas um valor ignorando os anteriores e os sucessores, deixando o codigo mais leve
#e mais rapido.