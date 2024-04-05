import requests
import json
from itineraries import Itineraries

from leg import Leg

# read in api key from file
with open('api_key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

base_url = "https://skyscanner80.p.rapidapi.com/api/v1/"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

def get_round_trip(departure_date, return_date):
    url = base_url + "flights/search-roundtrip"
    querystring = {"fromId":"eyJzIjoiTllDQSIsImUiOiIyNzUzNzU0MiIsImgiOiIyNzUzNzU0MiIsInAiOiJDSVRZIn0=",
                   "toId":"eyJzIjoiTEFYQSIsImUiOiIyNzUzNjIxMSIsImgiOiIyNzUzNjIxMSIsInAiOiJDSVRZIn0=",
                   "departDate":"2024-05-30", # NOTE: THESE NEED TO BE FORMATTED AS YYYY-MM-DD - including 0s where necessary
                   "returnDate":"2024-06-03",  
                   "adults":"1",
                   "currency":"USD",
                   "market":"US",
                   "locale":"en-US"}

    response = requests.get(url, headers=headers, params=querystring)

    with open('get_round_trip.json', 'w') as file:
        file.write(json.dumps(response.json(), indent=4))

def get_config():
    flights_api_url = base_url+"get-config"
    response = requests.get(flights_api_url, headers=headers)
    # save json string as beautiful json
    with open('get_config.json', 'w') as file:
        file.write(json.dumps(response.json(), indent=4))


def main():
    departure_date = "2024-05-30" # NOTE: THESE NEED TO BE FORMATTED AS YYYY-MM-DD - including 0s where necessary
    return_date = "2024-06-03"  


    get_config()
    get_round_trip(departure_date, return_date)


if __name__ == '__main__':
    main()