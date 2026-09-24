times = ('Athletico-PR', 'Atlético-GO',	'Atlético-MG', 'Bahia',
         'Botafogo', 'Bragantino', 'Corinthians','Criciúma',
         'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
         'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'São Paulo',
         'Vasco', 'Vitória')
print(f'''Esses são so times {times}
{'—' * 120}
Os cinco primeiros colocados foram os {times[0:6]}
{'—' * 120}
Os últimos 4 colocados {times[-4:]}
{'—' * 70}
Os times em ordem alfabetica é {sorted(times)}
{'—' * 120}
E o Vasco está na {times.index('Vasco')+ 1}ª posição 
{'—' * 35}''')