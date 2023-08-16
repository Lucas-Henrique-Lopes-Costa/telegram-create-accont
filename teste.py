import requests

# set the proxy url
proxy_url = 'geo.iproyal.com'
port = '32325'
user = 'leiroz7'
password = 'arvore11_country-ro'

# Realiza a requisição HTTP utilizando o proxy
response = requests.get('http://httpbin.org/ip', proxies=dict(http=f'socks5://{user}:{password}@{proxy_url}:{port}', https=f'socks5://{user}:{password}@{proxy_url}:{port}'))

# Verifica o resultado
if response.status_code == 200:
    print("Requisição bem-sucedida!")
    print(response.text)
else:
    print(f"Erro na requisição. Código de status: {response.status_code}")
