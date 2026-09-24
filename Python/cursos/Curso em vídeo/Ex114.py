import requests
try:
    site = input('Digite a URL do site: ')
    url = requests.get(site)
    if url.status_code == 200:
        print(f'\033[32mConsegui acessar com sucesso o site \n"{site}"\033[0m')
    else:
        print(f'\033[31mNão consegui acessar o site {site}\033[0m')
except Exception:
    print(f'\033[31mNão consegui acessar o site \n"{site}"\033[0m')
    