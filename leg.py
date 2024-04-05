class Leg:
    def __init__(self, departure_airport, arrival_airport, departure_time, arrival_time, duration):
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.duration = duration

    def __str__(self):
        return f"Departure Airport: {self.departure_airport}\nArrival Airport: {self.arrival_airport}\nDeparture Time: {self.departure_time}\nArrival Time: {self.arrival_time}\nDuration: {self.duration}\n"
