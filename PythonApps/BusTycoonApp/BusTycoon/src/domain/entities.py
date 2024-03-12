
class BusRoute:
    def __init__(self, route_code, length):
        self.route_code = route_code
        self.length = length

class Bus:
    def __init__(self, bus_id, route_code, model, times_used):
        self.bus_id = bus_id
        self.route_code = route_code
        self.model = model
        self.times_used = times_used
