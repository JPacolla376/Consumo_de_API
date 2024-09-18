#Requisição em teste
import requests


ingredients_input = input("Digite os ingredientes separados por vírgula (ex: cenoura, açúcar, óleo...): ")

#Divide os ingredientes inseridos em uma lista e remove espaços extras
ingredients = [ingredient.strip().lower() for ingredient in ingredients_input.split(',')]

# URL para buscar todas as receitas
url = 'https://api-receitas-pi.vercel.app/receitas/todas'

try:
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            
            print("Conteúdo do JSON recebido:")
            print(data)

            matching_recipes = []
            for recipe in data:
                recipe_ingredients = [ingredient.lower() for ingredient in recipe.get('ingredientes', [])]
                if any(ingredient in recipe_ingredients for ingredient in ingredients):
                    matching_recipes.append(recipe)
            
            if matching_recipes:
                print(f"Receitas encontradas com pelo menos um dos ingredientes: {', '.join(ingredients)}")
                for recipe in matching_recipes:
                    print(f"- {recipe['nome']} (ID: {recipe['_id']})")
            else:
                print(f"Nenhuma receita encontrada com os ingredientes: {', '.join(ingredients)}.")
        
        except ValueError:
            print('Erro ao decodificar JSON.')
    else:
        print('Erro na requisição:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Erro na requisição:', e)
