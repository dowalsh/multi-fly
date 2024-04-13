class ItinerarySet:
    def __init__(self):
        self.itineraries = []

    def add_itinerary(self, itinerary):
        self.itineraries.append(itinerary)

    def remove_itinerary(self, itinerary):
        self.itineraries.remove(itinerary)

    def get_all_itineraries(self):
        return self.itineraries

    def clear_all_itineraries(self):
        self.itineraries = []

    def get_cheapest_itinerary(self):
        if not self.itineraries:
            return None
        cheapest_itinerary = min(self.itineraries, key=lambda itinerary: itinerary.get_total_cost())
        return cheapest_itinerary
    
    def __iter__(self):
        return iter(self.itineraries)