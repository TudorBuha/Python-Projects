import copy
import pickle
import time
from collections import defaultdict
from datetime import timedelta, datetime
from numpy import random

from src.domain.Rental import Rental

class NotUniqueIdError(Exception):
    def __init__(self, rental_id):
        self.__rental_id = rental_id

    def __str__(self):
        return str(self.__rental_id) + " is not an unique id "

class RentalRepo:

    def __init__(self):
        self._rentallist = []
        self.generate_n_rentals(20)
    def already_exists_rental_movie(self, rental: Rental):
        """
        Function that checks if a rental already exists
        :param rental:
        :return:
        """

        for x in self._rentallist:
            if x.rental_id == rental.rental_id:
                return False
        return True

    def add_rental(self, rental:Rental):
        """
        Function that adds a rental to the list
        :param rental: object of type Rental
        :return:
        """
        if self.already_exists_rental_movie(rental) is False:
            raise NotUniqueIdError(rental.rental_id)

        else:

            self._rentallist.append(rental)

    def remove_rental(self, rental_id):
        """
        Function that removes a rental from the list
        :param rental_id: id of the rental to be removed
        :return:
        """
        for rental in self._rentallist:
            if rental_id == rental.rental_id:
                self._rentallist.remove(rental)

    def update_rental(self, rental_id: int, returned_date: []):
        """
        Function that updates a rental
        :param rental_id: id of the rental to be updated
        :param returned_date: date that will replace the old one
        :return:
        """
        for rental in self._rentallist:
            if rental.rental_id == rental_id:
                rental.returned_date = copy.deepcopy(returned_date)

    def get_all_rentals_by_id(self, client_id: int):
        """
        Function that returns all the rentals of a client
        :param client_id: id of the client
        :return:
        """
        elements = []
        for rental in self._rentallist:
            if rental.client_id == client_id:
                elements.append(rental)
        return elements

    def get_all_rentals(self):
        """
        Function that returns the list of rentals
        :return:
        """
        return self._rentallist

    def most_rented_movies(self):
        aux = defaultdict(lambda: [0, 0])
        for rental in self._rentallist:
            aux[rental.movie_id][0] = rental.movie_id
            due_date_conversion = rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365
            rented_date_conversion = rental.rented_date[0] + rental.rented_date[1] * 30 + rental.rented_date[2] * 365

            aux[rental.movie_id][1] = aux[rental.movie_id][1] + due_date_conversion - rented_date_conversion

        sorted_array = sorted(aux.values(), reverse=True, key=lambda k: k[1])

        return sorted_array


    def most_active_clients(self):
        aux = defaultdict(lambda: [0, 0])
        for rental in self._rentallist:
            aux[rental.client_id][0] = rental.client_id

            due_date_conversion = rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365
            rented_date_conversion = rental.rented_date[0] + rental.rented_date[1] * 30 + rental.rented_date[2] * 365

            aux[rental.client_id][1] = aux[rental.client_id][1] + due_date_conversion - rented_date_conversion

        sorted_array = sorted(aux.values(), reverse=True, key=lambda k: k[1])

        return sorted_array

    def late_rentals(self):
        aux = defaultdict(lambda: [0, 0])

        for rental in self._rentallist:
            if rental.returned_date is None:
                continue

            aux[rental.rental_id][0] = rental.rental_id


            due_date_conversion = rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365
            returned_date_conversion = rental.returned_date[0] + rental.returned_date[1] * 30 + rental.returned_date[2] * 365

            if returned_date_conversion - due_date_conversion >=0:

                aux[rental.rental_id][1] = returned_date_conversion - due_date_conversion

        sorted_array = sorted(aux.values(), reverse=True, key=lambda k: k[1])

        return sorted_array

    def get_rental_by_id(self, id):
        """
        Function that returns a rental by id
        :param id: id of the rental
        :return:
        """
        for rental in self._rentallist:
            if rental.rental_id == id:
                return rental


    def generate_rentals(self,idd:int):

        """
        Function that generates a  rental
        :param idd: id of the rental
        :return:
        """




        id_ = idd
        movie_id_=random.randint(1,20)
        client_id=random.randint(1,20)

        rent_date_day = random.randint(1,30)
        rent_date_month= random.randint(1, 13)
        rent_date_year= random.randint(2010, 2015)

        due_date_day= random.randint(1, 30)
        due_date_month=random.randint(1, 13)
        due_date_year=rent_date_year+random.randint(1,3)





        return Rental(id_,movie_id_, client_id, [rent_date_day, rent_date_month, rent_date_year],[due_date_day, due_date_month, due_date_year] )


    def generate_n_rentals(self,n: int):
        """
        Function that generates n rentals
        :param n: number of rentals to be generated
        :return:
        """

        for i in range(1,n+1):
            new = self.generate_rentals(i)
            self._rentallist.append(new)


class RentalTextFileRepo(RentalRepo):
    def __init__(self, file_name):
        self._rentallist=[]
        self.__file_name=file_name

        self.load()

    def load(self):
        try:
            file =open(self.__file_name, "r")
            values = file.readlines()
            for value in values:
                value=value.removesuffix("\n")
                parsed_values = value.split("|")
                due_date=parsed_values[3].removesuffix("]"). removeprefix("[")
                due_date1=parsed_values[4].removesuffix("]").removeprefix("[")
                values1=due_date.split(",")
                values2 = due_date1.split(",")
                if parsed_values[5]!="None":
                    due_date2= parsed_values[5].removeprefix("[").removesuffix("]")
                    values3 = due_date2.split(",")
                    self.add_rental(Rental(int(parsed_values[0]), int(parsed_values[1]), int(parsed_values[2]), [int(values1[0]), int(values1[1]), int(values1[2])], [int(values2[0]), int(values2[1]), int(values2[2])], [int(values3[0]), int(values3[1]), int(values3[2])]))
                else:
                    self.add_rental(Rental(int(parsed_values[0]), int(parsed_values[1]), int(parsed_values[2]), [int(values1[0]), int(values1[1]), int(values1[2])], [int(values2[0]), int(values2[1]), int(values2[2])], None))

            file.close()
        except FileNotFoundError as ve:
            self.generate_n_rentals(20)
            self.save()
            pass

    def save(self):
        array=[]
        for rental in self._rentallist:
             array.append(str(rental.rental_id) + "|" + str(rental.movie_id) + "|" + str(rental.client_id) + "|" + str(rental.rented_date) + "|" +  str(rental.due_date) + "|" + str(rental.returned_date) + "\n")
        file=open(self.__file_name, "w")
        file.writelines(array)
        file.close()

    def add_rental(self, rental:Rental):
        super().add_rental(rental)
        self.save()

    def update_rental(self, id:int, date:[]):
        super().update_rental(id, date)

class RentalBinaryRepo(RentalRepo):
    def __init__(self, file_name: str):
        self._rentallist = []
        self.__file_name = file_name

        self.load()


    def load(self):
        try:
            file = open(self.__file_name, "rb")
            self._rentallist = pickle.load(file)
            file.close()

        except:
            self.generate_n_rentals(20)
            self.save()
            pass



    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._rentallist, file)
        file.close()