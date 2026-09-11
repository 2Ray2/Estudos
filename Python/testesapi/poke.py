import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"

response = requests.get(url)

data = response.json()

pokemons = data['results']

name = input('Digite o nome do Pokemon: ')

def findpokemon(name):
    find = False

    for pokemon in pokemons:
        if name == pokemon['name']:
            find = True

            response = requests.get(pokemon['url'])

            data = response.json()   

            name = data['name']

            altura = data['height']

            peso = data['weight']

            tipos = [t['type']['name'] for t in data['types']]

            habilidades = [t['ability']['name'] for t in data['abilities']]

            hp = data['stats'][0]['base_stat']

            ataque = data['stats'][1]['base_stat']

            defesa = data['stats'][2]['base_stat']

            dic = {'name': name, 
                   'altura': altura,
                   'peso': peso, 
                   'tipos': tipos,
                   'habilidades': habilidades,
                   'hp': hp,
                   'ataque': ataque,
                   'defesa': defesa}

            return dic

    if find == False:
        print('Pokemon não encontrado.')
