import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"}) #returns a regular python string
data = response.json() #pyhon dict

print(data["joke"])