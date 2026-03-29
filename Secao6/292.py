import json
from pprint import pprint

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''


movie = json.loads(string_json) #Pego algo que não é Json e transformo em Json

pprint(movie)
print(type(movie))
print()

movie_dump = json.dumps(movie,ensure_ascii=False,indent=2) #Pego algo que é json e transformo pra python
print(movie_dump)
print(type(movie_dump))