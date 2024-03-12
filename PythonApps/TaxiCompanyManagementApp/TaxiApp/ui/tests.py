import unittest
from domain.Taxi import Taxi, Location
from repository.TaxiRepo import TaxiRepository
from service.TaxiService import TaxiService


class TestTaxiService(unittest.TestCase):

    def setUp(self):
        # Setup for each test case
        self.taxi_repository = TaxiRepository(num_taxis=3)  # Adjust the number of taxis as needed
        self.taxi_service = TaxiService(self.taxi_repository)

    def test_add_ride(self):
        # Test the adding a ride functionality

        # Create a taxi with known location
        taxi = Taxi(taxi_id=1, location=Location(0, 0))
        self.taxi_repository.taxis = [taxi]

        # Set up start and end locations
        start_location = Location(20, 10)
        end_location = Location(10, 20)

        # Calculate the Manhattan distance between start and end locations
        expected_fare = abs(end_location.x - start_location.x) + abs(end_location.y - start_location.y)

        # Add the ride
        self.taxi_service.add_ride(start_location, end_location)

        # Check if the taxi details are updated correctly
        updated_taxi = self.taxi_repository.get_all_taxis()[0]
        self.assertEqual(updated_taxi.total_fare, expected_fare)
        self.assertEqual(updated_taxi.location, end_location)
        self.assertFalse(updated_taxi.is_available)

if __name__ == '__main__':
    unittest.main()