import requests
import json

""" Get sunrise and sunset times from yahoo weather api"""
BASE_URL = "https://query.yahooapis.com/v1/public/yql"
YAHOO_QUERY = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="cupertino, ca")' 

print(YAHOO_QUERY)

response = requests.get(BASE_URL, 
                        headers = {"Accept": "application/json"}, 
                        params = {"q": YAHOO_QUERY})

data = response.json()
astro = data["query"]["results"]['channel']['astronomy']
for k,v in astro.items():
    print("{} value: {}" .format(k,v))

wind = data["query"]["results"]["channel"]["wind"]
print(wind)
atmos = data["query"]["results"]["channel"]["atmosphere"]
print(atmos)

forecast = data["query"]["results"]["channel"]["item"]["forecast"]

for i in range(len(forecast)):
    print(forecast[i])
