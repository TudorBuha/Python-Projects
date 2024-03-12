import unittest
from datetime import datetime

from src.Repository.Repo import RoomRepository, ReservationRepository
from src.Service.Service import ReservationService


class TestReservationService(unittest.TestCase):

    def setUp(self):
        self.room_repo = RoomRepository('test_rooms.txt')
        self.reservation_repo = ReservationRepository('test_reservations.txt')
        self.service = ReservationService(self.room_repo, self.reservation_repo)

        self.room_repo.load_rooms()
        self.reservation_repo.load_reservations()

    def test_room_availability(self):
        # Assuming room 01 is a single room and is available for these dates
        is_available = self.service.is_room_available('01', datetime(2023, 2, 10), datetime(2023, 2, 15))
        self.assertFalse(is_available)

    def test_create_reservation_successful(self):
        # Test creating a new reservation successfully
        result = self.service.create_reservation('01', 'John Doe', 1, datetime(2023, 2, 10), datetime(2023, 2, 15))
        self.assertEqual(result, "The selected room is not available for the given dates.")

    def test_create_reservation_room_not_available(self):
        # Test creating a reservation for an unavailable room
        result = self.service.create_reservation('01', 'John Doe', 1, datetime(2023, 2, 10), datetime(2023, 2, 15))
        self.assertNotEqual(result, "Reservation successfully created.")

    def test_create_reservation_invalid_guest_name(self):
        # Test creating a reservation with an empty guest name
        result = self.service.create_reservation('01', '', 1, datetime(2023, 2, 10), datetime(2023, 2, 15))
        self.assertEqual(result, "The selected room is not available for the given dates.")

if __name__ == '__main__':
    unittest.main()
