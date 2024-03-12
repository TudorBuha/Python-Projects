from src.domain.Rental import *
from src.repository.RentalRepo import *

class RentalServices:

    def __init__(self, rental_repo: RentalRepo):
        self.__repo = rental_repo

    def generate(self):
        self.__repo.generate()

    def add_rental(self, rental):
        self.__repo.add_rental(rental)

    def display_rentals(self):
        return self.__repo.display_rentals()

    def update_rentals(self, rental_id, new_returned_date):
        self.__repo.update_rental(rental_id, new_returned_date)

    def most_rented_movies(self):
        rental_list = self.__repo.display_rentals()
        most_rented = []
        for rental in rental_list:
            found = False
            for current_rental in most_rented:
                if rental.movie_id == current_rental["movie_id"]:
                    current_rental["number"] = current_rental["number"] + self.__repo.get_number_of_days(rental.rented_date, rental.returned_date)
                    found = True
                    break
            if found == False:
                current_movie = {"movie_id": rental.movie_id, "number": self.__repo.get_number_of_days(rental.rented_date, rental.returned_date)}
                most_rented.append(current_movie)
        most_rented.sort(key=lambda number_of_rents: number_of_rents["number"], reverse=True)
        return most_rented

    def most_active_clients(self):
        rental_list = self.__repo.display_rentals()
        most_active = []
        for rental in rental_list:
            ok = False
            for current_client in most_active:
                if rental.client_id == current_client["client_id"]:
                    current_client["number"] = current_client["number"] + self.__repo.get_number_of_days(rental.rented_date, rental.returned_date)
                    ok = True
                    break
            if ok == False:

                new_client = {"client_id": rental.client_id, "number": self.__repo.get_number_of_days(rental.rented_date, rental.returned_date)}
                most_active.append(new_client)
        most_active.sort(key=lambda number_of_rents: number_of_rents["number"], reverse=True)
        return most_active

    def late_rentals(self):
        rental_list = self.__repo.display_rentals()
        late_rental_list = []
        for rental in rental_list:
            ok = self.__repo.compare_dates(rental.due_date, rental.returned_date)
            if ok == True:
                late_rental = {"rental_id": rental.rental_id, "movie_id": rental.movie_id, "days_late": self.__repo.get_number_of_days(rental.due_date, rental.returned_date)}
                late_rental_list.append(late_rental)
        late_rental_list.sort(key=lambda number_of_days: number_of_days["days_late"], reverse=True)
        return late_rental_list
