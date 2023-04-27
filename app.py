#!/usr/bin/env python3
import requests

print('WELCOME TO THE NEWEST STARWARS API USER BASE')

choice = int(input('Type (1) for a list of StarWars Universe characters, or: type (2)for a list of starshipsClasses from the movies '))
if choice == 1:
    print('STARWARS CHARACTERS')
    url = "http://swapi.dev/api/people/"
    response = requests.get(url).json()
    while response['next']:
        for people in response['results']:
            print(people['name'])
        url = response["next"]
        response = requests.get(url).json()
elif choice == 2:
    print('STARWARS SPACESHIPS')
    url = "http://swapi.dev/api/starships/"
    response = requests.get(url).json()
    while response['next']:
        for starship in response['results']:
            print(starship['name'])
        url = response["next"]
        response = requests.get(url).json()

choice = int(input('Type (1) for a list of species droid, humanoid other, or; type (2) to list the vehicles from the movies ' ))
if choice == 1:
    print('STARWARS SPECIES')
    url = "http://swapi.dev/api/species/"
    response = requests.get(url).json()
    while response['next']:
        for species in response['results']:
            print(species['name'])
        url = response["next"]
        response = requests.get(url).json()
elif choice == 2:
    print('STARWARS VEHICLES')
    url = "http://swapi.dev/api/vehicles/"
    response = requests.get(url).json()
    while response['next']:
        for vehicle in response['results']:
            print(vehicle['name'])
        url = response["next"]
        response = requests.get(url).json()

choice = int(input('Type(1)for a list of titles of the StarWars movies  or type (2) to exit '))
if choice == 1:
    print('STARWARS MOVIES')
    url = "http://swapi.dev/api/films"
    response = requests.get(url).json()
    for film in response['results']:
        print(film['title'])
elif choice ==2:
    exit()
choice = int(input('Type(1)for details about Darth Vader  or type (2) for details about AT-AT vehicle  or type (3) for details about the movie Return of the Jedi enter (4)to exit '))
if choice == 1:
    print('LISTING DETAILS DARTH VADER')
    url = "http://swapi.dev/api/people/4"
    response = requests.get(url).json()
    print(response)

if choice == 2:
    print('LISTING DETAILS FOR AT-AT')
    url = "http://swapi.dev/api/vehicles/18"
    response = requests.get(url).json()
    print(response)

if choice == 3:
    print('LISTING DETAIL FOR RETURN OF THE JEDI')
    url = "http://swapi.dev/api/films/3"
    response = requests.get(url).json()
    print(response)

elif choice ==4:
    exit()
