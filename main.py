import requests

print('WELCOME TO THE STARWARS API USER BASE')

choice = int(input('Type (1) for a list of StarWars Universe characters, or: type (2)for a list of starshipsClasses from the movies'))
if choice == 1:
    url = "http://swapi.co/api/people/"
    response = requests.get(url).json()
    while response['next']:
        for people in response['results']:
            print(people['name'])
        url = response["next"]
        response = requests.get(url).json()
elif choice == 2:
    url = "http://swapi.co/api/starships/"
    response = requests.get(url).json()
    while response['next']:
        for starship in response['results']:
            print(starship['name'])
        url = response["next"]
        response = requests.get(url).json()

choice = int(input('Type (1) for a list of species droid, humanoid other, or; type (2) to list the vehicles from the movies' ))
if choice == 1:
    url = "http://swapi.co/api/species/"
    response = requests.get(url).json()
    while response['next']:
        for species in response['results']:
            print(species['name'])
        url = response["next"]
        response = requests.get(url).json()
elif choice == 2:
    url = "http://swapi.co/api/vehicles/"
    response = requests.get(url).json()
    while response['next']:
        for vehicle in response['results']:
            print(vehicle['name'])
        url = response["next"]
        response = requests.get(url).json()

choice = int(input('Type(1)for a list of titles of the StarWars movies as they appeared in chronological order or type (2) to exit'))
if choice == 1:
    url = "http://swapi.co/api/films"
    response = requests.get(url).json()
    for film in response['results']:
        print(film['title'])
elif choice ==2:
    exit()
