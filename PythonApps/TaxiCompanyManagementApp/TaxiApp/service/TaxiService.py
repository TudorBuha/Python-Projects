from domain.Taxi import *
import random

class TaxiService:
    def __init__(self, taxi_repository):
        self.taxi_repository = taxi_repository


    def add_ride(self, start_location, end_location):
        try:
            start_x, start_y = start_location.x, start_location.y
            #if end location is already occupied by a taxi, then the ride cannot be added???
            for taxi in self.taxi_repository.get_all_taxis():
                if taxi.location.x == end_location.x and taxi.location.y == end_location.y:
                    print("Ride cannot be added. Taxi already at end location.")
                    return
            end_x, end_y = end_location.x, end_location.y
        except AttributeError:
            print("Invalid input. Please enter valid coordinates.")
            return

        start_location = Location(start_x, start_y)
        end_location = Location(end_x, end_y)

        closest_taxi = min(self.taxi_repository.get_all_taxis(), key=lambda taxi: taxi.calculate_distance(start_location))
        distance = closest_taxi.calculate_distance(end_location)

        closest_taxi.total_fare += distance
        closest_taxi.update_location(end_location)
        closest_taxi.set_available(False)

        # pppdate taxi details after the ride
        self.taxi_repository.update_taxi(closest_taxi)


    def simulate_ride(self):
        start_point = Location(random.randint(1, 100), random.randint(1, 100))
        end_point = Location(random.randint(1, 100), random.randint(1, 100))

        while abs(start_point.x - end_point.x) + abs(start_point.y - end_point.y) < 5:
            end_point = Location(random.randint(1, 100), random.randint(1, 100))

        self.add_ride(start_point, end_point)

    def display_taxi_status(self):
        taxis = self.taxi_repository.get_all_taxis()
        sorted_taxis = sorted(taxis, key=lambda taxi: taxi.total_fare, reverse=True)

        for taxi in sorted_taxis:
            print(f"Taxi ID: {taxi.taxi_id}, Location: ({taxi.location.x}, {taxi.location.y}), Total Fare: {taxi.total_fare}")
