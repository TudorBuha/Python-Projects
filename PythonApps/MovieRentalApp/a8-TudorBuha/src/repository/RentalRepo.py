from random import randint, choice
import dateutil
from src.domain.Rental import *
from datetime import date
from datetime import datetime
from src.repository.ClientRepo import NotUniqueClientIdError, NotFoundID


class RentalRepo:

    def __init__(self):
        self._rental_list = []

    def generate(self):
        """
        Generates 20 random rentals
        :return:
        """
        rented_date_list = ["2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07",
                            "2023-01-08", "2023-01-09", "2023-01-10", "2023-01-11", "2023-01-12", "2023-01-13",
                            "2023-01-14", "2023-01-15", "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19",
                            "2023-01-20", "2023-01-21"]
        due_date_list = ["2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25", "2023-01-26", "2023-01-27",
                         "2023-01-28", "2023-01-29", "2023-01-30", "2023-01-31", "2023-02-01", "2023-02-02",
                         "2023-02-03", "2023-02-04", "2023-02-05", "2023-02-06", "2023-02-07", "2023-02-08",
                         "2023-02-09", "2023-02-10"]
        returned_date_list = ["2023-01-30", "2023-02-12", "2023-01-24", "2023-01-31", "2023-01-23", "2023-02-16",
                              "2023-02-17", "2023-01-25", "2023-02-19", "2023-01-26", "2023-02-21", "2023-02-22",
                              "2023-01-23", "2023-02-24", "2023-02-25", "2023-02-26", "2023-01-27", "2023-02-28",
                              "2023-03-01", "2023-03-02"]
        for i in range(1, 21):
            rentals_id = i
            id_movie = randint(1, 20)
            id_client = randint(1, 20)
            rented_date = choice(rented_date_list)
            due_date = choice(due_date_list)
            #returned_date = choice(returned_date_list)
            returned_date = choice(returned_date_list)
            rental = Rental(rentals_id, id_movie, id_client, rented_date, due_date, returned_date)
            self._rental_list.append(rental)

    def add_rental(self, rental):
        if self.already_exists_rental(rental) is False:
            raise NotUniqueClientIdError(rental.rental_id)
        self._rental_list.append(rental)

    def display_rentals(self):
        return self._rental_list

    def update_rental(self, rental_id, new_returned_date):
        found = False
        for rental in self._rental_list:
            if int(rental.rental_id) == int(rental_id):
                rental.returned_date = new_returned_date
                found = True
        if found == False:
            raise NotFoundID(rental_id)

    def get_number_of_days(self, rented_date, returned_date):

        year = 0
        month = 1
        day = 2

        if returned_date is None:
            current_rented_date = rented_date.split("-")
            current_date = datetime.now()
            rented_date_copy = date(int(current_rented_date[year]), int(current_rented_date[month]), int(current_rented_date[day]))
            returned_date_copy = date(int(current_date.year), int(current_date.month), int(current_date.day))
            delta = returned_date_copy - rented_date_copy
        else:
            current_rented_date = rented_date.split("-")
            returned_date1 = returned_date.split("-")
            rented_date_copy = date(int(current_rented_date[year]), int(current_rented_date[month]), int(current_rented_date[day]))
            returned_date_copy = date(int(returned_date1[year]), int(returned_date1[month]), int(returned_date1[day]))
            delta = returned_date_copy - rented_date_copy
        return delta.days

    def compare_dates(self, due_date, returned_date):
        year = 0
        month = 1
        day = 2
        ok = False
        if returned_date is None:
            current_due_date = due_date.split("-")
            current_returned_date = datetime.now()
            if int(current_due_date[year]) < int(current_returned_date.year):
                ok = True
            elif int(current_due_date[year]) == int(current_returned_date.year):
                if int(current_due_date[month]) < int(current_returned_date.month):
                    ok = True
                elif int(current_due_date[month]) == int(current_returned_date.month):
                    if int(current_due_date[day]) < int(current_returned_date.day):
                        ok = True
        else:
            current_due_date = due_date.split("-")
            current_returned_date = returned_date.split("-")
            if int(current_due_date[year]) < int(current_returned_date[year]):
                ok = True
            elif int(current_due_date[year]) == int(current_returned_date[year]):
                if int(current_due_date[month]) < int(current_returned_date[month]):
                    ok = True
                elif int(current_due_date[month]) == int(current_returned_date[month]):
                    if int(current_due_date[day]) < int(current_returned_date[day]):
                        ok = True
        return ok

    def already_exists_rental(self, rental_to_search_for):
        for current_rental in self._rental_list:
            if current_rental.rental_id == rental_to_search_for.rental_id:
                return False
        return True

