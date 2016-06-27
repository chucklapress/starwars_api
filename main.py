import requests

url = "http://swapi.co/api/people/"
response = requests.get(url).json()
while response['next']:
    for people in response['results']:
        print(people['name'])
    url = response["next"]
    response = requests.get(url).json()

url = "http://swapi.co/api/planets/"
response = requests.get(url).json()
while response['next']:
    for planet in response['results']:
        print(planet['name'])
    url = response["next"]
    response = requests.get(url).json()

url = "http://swapi.co/api/films"
response = requests.get(url).json()
for film in response['results']:
    print(film['title'])

url = "http://swapi.co/api/vehicles/"
response = requests.get(url).json()
while response['next']:
    for vehicle in response['results']:
        print(vehicle['name'])
    url = response["next"]
    response = requests.get(url).json()

url = "http://swapi.co/api/starships/"
response = requests.get(url).json()
while response['next']:
    for starship in response['results']:
        print(starship['name'])
    url = response["next"]
    response = requests.get(url).json()

url = "http://swapi.co/api/species/"
response = requests.get(url).json()
while response['next']:
    for species in response['results']:
        print(species['name'])
    url = response["next"]
    response = requests.get(url).json()
