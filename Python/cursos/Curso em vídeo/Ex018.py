from math import cos, sin, tan, radians
ang = float(input('Qual é o angulo? '))
anr = radians(ang)
print('''seno {:.2f}
cosseno {:.2f}
tangente {:.2f}'''.format(sin(anr), cos(anr), tan(anr)))
