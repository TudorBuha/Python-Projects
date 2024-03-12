from src.services.MovieService import *
from src.services.ClientService import *
from src.services.RentalService import *

class UI:
    @staticmethod
    def print_menu():
        print("Menu")
        print("1 - Add a client")
        print("2 - Remove a client")
        print("3 - Update a client's name")
        print("4 - Display the clients")
        print("5 - Add a movie")
        print("6 - Remove a movie")
        print("7 - Update a movie's title")
        print("8 - Update a movie's description")
        print("9 - Update a movie's genre")
        print("10 - Display the movies")
        print("11 - Rent a movie")
        print("12 - Return a movie")
        print("13 - Display rentals")
        print("14 - Search by a movie's title")
        print("15 - Search by a movie's description")
        print("16 - Search by a movie's genre")
        print("17 - Search by a client's name")
        print("18 - Most rented movies")
        print("19 - Most active clients")
        print("20 - Late rentals")
        print("0 - Exit")

    def __init__(self, client_services: ClientServices, movie_services: MovieService, rental_services: RentalServices):
        self.__rental_services = rental_services
        self.__client_services = client_services
        self.__movie_services = movie_services

    def start(self):
        self.print_menu()
        self.__movie_services.generate()
        self.__client_services.generate()
        self.__rental_services.generate()
        while True:
            try:
                users_choice = int(input(">>"))

                add_client = 1
                remove_client = 2
                update_client_name = 3
                display_clients = 4
                add_movie = 5
                remove_movie = 6
                update_title = 7
                update_description = 8
                update_genre = 9
                display_movies = 10
                rent_movie = 11
                return_movie = 12
                display_rentals = 13
                search_by_title = 14
                search_by_description = 15
                search_by_genre = 16
                search_by_client_name = 17
                most_rented_movies = 18
                most_active_clients = 19
                late_rentals = 20
                exit = 0







                if users_choice == add_client:
                    clients_id = int(input("Client's ID: "))
                    clients_name = input("Client's name: ")
                    client = Client(clients_id, clients_name)
                    self.__client_services.add_client(client)

                elif users_choice == remove_client:
                    clients_id_to_be_removed = int(input("Client's ID: "))
                    self.__client_services.remove(clients_id_to_be_removed)

                elif users_choice == update_client_name:
                    clients_id_to_be_updated = int(input("Client's ID: "))
                    new_clients_name = input("New name: ")
                    self.__client_services.update_name(new_clients_name, clients_id_to_be_updated)

                elif users_choice == display_clients:
                    client_list = self.__client_services.display_client()
                    for each_client in client_list:
                        print(each_client)

                elif users_choice == add_movie:
                    movies_id = int(input("Movie's ID: "))
                    movies_title = input("Movie's title: ")
                    movies_description = input("Movie's description: ")
                    movies_genre = input("Movie's genre: ")
                    movie = Movie(movies_id, movies_title, movies_description, movies_genre)
                    self.__movie_services.add_movie(movie)

                elif users_choice == remove_movie:
                    clients_id_to_be_removed = int(input("Movie's ID: "))
                    self.__movie_services.remove(clients_id_to_be_removed)

                elif users_choice == update_title:
                    movies_id = int(input("Movie's ID: "))
                    new_title = input("New title: ")
                    self.__movie_services.update_title(new_title, movies_id)

                elif users_choice == update_description:
                    movies_id = int(input("Movie's ID: "))
                    new_description = input("New description: ")
                    self.__movie_services.update_description(new_description, movies_id)

                elif users_choice == update_genre:
                    movies_id = int(input("Movie's ID: "))
                    new_genre = input("New genre: ")
                    self.__movie_services.update_genre(new_genre, movies_id)

                elif users_choice == display_movies:
                    movie_list = self.__movie_services.display_movie()
                    for each_movie in movie_list:
                        print(each_movie)

                elif users_choice == rent_movie:
                    rentals_id = int(input("Rental's ID: "))
                    movie_id = int(input("Movie's ID: "))
                    client_id = int(input("Client's ID: "))
                    rented_date = input("Rented date is: ")
                    due_date = input("Due date is: ")
                    rental = Rental(rentals_id, movie_id, client_id, rented_date, due_date, None)
                    self.__rental_services.add_rental(rental)

                elif users_choice == return_movie:
                    rentals_id = int(input("Rental's ID: "))
                    new_returned_date = input("Returned date is: ")
                    self.__rental_services.update_rentals(rentals_id, new_returned_date)

                elif users_choice == display_rentals:
                    rental_list = self.__rental_services.display_rentals()
                    for each_rental in rental_list:
                        print(each_rental)

                elif users_choice == search_by_title:
                    title_for_search = input("Introduce the title for the search: ")
                    same_title_ish_movie_list = self.__movie_services.search_by_title(title_for_search)
                    for each_movie in same_title_ish_movie_list:
                        print(each_movie)

                elif users_choice == search_by_description:
                    description_for_search = input("Introduce the description for the search: ")
                    same_description_ish_movie_list = self.__movie_services.search_by_description(description_for_search)
                    for each_movie in same_description_ish_movie_list:
                        print(each_movie)

                elif users_choice == search_by_genre:
                    genre_search = input("Introduce the genre for the search: ")
                    same_genre_ish_movie_list = self.__movie_services.search_by_genre(genre_search)
                    for each_movie in same_genre_ish_movie_list:
                        print(each_movie)

                elif users_choice == search_by_client_name:
                    name_to_search_for = input("Introduce the name for the: ")
                    same_name_ish_movie_list = self.__client_services.search_by_name(name_to_search_for)
                    for each_movie in same_name_ish_movie_list:
                        print(each_movie)

                elif users_choice == most_rented_movies:
                    most_rented_movie_list = self.__rental_services.most_rented_movies()
                    for a_movie in most_rented_movie_list:
                        print("The movie's ID is", a_movie["movie_id"], "and it was rented", a_movie["number"], "day(s)", self.__movie_services.get_movie_by_id(a_movie["movie_id"]))

                elif users_choice == most_active_clients:
                    most_active_clients_list = self.__rental_services.most_active_clients()
                    for a_client in most_active_clients_list:
                        print("The client's ID is", a_client["client_id"], "and he rented movies for", a_client["number"], "days", self.__client_services.get_client_by_id(a_client["client_id"]))

                elif users_choice == late_rentals:
                    late_rental_list = self.__rental_services.late_rentals()
                    for a_rental in late_rental_list:
                        print("Number of days late", a_rental["days_late"], "for Rental ID", a_rental["rental_id"], self.__movie_services.get_movie_by_id(a_rental["movie_id"]))
                elif users_choice == exit:
                    print("Bye!")
                    break
                else:
                    print("Invalid option!")
            except Exception as ex:
                print(ex)
