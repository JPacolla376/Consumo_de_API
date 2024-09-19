#Busca por id específico
import requests

recipe_name = input("Digite o nome da receita que deseja buscar: ").lower()

url = 'https://api-receitas-pi.vercel.app/receitas/todas'

try:
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            
            matching_recipes = [recipe for recipe in data if recipe_name in recipe['nome'].lower()]
            
            if matching_recipes:
                print(f"Receitas encontradas com o nome '{recipe_name}':")
                for recipe in matching_recipes:
                    print(f"- {recipe['nome']} (ID: {recipe['_id']})")
            else:
                print(f"Nenhuma receita encontrada com o nome '{recipe_name}'.")
        
        except ValueError:
            print('Erro ao decodificar JSON.')
    else:
        print('Erro na requisição:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Erro na requisição:', e)
