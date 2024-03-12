class Room:
    def __init__(self, number, room_type):
        self.number = number
        self.room_type = room_type

class Reservation:
    def __init__(self, reservation_number, room_number, name, guests, arrival_date, departure_date):
        self.reservation_number = reservation_number
        self.room_number = room_number
        self.name = name  # in the format "family + given"
        self.guests = guests
        self.arrival_date = arrival_date
        self.departure_date = departure_date
