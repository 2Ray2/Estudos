n = int(input('Digite o valor em metros: '))
print('''Convertendo metros {}m 
em km fica {}km 
em hectómetro {}hm
em decâmetro {}dam
em decimetro {}dm
em centimetro {}cm
em milímetro {}mm'''
      .format(n, n / 1000, n / 100, n / 10, n * 10, n * 100, n * 1000))
