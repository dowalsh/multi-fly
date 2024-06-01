import requests
import json
from itinerary import Itinerary
from leg import Leg
from itinerary_set import ItinerarySet
from location import Location
import os


global use_cache
use_cache = True

# read in api key from file
with open('api_key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

base_url = "https://skyscanner80.p.rapidapi.com/api/v1/"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "skyscanner80.p.rapidapi.com"
}

def get_round_trip(fromLocation , toLocation ,departDate, returnDate):

    url = base_url + "flights/search-roundtrip"
    querystring = {"fromId": fromLocation.get_id(),
                   "toId": toLocation.get_id(),
                   "departDate":departDate, # NOTE: THESE NEED TO BE FORMATTED AS YYYY-MM-DD - including 0s where necessary
                   "returnDate":returnDate,  
                   "adults":"1",
                   "currency":"USD",
                   "market":"US",
                   "locale":"en-US"}
    
    # name the file with from and to locations and dates
    filename = f"data/{fromLocation.get_name()}_{toLocation.get_name()}_{departDate}_{returnDate}.json"

    # if filename exists, read from file, else make api call and save to file
    if use_cache and os.path.exists(filename):
        with open(filename, 'r') as file:
            response_json = json.load(file)
    else:
        # print the full url and querystring        
        print(url) 
        print(querystring)
        response = requests.get(url, headers=headers, params=querystring)
        response_json = response.json()
        with open(filename, 'w') as file:
            file.write(json.dumps(response_json, indent=4))
  
    # parse json response into a list of Itinerary objects
    # create an itinerary set
    itineraries = ItinerarySet()
    
    for itinerary in response_json['data']['itineraries']:
        id = itinerary['id']
        price = itinerary['price']['raw']
        legs = []
        for leg in itinerary['legs']:
            departure_airport = leg['origin']['displayCode']
            arrival_airport = leg['destination']['displayCode']
            departure_time = leg['departure']
            arrival_time = leg['arrival']
            duration = leg['durationInMinutes']
            legs.append(Leg(departure_airport, arrival_airport, departure_time, arrival_time, duration))
        itineraries.add_itinerary(Itinerary(id, price, legs))
   

    return itineraries

def get_config():
    flights_api_url = base_url+"get-config"
    response = requests.get(flights_api_url, headers=headers)

    # save json string as beautiful json
    with open('data/get_config.json', 'w') as file:
        file.write(json.dumps(response.json(), indent=4))

def get_airport_ids():
    # a way to get all airports and their corresponding ids...
    # not being used yet...
    # NOTE: doesn't return (ANY) airports...
    url = "https://sky-scanner3.p.rapidapi.com/flights/airports"

    headers = {
	    "x-rapidapi-key": "181827ffb8msh06543a1290959bep1aa22bjsnc4fdf143fc4a",
	    "x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    # save response as beautiful json
    with open('data/airports.json', 'w') as file:
        file.write(json.dumps(response.json(), indent=4))


def main():
    departure_date = "2024-06-02" # NOTE: THESE NEED TO BE FORMATTED AS YYYY-MM-DD - including 0s where necessary
    return_date = "2024-06-08"  

    # create hard coded set of 3 possible destinations
    destinations = [Location("London", "eyJzIjoiTE9ORCIsImUiOiIyNzU0NDAwOCIsImgiOiIyNzU0NDAwOCJ9="), 
                    Location("Prague", "eyJzIjoiUFJHIiwiZSI6Ijk1NjczNTAyIiwiaCI6IjI3NTQ2MDMzIn0="), 
                    Location("Berlin", "eyJzIjoiQkVSIiwiZSI6Ijk1NjczMzgzIiwiaCI6IjI3NTQ3MDUzIn0=")]
    
    homes =  [Location("London", "eyJzIjoiTE9ORCIsImUiOiIyNzU0NDAwOCIsImgiOiIyNzU0NDAwOCJ9="), 
                    Location("Prague", "eyJzIjoiUFJHIiwiZSI6Ijk1NjczNTAyIiwiaCI6IjI3NTQ2MDMzIn0="), 
                    Location("Berlin", "eyJzIjoiQkVSIiwiZSI6Ijk1NjczMzgzIiwiaCI6IjI3NTQ3MDUzIn0=")]

    fromId = "eyJzIjoiTllDQSIsImUiOiIyNzUzNzU0MiIsImgiOiIyNzUzNzU0MiIsInAiOiJDSVRZIn0="
    toId =  "eyJzIjoiTEFYQSIsImUiOiIyNzUzNjIxMSIsImgiOiIyNzUzNjIxMSIsInAiOiJDSVRZIn0="

    #  create dictionary to store ItinerarySet for each combination of home and destination
    itinerary_dict = {}
    for home in homes:
        for destination in destinations:
            # check if home and destination are the same
            if home == destination:
                continue
            itinerary_dict[(home, destination)] = get_round_trip(home,destination,departure_date, return_date)

    # print the cheapest itinerary for each combination of home and destination
    for key, itineraries in itinerary_dict.items():
        cheapest_itinerary = itineraries.get_cheapest_itinerary()
        print(f"{key[0]} -> {key[1]}: {cheapest_itinerary.get_total_cost()}")

    # create dictionary to store ItinerarySet of the cheapest itinerary for each destination
    cheapest_dict = {}
    for destination in destinations:
        # get the cheapest itinerary for each home
        cheapest_itineraries = []
        for home in homes:
            if home == destination:
                continue
            # for each home, get the cheapest itinerary to the destination
            cheapest_itinerary = itinerary_dict[(home, destination)].get_cheapest_itinerary()
            cheapest_itineraries.append(cheapest_itinerary)
        # store these itineraries in the cheapest_dict
        cheapest_dict[destination] = cheapest_itineraries
        
    print("=====================================")
    # print the total cost of the cheapest itineraries for each destination
    for key, itineraries in cheapest_dict.items():
        print(f"Destination: {key}")
        total_cost = sum([itinerary.get_total_cost() for itinerary in itineraries])
        print(total_cost)
        



if __name__ == '__main__':
    main()



# next steps - think about user interface - selecting airports, dates, etc?
# maybe an async solution here makes sense - where 

# would be great to be able to run this somewhat regularly to monitor prices for great deals - maybe a cron job or something?
# perhaps the output could be an email notification.