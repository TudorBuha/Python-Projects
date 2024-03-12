from domain.Taxi import *
from repository.TaxiRepo import *

class TaxiUI:
    def __init__(self, taxi_service):
        self.taxi_service = taxi_service

    def start(self):
        while True:
            print("\nTaxi Simulator:")
            print("1. Request a taxi")
            print("2. Simulate a ride")
            print("3. Display taxi status")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                self.request_taxi()
            elif choice == '2':
                self.taxi_service.simulate_ride()
            elif choice == '3':
                self.taxi_service.display_taxi_status()
            elif choice == '4':
                print("Exiting Taxi Simulator. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def request_taxi(self):
        try:
            #if coordinates are bigger then 100 or smaller than 0, then the ride cannot be added

            start_x = int(input("Enter start point x-coordinate (0-100): "))
            start_y = int(input("Enter start point y-coordinate (0-100): "))
            end_x = int(input("Enter end point x-coordinate (0-100): "))
            end_y = int(input("Enter end point y-coordinate (0-100): "))

            if start_x > 100 or start_x < 0 or start_y > 100 or start_y < 0 or end_x > 100 or end_x < 0 or end_y > 100 or end_y < 0:
                print("Ride cannot be added. Coordinates out of range.")
                return

        except ValueError:
            print("Invalid input. Please enter valid coordinates.")
            return


        start_location = Location(start_x, start_y)
        end_location = Location(end_x, end_y)

        self.taxi_service.add_ride(start_location, end_location)