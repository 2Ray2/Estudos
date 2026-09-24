import requests
import os
from dotenv import load_dotenv # função responsavel por ler o arquivo .env com a key da API.

load_dotenv()

token = os.getenv('RESTCOUNTRIES_TOKEN') # pegando a key sem deixar exposta.

url = 'https://api.restcountries.com/countries/v5'

def getdados(country):

    try:
        response = requests.get(
            url, 
            params= {'q': f'{country}'}, # parametros para a busca.
            headers= {'Authorization': f'Bearer {token}'} # parte responsavel pela verificação da key.
        )

        response.raise_for_status()

        data = response.json()

        if len(data['data']['objects']) > 0:
            return data

        else:
            print("País não encontrado.")
            return None
        
    except requests.exceptions.JSONDecodeError:
        print("A API respondeu, mas o conteúdo não é um JSON válido.")
        return None

    except requests.exceptions.ConnectionError:
        print("Não foi possível estabelecer conexão com o servidor.")
        return None

    except requests.exceptions.HTTPError as erro:
        if response.status_code == 401:
            print("Token inválido ou não autorizado.")

        elif response.status_code == 404:
            print("Recurso não encontrado.")

        elif response.status_code >= 500:
            print("O servidor da API apresentou um problema.")

        else:
            print(f"O servidor retornou um erro HTTP: {erro}")

    except requests.exceptions.Timeout:
        print("A requisição demorou demais para responder.")
        return None


def findcountry():
    country = input('Digite o nome do pais: ').strip().lower()

    data = getdados(country)

    if data is None:
        return

    pais = data['data']['objects'][0]['names']['common']

    capital = data['data']['objects'][0]['capitals'][0]['name']

    continente = data['data']['objects'][0]['subregion']

    populacao = data['data']['objects'][0]['population']

    moeda = data['data']['objects'][0]['currencies'][0]['name']

    idiomas = [t['name'] for t in data['data']['objects'][0]['languages']]

    fronteiras = [t for t in data['data']['objects'][0]['borders']]

    dic = {'País': pais,
           'capital': capital,
           'continente': continente,
           'populacao': populacao,
           'moeda': moeda,
           'idiomas': idiomas,
           'fronteiras': fronteiras}

    return dic

print(findcountry())