import requests

url = "http://swapi.co/api/people/"
response = requests.get(url).json()
for people in response['results']:
    print(people['name'])
