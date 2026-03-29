import requests

url = "https://rickandmortyapi.com/api/character"

response = requests.get(url)

data = response.json()

print(data)