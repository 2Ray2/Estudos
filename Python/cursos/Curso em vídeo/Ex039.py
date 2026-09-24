import datetime
ida = int(input('Digite a sua idade: '))
data = datetime.datetime.now()
ano = data.year
if ida < 18:
    print('Você ainda não precisa se alistar\nVocê devera se alistar em {} ano(s)'.format(ida - 18).replace('-',''))
elif ida == 18:
    print('Está na hora de se alistar!')
else:
    print('Você passou da idade necessaria\nDeveria ter ido {} ano(s) atras'.format(ida - 18))
