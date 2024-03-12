import calendar
from datetime import datetime

from texttable import Texttable

class ReservationUI:
    def __init__(self, reservation_service):
        self.reservation_service = reservation_service

    def display_reservations_for_period3(self, start_date, end_date):
        """ Display all reservations for a given period """
        reservations = self.reservation_service.get_reservations_for_date_range(start_date, end_date)
        # Sort the reservations by last name
        reservations.sort(key=lambda x: x.name.split()[-1])
        table = Texttable()
        # Define table header to match the desired format
        table.header(['Month', 'Name', 'Guests'])
        for reservation in reservations:
            # Extract the month name from the arrival date
            month = reservation.arrival_date.strftime('%B')
            # Add each reservation to the table, omitting reservation number and room number
            table.add_row([month, reservation.name, f"{reservation.guests} persons"])
        print(table.draw())  # Print the table

    def display_reservations_for_period2(self, start_date, end_date):
        """ Display all reservations for a given period """
        reservations = self.reservation_service.get_reservations_for_date_range(start_date, end_date)
        table = Texttable()
        # Define table header
        table.header(['Reservation Number', 'Room Number', 'Name', 'Guests', 'Arrival Date', 'Departure Date'])
        for reservation in reservations:
            # Add each reservation to the table
            table.add_row([reservation.reservation_number, reservation.room_number, reservation.name,
                           f"{reservation.guests} persons", reservation.arrival_date.strftime('%d.%m.%Y'),
                           reservation.departure_date.strftime('%d.%m.%Y')])
        print(table.draw())  # Print the table

    def display_reservations_for_period(self, start_date, end_date):
        """ Display all reservations for a given period """
        reservations = self.reservation_service.get_reservations_for_date_range(start_date, end_date)
        reservations.sort(key=lambda x: x.name.split()[0])  # Sort by family name

        table = Texttable()
        table.set_cols_align(["l", "l", "r"])  # Align the columns 'left', 'left', 'right'
        table.set_cols_valign(["m", "m", "m"])  # Vertical align to 'middle'
        table.set_cols_width([20, 20, 10])  # Set column widths

        # Define table header as per the image provided
        table.header(['Date', 'Name', 'Guests'])

        # Update to show date range in a single column and format the name correctly
        for reservation in reservations:
            date_range = f"{reservation.arrival_date.strftime('%d.%m')} - {reservation.departure_date.strftime('%d.%m')}"
            table.add_row([date_range, reservation.name, f"{reservation.guests} persons"])

        print(table.draw())  # Print the table

    def input_date(self, prompt):
        """ Get a date from the user """
        while True:
            date_str = input(prompt)
            try:
                return datetime.strptime(date_str, '%d.%m.%Y')
            except ValueError:
                print("This is the incorrect date string format. It should be DD.MM.YYYY")

    def create_reservation_ui(self):
        """
        Create a new reservation based on user input and display the result
        :return: the result of the reservation attempt as a string
        """
        print("Create a new reservation:")
        arrival_date_str = input("Enter arrival date (dd.mm.yyyy): ")
        departure_date_str = input("Enter departure date (dd.mm.yyyy): ")

        # Convert string input to datetime objects
        try:
            arrival_date = datetime.strptime(arrival_date_str, '%d.%m.%Y')
            departure_date = datetime.strptime(departure_date_str, '%d.%m.%Y')
        except ValueError:
            print("Invalid date format. Please use the format dd.mm.yyyy.")
            return  # Return to the main menu

        # Display available rooms
        available_rooms = [room for room in self.reservation_service.room_repository.get_rooms()
                           if self.reservation_service.is_room_available(room.number, arrival_date, departure_date)]
        if not available_rooms:
            print("No rooms are available for the selected dates.")
            return  # Return to the main menu

        print("Available rooms:")
        for room in available_rooms:
            print(f"Room Number: {room.number}, Type: {room.room_type}")

        # Get user input for reservation details
        room_number = input("Enter the room number to book: ")
        guest_name = input("Enter the guest's name: ")
        try:
            guests = int(input("Enter the number of guests: "))
        except ValueError:
            print("Number of guests should be an integer.")
            return  # Return to the main menu

        # Create the reservation
        result = self.reservation_service.create_reservation(room_number, guest_name, guests, arrival_date,
                                                             departure_date)
        print(result)  # Print the result of the reservation attempt

    def delete_reservation_ui2(self):
        """UI functionality to delete reservations."""
        reservation_number = input("Enter reservation number to delete (or 'cancel' to return): ")
        if reservation_number.lower() == 'cancel':
            return
        result = self.reservation_service.delete_reservation(reservation_number)
        print(result)

    def delete_reservation_ui(self):
        """UI functionality to delete a single reservation."""
        reservation_number = input("Enter reservation number to delete (or 'cancel' to return): ")
        if reservation_number.lower() == 'cancel':
            return
        deleted = self.reservation_service.delete_reservation(reservation_number)
        if deleted:
            print("The following reservation has been deleted:")
            self.display_deleted_reservations([deleted])  # Assuming delete_reservation returns the deleted reservation
        else:
            print("Reservation number does not exist.")

    def delete_reservations_by_date_and_room_ui2(self):
        """UI functionality to delete reservations by date range and room number."""
        date_range = input("Enter the date range (dd.mm - dd.mm) or 'cancel' to return: ")
        if date_range.lower() == 'cancel':
            return
        try:
            start_date_str, end_date_str = date_range.split(' - ')
            start_date = datetime.strptime(start_date_str.strip(), '%d.%m')
            end_date = datetime.strptime(end_date_str.strip(), '%d.%m')
            # Assuming the year is 2023, you can modify as needed
            start_date = start_date.replace(year=2023)
            end_date = end_date.replace(year=2023)
        except ValueError:
            print("Invalid date format. Please use the format dd.mm - dd.mm.")
            return

        room_number = input("Enter the room number or 'cancel' to return: ")
        if room_number.lower() == 'cancel':
            return

        deleted_reservations = self.reservation_service.delete_reservations_for_room_in_date_range(start_date, end_date,
                                                                                                   room_number)
        if deleted_reservations:
            print("Deleted reservations:")
            for reservation in deleted_reservations:
                print(
                    f"Reservation number {reservation.reservation_number} for room {reservation.room_number} from {reservation.arrival_date.strftime('%d.%m.%Y')} to {reservation.departure_date.strftime('%d.%m.%Y')}")
        else:
            print("No reservations found for the given criteria.")

    def delete_reservations_by_date_and_room_ui(self):
        """UI functionality to delete reservations by date range and room number."""
        date_range = input("Enter the date range (dd.mm - dd.mm) or 'cancel' to return: ")
        if date_range.lower() == 'cancel':
            return
        try:
            start_date_str, end_date_str = date_range.split(' - ')
            start_date = datetime.strptime(start_date_str.strip(), '%d.%m')
            end_date = datetime.strptime(end_date_str.strip(), '%d.%m')
            # Assuming the year is 2023, you can modify as needed
            start_date = start_date.replace(year=2023)
            end_date = end_date.replace(year=2023)
        except ValueError:
            print("Invalid date format. Please use the format dd.mm - dd.mm.")
            return

        room_number = input("Enter the room number or 'cancel' to return: ")
        if room_number.lower() == 'cancel':
            return

        deleted_reservations = self.reservation_service.delete_reservations_for_room_in_date_range(start_date, end_date,
                                                                                                   room_number)
        if deleted_reservations:
            print("The following reservations have been deleted:")
            self.display_deleted_reservations(deleted_reservations)
        else:
            print("No reservations found for the given criteria or failed to delete.")

    def display_deleted_reservations(self, deleted_reservations):
        """ Display deleted reservations in a table format. """
        # Create a table with the specified headers
        table = Texttable()
        table.set_cols_align(["c", "l", "r"])  # Center, left, right align columns
        table.header(['February', 'Name', 'Guests'])

        for reservation in deleted_reservations:
            # Assuming reservation.arrival_date and reservation.departure_date are datetime objects
            date_range = f"{reservation.arrival_date.strftime('%m.%d')} - {reservation.departure_date.strftime('%m.%d')}"
            table.add_row([date_range, reservation.name, f"{reservation.guests} persons"])

        print(table.draw())  # Print the table

    def display_monthly_report_ui(self):
        """ Display the monthly report of available rooms for each day """
        year = 2023  # Example year, can be made dynamic if needed
        month = int(input("Enter the month number (1-12): "))
        if not 1 <= month <= 12:
            print("Invalid month. Please enter a number between 1 and 12.")
            return

        report = self.reservation_service.get_monthly_report(year, month)
        table = Texttable()
        table.set_cols_align(["c"] * 7)
        table.set_cols_valign(["m"] * 7)
        table.add_rows([['M', 'T', 'W', 'T', 'F', 'S', 'S']])

        # Add each week to the table
        cal = calendar.Calendar()
        for week in cal.monthdayscalendar(year, month):
            week_row = []
            for day in week:
                if day == 0:  # Day outside month
                    week_row.append('')
                else:
                    week_row.append(f"{day}/{report[day]}")
            table.add_row(week_row)

        print(table.draw())