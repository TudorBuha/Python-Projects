from domain.Taxi import *

class TaxiRepository:
    def __init__(self, num_taxis):
        self.taxis = [Taxi(i) for i in range(1, num_taxis + 1)]


    def get_all_taxis(self):
        return self.taxis

    def update_taxi(self, updated_taxi):
        for i, taxi in enumerate(self.taxis):
            if taxi.taxi_id == updated_taxi.taxi_id:
                self.taxis[i] = updated_taxi
                break