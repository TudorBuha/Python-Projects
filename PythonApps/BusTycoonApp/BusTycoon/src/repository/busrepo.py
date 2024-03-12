from src.domain.entities import Bus, BusRoute

class BusRepository:
    def __init__(self):
        self.bus_routes = []
        self.buses = []

    def load_data(self, routes_file, buses_file):
            with open(routes_file, 'r') as route_file:
                for line in route_file:
                    route_data = line.strip().split(', ')
                    route = BusRoute(route_data[0], int(route_data[1]))
                    self.bus_routes.append(route)

            with open(buses_file, 'r') as bus_file:
                for line in bus_file:
                    bus_data = line.strip().split(', ')
                    bus = Bus(bus_data[0], bus_data[1], bus_data[2], int(bus_data[3]))
                    self.buses.append(bus)

    def get_buses_by_route(self, route_code):

        buses_on_route = []
        for bus in self.buses:
            if bus.route_code == route_code:
                buses_on_route.append(bus)
        return buses_on_route
    def get_total_mileage_by_route(self, route_code):
        """
        The function calculates the total mileage for a route
        by multiplying the route length by the number of times
        each bus has used the route.

        :param route_code: the code of the route
        :return: total mileage for the given route with the given code
        """
        route_length = 0
        buses_on_route = []
        total_mileage = 0
        for route in self.bus_routes:
            if route.route_code == route_code:
                route_length = route.length
        for bus in self.buses:
            if bus.route_code == route_code:
                buses_on_route.append(bus)
        for bus in buses_on_route:
            total_mileage += bus.times_used * route_length
        return total_mileage


    def get_bus_by_id(self, bus_id):

        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus
