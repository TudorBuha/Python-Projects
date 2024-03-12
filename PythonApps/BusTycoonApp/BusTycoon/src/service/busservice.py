from src.repository.busrepo import BusRepository


class BusService:
    def __init__(self, repository: BusRepository):
        self.repository = repository

    def display_buses_by_route(self, route_code):
        buses = self.repository.get_buses_by_route(route_code)
        if buses:
            print(f"\nBuses on Route {route_code}:")
            for bus in buses:
                print(f"Bus ID: {bus.bus_id}, Model: {bus.model}, Times Used: {bus.times_used}")
        else:
            print(f"No buses found for Route {route_code}")

    def calculate_total_mileage(self, bus_id):
        """
        The function calculates the total mileage for a bus
        by multiplying the route length by the number of times
        the bus has used the route.
        :param bus_id: the ID of the bus
        :return: total mileage for the given bus with the given ID
        """
        bus = self.repository.get_bus_by_id(bus_id)
        if bus:
            total_mileage = self.repository.get_total_mileage_by_route(bus.route_code)
            print(f"\nBus ID: {bus.bus_id}, Model: {bus.model}, Total Mileage: {total_mileage} kilometers")
        else:
            print(f"No bus found with ID {bus_id}")

    def display_routes_sorted_by_mileage(self):
        """
        The function displays all routes sorted by total mileage.
        :return:
        """
        sorted_routes = sorted(self.repository.bus_routes,
                               key=lambda route: self.repository.get_total_mileage_by_route(route.route_code),
                               reverse=True)

        print("\nRoutes Sorted by Total Mileage:")
        for route in sorted_routes:
            total_mileage = self.repository.get_total_mileage_by_route(route.route_code)
            print(f"Route {route.route_code}: Total Mileage - {total_mileage} kilometers")
            buses_on_route = self.repository.get_buses_by_route(route.route_code)
            for bus in buses_on_route:
                print(f"  - Bus ID: {bus.bus_id}, Model: {bus.model}, Times Used: {bus.times_used}")
