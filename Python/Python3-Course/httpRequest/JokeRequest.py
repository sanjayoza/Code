import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

hdr = figlet_format("DAD JOKE")
hdr = colored(hdr, "yellow")
print(hdr)
url = "https://icanhazdadjoke.com/search"
req = input("Please select topic for joke > ")

response = requests.get(url, 
                        headers = {"Accept": "application/json"},
                        params = {"term": req})

data = response.json()

if response.ok:
    totaljokes = data["total_jokes"]
    jokes = data["results"]
    if totaljokes > 1:
        print("I got {} jokes, here is one" .format(totaljokes))
        print(choice(jokes)['joke'])
    elif totaljokes == 1:
        print("I got 1 joke, here it is ")
        print(jokes["joke"])
    else:
        print("Sorry no jokes for {}" .format(req))
else:
    print("request failed status code {}" .format(response.status_code))

#print(response)
#print(data)
#print("status: {}" .format(response.status_code))
#print("total jokes: {}" .format(data["total_jokes"]))