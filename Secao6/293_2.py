import json

string = '''{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": [
    "Frodo",
    "Sam",
    "Gandalf",
    "Legolas",
    "Boromir"
  ],
  "budget": null
}'''

string2json = json.loads(string)
print(string2json)
print(type(string2json))

json2string = json.dumps(string2json)
print(json2string)
print(type(json2string))
