import requests

url = 'https://api-receitas-pi.vercel.app/receitas/todas'

try:
    response = requests.get(url)
    
    print('Status code:', response.status_code)
    print('Conteúdo bruto:', response.text) 

    if response.status_code == 200:
        try:
            data = response.json()
            print('Dados da API:', data)
        except ValueError:
            print('Erro ao decodificar JSON.')
    else:
        print('Erro na requisição:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Erro na requisição:', e)
