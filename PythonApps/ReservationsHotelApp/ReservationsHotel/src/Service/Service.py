import calendar
import random
from datetime import datetime, timedelta

from src.Domain.Entities import Reservation


class ReservationService:
    def __init__(self, room_repository, reservation_repository):
        self.room_repository = room_repository
        self.reservation_repository = reservation_repository

    def generate_random_date(self, year):
        """ Generate a random date within the given year """
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    def generate_random_reservations(self, num_reservations, year):
        """ Generate random reservations for the given year """
        names = ["Popescu Ioan", "Ionescu Maria", "Dumitru Ana"]  # Placeholder for real names
        self.room_repository.load_rooms()
        rooms = self.room_repository.get_rooms()
        for i in range(1, num_reservations + 1):
            room = random.choice(rooms)
            name = random.choice(names)  # Should be replaced with a proper random name generator
            guests = random.randint(1, 4)  # Assuming a max of 4 guests for simplicity
            arrival_date = self.generate_random_date(year)
            departure_date = arrival_date + timedelta(days=random.randint(1, 14))  # Stays can be 1 to 14 days
            reservation = Reservation(
                reservation_number=str(i),
                room_number=room.number,
                name=name,
                guests=guests,
                arrival_date=arrival_date,
                departure_date=departure_date
            )
            self.reservation_repository.add_reservation(reservation)

    def get_reservations_for_date_range(self, start_date, end_date):
        """ Retrieve reservations for a specific date range """
        self.reservation_repository.load_reservations()
        reservations = self.reservation_repository.get_reservations()
        return [
            reservation for reservation in reservations
            if start_date <= reservation.arrival_date <= end_date
        ]

    def is_room_available(self, room_number, arrival_date, departure_date):
        """ Check if a room is available for the given date range """
        for reservation in self.reservation_repository.get_reservations():
            # Check for date range overlap and same room number
            if (reservation.room_number == room_number and not (
                    departure_date <= reservation.arrival_date or
                    arrival_date >= reservation.departure_date)):
                return False  # Room is not available
        return True  # Room is available

    def create_reservation(self, room_number, guest_name, guests, arrival_date, departure_date):
        """
        Create a new reservation and save it to the repository
        :param room_number: the room number
        :param guest_name: the name of the guest
        :param guests: the number of guests
        :param arrival_date: the arrival date
        :param departure_date: the departure date
        :return: result message as a string
        """
        # Check if the room is available
        if not self.is_room_available(room_number, arrival_date, departure_date):
            return "The selected room is not available for the given dates."

        # Check if the guest's name is not empty
        if not guest_name.strip():
            return "Guest's name cannot be empty."

        # Validate the number of guests based on room type
        room = next((room for room in self.room_repository.get_rooms() if room.number == room_number), None)
        if room is None:
            return "Room does not exist."

        max_guests = {"single": 1, "double": 2, "family": 4}
        if guests > max_guests.get(room.room_type, 0):
            return f"The number of guests is too high for the selected {room.room_type} room."

        # Create and save the new reservation
        new_reservation_number = str(len(self.reservation_repository.get_reservations()) + 1)
        new_reservation = Reservation(
            reservation_number=new_reservation_number,
            room_number=room_number,
            name=guest_name,
            guests=guests,
            arrival_date=arrival_date,
            departure_date=departure_date
        )
        self.reservation_repository.add_reservation(new_reservation)
        return "Reservation successfully created."

    def delete_reservation(self, reservation_number):
        """Delete a reservation by its number."""
        if self.reservation_repository.delete_reservation_by_number(reservation_number):
            return "Reservation deleted successfully."
        else:
            return "Reservation number does not exist."

    def delete_reservations_for_room_in_date_range(self, start_date, end_date, room_number):
        """Delete reservations for a specific room within a date range."""
        deleted_reservations = self.reservation_repository.delete_reservations_by_date_and_room(start_date, end_date,
                                                                                                room_number)
        return deleted_reservations  # This will return the list of deleted reservations

    def get_monthly_report(self, year, month):
        """ Get a report of available rooms for each day of the given month """
        self.room_repository.load_rooms()
        total_rooms = len(self.room_repository.get_rooms())
        self.reservation_repository.load_reservations()
        reservations = self.reservation_repository.get_reservations()

        # Initialize the report with the total number of rooms available for each day
        days_in_month = calendar.monthrange(year, month)[1]
        report = {day: total_rooms for day in range(1, days_in_month + 1)}

        # Subtract the number of rooms reserved for each day
        for reservation in reservations:
            if reservation.arrival_date.year == year and reservation.arrival_date.month == month:
                for day in range(reservation.arrival_date.day, min(reservation.departure_date.day, days_in_month) + 1):
                    report[day] -= 1

        return report