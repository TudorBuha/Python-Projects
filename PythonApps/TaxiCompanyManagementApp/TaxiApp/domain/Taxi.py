import random

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Taxi:
    def __init__(self, taxi_id, location = None):
        self.taxi_id = taxi_id
        #location is random if there is no location already given
        self.location = location if location else Location(random.randint(1, 100), random.randint(1, 100))
        self.is_available = True
        self.total_fare = 0

    def update_location(self, new_location):
        self.location = new_location

    def set_available(self, status=True):
        self.is_available = status

    def calculate_distance(self, destination):
        return abs(self.location.x - destination.x) + abs(self.location.y - destination.y)

    def __str__(self):
        return f"Taxi ID: {self.taxi_id}, Location: ({self.location.x}, {self.location.y}), Total Fare: {self.total_fare}"

