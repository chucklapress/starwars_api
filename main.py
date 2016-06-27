import requests

url = "http://swapi.co/api/people/"
response = requests.get(url).json()
while response['next']:
    for people in response['results']:
        print(people['name'])
    url = response["next"]
    response = requests.get(url).json()

    
