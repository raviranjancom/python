import requests

base_url="https://pokeapi.co/api/v2/pokemon/"

def pokemon_info(name):
    url=base_url+name
    response=requests.get(url)
    if response.status_code == 200:
        pokemon_data=response.json()
        print(pokemon_data)
    else:
        print(f"Unknown Error!")


def main():
    pokemon_info("pikachu")

if __name__=="__main__":
    main()
