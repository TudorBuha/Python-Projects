from jproperties import *

from src.services.ClientService import ClientService
from src.services.HistoryService import *
from src.services.MovieService import MovieService
from src.services.RentalService import RentalService


class Ui:
    def __init__(self, client_service: ClientService, movie_service: MovieService, rental_service: RentalService,
                 history_service: HistoryService):
        self.__client_service = client_service
        self.__movie_service = movie_service
        self.__rental_service = rental_service
        self.__history_service = history_service

    def print_menu(self):
        print("Insert an option:")
        print("1. Client menu")
        print("2. Movie menu")
        print("3. Rental menu")
        print("4. Search menu")
        print("5. Statistics menu")
        print("6. Undo")
        print("7. Redo")
        print("0. Exit")
        # TO DO

        return input("> ")

    def print_client_menu(self):
        print("Insert sub-option:")
        print("1. Add a new entry")
        print("2. Remove a client")
        print("3. List all clients")
        print("4. Update client's name")

        return input(">")

    def print_movie_menu(self):
        print("Insert sub-option:")
        print("1. Add a new entry")
        print("2. Remove a movie")
        print("3. List all movies")
        print("4. Update movie's title")
        print("5. Update movie's description")
        print("6. Update movie's genre")

        return input(">")

    def print_rental_menu(self):
        print("Insert sub-option:")
        print("1. Add a new entry")
        print("2. Return a rental")
        print("3. List all rentals")

        return input(">")

    def print_search_menu(self):
        print("Insert sub-option:")
        print("1. Search upon movies")
        print("2. Search upon clients")

        return input(">")

    def print_statistics_menu(self):
        print("Insert sub-option:")
        print("1. Most rented movies")
        print("2. Most active clients")
        print("3. Late rentals")

        return input(">")

    def start(self):

        while True:
            try:
                print("-- Menu:")
                option = self.print_menu()

                if option == "1":
                    option = self.print_client_menu()
                    self.couple_client_option(option)

                elif option == "2":
                    option = self.print_movie_menu()
                    self.couple_movie_option(option)

                elif option == "3":
                    option = self.print_rental_menu()
                    self.couple_rental_option(option)

                elif option == "4":
                    option = self.print_search_menu()
                    self.couple_search_option(option)

                elif option == "5":
                    option = self.print_statistics_menu()
                    self.couple_statistics_option(option)

                elif option == "6":
                    self.__history_service.undo()

                elif option == "7":
                    self.__history_service.redo()

                elif option == "0":
                    exit()
            except Exception as ex:
                print(ex)

    def couple_client_option(self, option: str):
        if option == "1":
            client_id = input("Id: ")
            client_name = input("Name: ")
            client = Client(int(client_id), client_name)
            self.__client_service.add_client(client)

            self.__history_service.add_to_history("add client", [client.client_id, client.name])

        elif option == "2":
            client_id = input("Id: ")
            client = self.__client_service.get_client_by_id(int(client_id))
            self.__client_service.remove(int(client_id))
            rentals = self.__rental_service.get_all_rentals_by_client(client.client_id)
            for rental in rentals:
                self.__rental_service.remove_rental(rental.rental_id)
            self.__history_service.add_to_history("remove client", [client.client_id, client.name, rentals])

        elif option == "3":
            elements = self.__client_service.get_all_clients()
            for el in elements:
                print(el)

        elif option == "4":
            client_id = input("Id: ")
            client_name = input("Name: ")
            client = self.__client_service.get_client_by_id(int(client_id))
            client_initial_name = client.name
            self.__client_service.update(int(client_id), client_name)
            self.__history_service.add_to_history("update client", [int(client_id), client_initial_name, client_name])

        else:
            print("Invalid option.")
            pass

    def couple_movie_option(self, option: str):
        if option == "1":
            movie_id = input("Id: ")
            title = input("Title")
            description = input("Description: ")
            genre = input("Genre: ")
            self.__movie_service.add_movie(Movie(int(movie_id), title, description, genre))
            self.__history_service.add_to_history("add movie", [int(movie_id), title, description, genre])
        elif option == "2":
            movie_id = input("Id: ")
            movie = self.__movie_service.get_movie_by_id(int(movie_id))
            self.__movie_service.remove(movie.movie_id)
            rentals = self.__rental_service.get_all_rentals_by_movie(movie.movie_id)
            for rental in rentals:
                self.__rental_service.remove_rental(rental.rental_id)
            self.__history_service.add_to_history(
                "remove movie", [movie.movie_id, movie.title, movie.description, movie.genre, rentals])
        elif option == "3":
            elements = self.__movie_service.get_all_movies()
            for el in elements:
                print(el)
        elif option == "4":
            movie_id = input("Id: ")
            title = input("Title: ")
            movie = self.__movie_service.get_movie_by_id(int(movie_id))
            previous_movie_title = movie.title
            self.__movie_service.update_title(int(movie_id), title)
            self.__history_service.add_to_history("update title", [movie.movie_id, previous_movie_title, title])

        elif option == "5":
            movie_id = input("Id: ")
            description = input("Description: ")
            movie = self.__movie_service.get_movie_by_id(int(movie_id))
            previous_movie_desc = movie.description
            self.__movie_service.update_description(int(movie_id), description)
            self.__history_service.add_to_history("update description",
                                                  [movie.movie_id, previous_movie_desc, description])
        elif option == "6":
            movie_id = input("Id: ")
            genre = input("Genre: ")
            movie = self.__movie_service.get_movie_by_id(int(movie_id))
            previous_movie_genre = movie.genre
            self.__movie_service.update_genre(int(movie_id), genre)
            self.__history_service.add_to_history("update genre", [movie.movie_id, previous_movie_genre, genre])
        else:
            print("Invalid option.")
            pass

    def couple_rental_option(self, option: str):
        if option == "1":
            rental_id = input("Id: ")
            movie_id = input("Movie id: ")
            client_id = input("Client id: ")
            rented_date_raw = input("Rented date: ")
            due_date_raw = input("Due date: ")

            rented_date_args = rented_date_raw.split(' ')
            due_date_args = due_date_raw.split(' ')

            self.__rental_service.add_rental(
                int(rental_id), int(movie_id), int(client_id),
                [int(rented_date_args[0]), int(rented_date_args[1]), int(rented_date_args[2])],
                [int(due_date_args[0]), int(due_date_args[1]), int(due_date_args[2])])
            rental = self.__rental_service.get_rental_by_id(int(rental_id))
            self.__history_service.add_to_history("add rental", [rental.rental_id, rental.movie_id, rental.client_id,
                                                                 rental.rented_date, rental.due_date,
                                                                 rental.returned_date])
        elif option == "2":
            rental_id = input("Id: ")
            returned_date_raw = input("Returned date: ")

            returned_date_args = returned_date_raw.split(' ')

            rental = self.__rental_service.get_rental_by_id(int(rental_id))

            previous_returned_date = rental.returned_date

            self.__rental_service.return_rental(
                int(rental_id),
                [int(returned_date_args[0]), int(returned_date_args[1]), int(returned_date_args[2])])

            self.__history_service.add_to_history("update rental", [rental.rental_id, rental.client_id, rental.movie_id,
                                                                    rental.rented_date, rental.due_date,
                                                                    rental.returned_date, previous_returned_date])
        elif option == "3":
            for el in self.__rental_service.get_all_rentals():
                print(el)

    def couple_search_option(self, option):
        if option == "1":
            search_string = input("Search string: ")
            for el in self.__movie_service.search(search_string):
                print(el)
        elif option == "2":
            search_string = input("Search string: ")
            for el in self.__client_service.search(search_string):
                print(el)
        else:
            print("Invalid option.")

    def couple_statistics_option(self, option):
        if option == "1":
            for el in self.__rental_service.get_most_rented_movies():
                print("Days: ", el[1], " for ", self.__movie_service.get_movie_by_id(el[0]))
        elif option == "2":
            for el in self.__rental_service.get_most_active_clients():
                print("Days: ", el[1], " for ", self.__client_service.get_client_by_id(el[0]))
        elif option == "3":
            for el in self.__rental_service.get_late_rentals():
                if el[1] > 0:
                    print("Days late: ", el[1], " for ", self.__rental_service.get_rental_by_id(el[0]))
        else:
            print("Invalid option.")


###############################################  START
def main():
    config = Properties()
    with open("settings.properties", "rb") as config_file:
        config.load(config_file)

    if config.get("repository").data == "inmemory":
        _repo_client = ClientRepo()
        _repo_movie = MovieRepo()
        _repo_rental = RentalRepo()

    elif config.get("repository").data == "textfiles":
        _repo_client = ClientTextFileRepo(config.get("clients").data)
        _repo_movie = MovieTextFileRepo(config.get("movies").data)
        _repo_rental = RentalTextFileRepo(config.get("rentals").data)

    elif config.get("repository").data == "binary":
        _repo_client = ClientBinaryRepo(config.get("clients").data)
        _repo_movie = MovieBinaryRepo(config.get("movies").data)
        _repo_rental = RentalBinaryRepo(config.get("rentals").data)

    _history_repo = HistoryRepository()
    _services_client = ClientService(_repo_client)
    _services_movie = MovieService(_repo_movie)
    _services_rental = RentalService(_repo_rental, _repo_movie, _repo_client)
    _services_history = HistoryService(_history_repo, _repo_client, _repo_movie, _repo_rental)
    _ui = Ui(_services_client, _services_movie, _services_rental, _services_history)
    _ui.start()


main()