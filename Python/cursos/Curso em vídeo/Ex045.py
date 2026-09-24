from random import choice
print('=-=' * 10,
      'JOKENPÔ',
      '=-=' * 10)
jokenpo = ['Pedra', 'Papel', 'Tesoura']
comp = choice(jokenpo)
escolha = input('Digite Pedra, Papel ou Tesoura: ').capitalize()
if escolha == 'Pedra' and comp == 'Tesoura':
    print('Parabens você ganhou da maquina ψ(｀∇´)ψ')
elif escolha == 'Papel' and comp == 'Pedra':
    print('Parabens você ganhou da maquina ψ(｀∇´)ψ')
elif escolha == 'Tesoura' and comp == 'Papel':
    print('Parabens você ganhou da maquina ψ(｀∇´)ψ')
elif escolha == 'Pedra' and comp == 'Papel':
    print('Invefizmente você perdeu ＞﹏＜')
elif escolha == 'Papel' and comp == 'Tesoura':
    print('Invefizmente você perdeu ＞﹏＜')
elif escolha == 'Tesoura' and comp == 'Pedra':
    print('Invefizmente você perdeu ＞﹏＜')
elif escolha == comp:
    print('EMPATE')
else:
    print('Resposta incorreta!, tente novamente')
