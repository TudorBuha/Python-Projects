from domain import *
from repository import *
from service.TaxiService import *
from UI import *

def main():
    num_taxis = int(input("Enter the number of operational taxis (1-10): "))
    taxi_repository = TaxiRepository(num_taxis)
    taxi_service = TaxiService(taxi_repository)
    taxi_ui = TaxiUI(taxi_service)

    taxi_ui.start()

if __name__ == "__main__":
    main()