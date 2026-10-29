

import requests


def buscar_pokemon(nome):
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}")

    if resposta.status_code != 200:
        print("Pokémon não encontrado.")
        return

    dados = resposta.json()

    tipos = [t["type"]["name"] for t in dados["types"]]

    print(f"\nNome: {dados['name']}")
    print(f"Tipos: {', '.join(tipos)}")
    print(f"Altura: {dados['height']}")
    print(f"Peso: {dados['weight']}\n")


if __name__ == "__main__":
    nome = input("Digite o nome do Pokémon: ")
    buscar_pokemon(nome)
