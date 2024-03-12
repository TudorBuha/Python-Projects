from datetime import datetime

from src.Repository.Repo import RoomRepository, ReservationRepository
from src.Service.Service import ReservationService
from src.UI.UI import ReservationUI


def main():
    room_repo = RoomRepository('rooms.txt')
    reservation_repo = ReservationRepository('reservations.txt')
    reservation_service = ReservationService(room_repo, reservation_repo)
    reservation_ui = ReservationUI(reservation_service)

    room_repo.load_rooms()
    reservation_repo.load_reservations()

    while True:
        print("\nMain Menu:")
        print("1. Generate Random Reservations")
        print("2. Display Reservations for a Given Interval")
        print("3. Create a Reservation")
        print("4. Delete a Reservation by Number")
        print("5. Delete Reservations by Date Range and Room Number")
        print("6. Display Monthly Report of Available Rooms")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # This would be where you generate random reservations if needed.
            # You would uncomment the next line in a real scenario to generate data.
            reservation_service.generate_random_reservations(1000, 2023)
            #pass
        elif choice == "2":
            date_range = input("Enter the date range (dd.mm - dd.mm): ")
            try:
                start_date_str, end_date_str = date_range.split(' - ')
                start_date = datetime.strptime(start_date_str.strip(), '%d.%m')
                end_date = datetime.strptime(end_date_str.strip(), '%d.%m')
                # Assuming the year is 2023, you can modify as needed
                start_date = start_date.replace(year=2023)
                end_date = end_date.replace(year=2023)
                reservation_ui.display_reservations_for_period(start_date, end_date)
            except ValueError as e:
                print(f"Invalid date format: {e}")
        elif choice == "3":
            reservation_ui.create_reservation_ui()
        elif choice == "4":
            reservation_ui.delete_reservation_ui()
        elif choice == "5":
            reservation_ui.delete_reservations_by_date_and_room_ui()
        elif choice == "6":
            reservation_ui.display_monthly_report_ui()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
