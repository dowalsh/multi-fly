import requests
import json

# read in api key from file
with open('api_key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

base_url = "https://skyscanner80.p.rapidapi.com/api/v1/"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

def get_round_trip():
    url = base_url + "flights/search-roundtrip"
    querystring = {"fromId":"eyJzIjoiTllDQSIsImUiOiIyNzUzNzU0MiIsImgiOiIyNzUzNzU0MiIsInAiOiJDSVRZIn0=","toId":"eyJzIjoiTEFYQSIsImUiOiIyNzUzNjIxMSIsImgiOiIyNzUzNjIxMSIsInAiOiJDSVRZIn0=","departDate":"2024-03-11","returnDate":"<REQUIRED>","adults":"1","currency":"USD","market":"US","locale":"en-US"}

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
    print("Hello World")
    get_config()
    get_round_trip()


if __name__ == '__main__':
    main()