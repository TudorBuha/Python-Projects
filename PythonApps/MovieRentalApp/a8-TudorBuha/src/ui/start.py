from src.services.MovieService import *
from src.services.ClientService import *
from src.repository.ClientRepo import *
from src.repository.MovieRepo import *
from src.ui.ConsoleUI import *

if __name__ == "__main__":
    client_repository = ClientRepo()
    movie_repository = MovieRepo()
    rental_repository = RentalRepo()
    client_services = ClientServices(client_repository)
    movie_services = MovieService(movie_repository)
    rental_services = RentalServices(rental_repository)
    ui = UI(client_services, movie_services, rental_services)
    ui.start()
