import requests
import pyfiglet
import termcolor
from random import choice

url = "https://icanhazdadjoke.com/search"

print(termcolor.colored(pyfiglet.figlet_format("Welcome to the DadJoke3000!"), color="red"))

user_input = input(pyfiglet.figlet_format("Choose the topic for your terrible joke"))
#user_limit = int(input("How many jokes would you like to hear?\n"))

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={
        "term": user_input,
    }
    ) #returns a regular python string
data = response.json() #pyhon dict
num_jokes = data["total_jokes"]

if num_jokes > 1:
    print(f"I have got {num_jokes} jokes about {user_input} for ya. Here comes one of them!")
    print(choice(data["results"])['joke'])
elif num_jokes == 1:
    print(f"I have got one joke about {user_input} for ya. Here comes!")
    print(data["results"][0]["joke"])
else:
    print("Sorry buddy, I got nothing on this topic for ya! Please try again")
