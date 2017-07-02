import requests

url = "http://dbpedia.org/resource/Category:Municipal_seats_of Denmark"
seats = requests.get(url, headers={'Accept': 'application/json'}).json()

print(seats)

