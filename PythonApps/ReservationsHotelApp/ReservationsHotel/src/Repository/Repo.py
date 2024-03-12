from datetime import datetime
from src.Domain.Entities import Room, Reservation


class RoomRepository:
    def __init__(self, rooms_file):
        self.rooms_file = rooms_file

    def load_rooms(self):
        """ Load rooms from the text file """
        self.rooms = []
        with open(self.rooms_file, 'r') as file:
            for line in file:
                number, room_type = line.strip().split(', ')
                self.rooms.append(Room(number, room_type))

    def get_rooms(self):
        """ Return a list of rooms """
        return self.rooms

class ReservationRepository:
    def __init__(self, reservations_file):
        self.reservations_file = reservations_file

    def load_reservations(self):
        """ Load reservations from the text file """
        self.reservations = []
        with open(self.reservations_file, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                reservation_number, room_number, name, guests, arrival_date, departure_date = parts
                reservation = Reservation(
                    reservation_number,
                    room_number,
                    name,
                    int(guests),
                    datetime.strptime(arrival_date, '%d.%m.%Y'),
                    datetime.strptime(departure_date, '%d.%m.%Y')
                )
                self.reservations.append(reservation)

    def save_reservations2(self, reservations):
        """ Save the reservations to the text file """
        with open(self.reservations_file, 'w') as file:
            for reservation in reservations:
                line = f"{reservation.reservation_number}, {reservation.room_number}, {reservation.name}, {reservation.guests}, {reservation.arrival_date.strftime('%d.%m.%Y')}, {reservation.departure_date.strftime('%d.%m.%Y')}\n"
                file.write(line)

    def save_reservations(self):
        """ Save the reservations to the text file without needing a parameter """
        with open(self.reservations_file, 'w') as file:
            for reservation in self.reservations:
                line = f"{reservation.reservation_number}, {reservation.room_number}, {reservation.name}, {reservation.guests}, {reservation.arrival_date.strftime('%d.%m.%Y')}, {reservation.departure_date.strftime('%d.%m.%Y')}\n"
                file.write(line)

    def add_reservation(self, reservation):
        """ Add a single reservation to the text file """
        with open(self.reservations_file, 'a') as file:
            line = f"{reservation.reservation_number}, {reservation.room_number}, {reservation.name}, {reservation.guests}, {reservation.arrival_date.strftime('%d.%m.%Y')}, {reservation.departure_date.strftime('%d.%m.%Y')}\n"
            file.write(line)

    def add_reservation2(self, reservation):
        """ Add a single reservation to the text file, ensuring it starts on a new line """
        with open(self.reservations_file, 'a+') as file:  # Open the file in append mode
            file.seek(0, 2)  # Go to the end of the file
            if file.tell() != 0 and file.seek(-1, 2) != '\n':  # Check if last character is not a newline
                file.write('\n')  # If not, write a newline
            # Write the new reservation
            line = f"{reservation.reservation_number}, {reservation.room_number}, {reservation.name}, {reservation.guests}, {reservation.arrival_date.strftime('%d.%m.%Y')}, {reservation.departure_date.strftime('%d.%m.%Y')}\n"
            file.write(line)

    def get_reservations(self):
        """ Return a list of reservations """
        return self.reservations

    def delete_reservation_by_number(self, reservation_number):
        """Delete a reservation by its number."""
        self.load_reservations()  # Reload the latest reservations
        reservation_to_delete = None
        for reservation in self.reservations:
            if reservation.reservation_number == reservation_number:
                reservation_to_delete = reservation
                break
        if reservation_to_delete:
            self.reservations.remove(reservation_to_delete)
            self.save_reservations()  # Save the updated reservations list to file
            return True
        return False

    def delete_reservations_by_date_and_room(self, start_date, end_date, room_number):
        """Delete reservations for a specific room within a date range."""
        self.load_reservations()  # Reload the latest reservations
        reservations_to_delete = [
            reservation for reservation in self.reservations
            if reservation.room_number == room_number and
               not (reservation.departure_date < start_date or reservation.arrival_date > end_date)
        ]
        for reservation in reservations_to_delete:
            self.reservations.remove(reservation)
        self.save_reservations()  # Save the updated reservations list to file
        return reservations_to_delete
