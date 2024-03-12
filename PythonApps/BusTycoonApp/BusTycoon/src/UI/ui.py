from src.repository.busrepo import BusRepository
from src.service.busservice import BusService

class BusAppUI:
    def __init__(self, repository: BusRepository, service: BusService):
        self.repository = repository
        self.service = service

    def run(self):
        # Load data from files

        self.repository.load_data('bus_routes.txt', 'buses.txt')

        while True:




            print("\n1. Display all buses for a route")
            print("2. Calculate total mileage for a bus")
            print("3. Display routes sorted by total mileage")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                route_code = input("Enter route code: ")
                self.service.display_buses_by_route(route_code)

            elif choice == '2':
                bus_id = input("Enter bus ID: ")
                self.service.calculate_total_mileage(bus_id)

            elif choice == '3':
                self.service.display_routes_sorted_by_mileage()

            elif choice == '4':
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    from src.repository import BusRepository
    from src.service.busservice import BusService

    repository = BusRepository()
    service = BusService(repository)

    app_ui = BusAppUI(repository, service)
    app_ui.run()
