from src.repository.ClientRepo import *
from src.repository.HistoryRepo import *
from src.repository.MovieRepo import *
from src.repository.RentalRepo import *


class HistoryService:
    def __init__(self, history_repo: HistoryRepository, client_repo: ClientRepo, movie_repo: MovieRepo,
                 rental_repo: RentalRepo):
        self._repo = history_repo
        self._client_repo = client_repo
        self._movie_repo = movie_repo
        self._rental_repo = rental_repo

    def add_to_history(self, command_type: str, parameters: []):
        self._repo.add_to_history(HistoryCommand(command_type, parameters))

    def undo(self):
        try:
            last_command = self._repo.get_command()
            if self._repo.history_index > -1:
                self._repo.history_index -= 1
            self.map_command_and_execute(last_command)
        except IndexError as er:
            pass

    def redo(self):
        try:

            self._repo.history_index += 1
            last_command = self._repo.get_command()
            self.map_command_and_execute2(last_command)
        except IndexError as er:
            self._repo.history_index -= 1

    def map_command_and_execute(self, command: HistoryCommand):

        if command.command_type == "add client":
            self._client_repo.remove(command.parameters[0])

        elif command.command_type == "remove client":
            self._client_repo.add_client(Client(command.parameters[0], command.parameters[1]))
            for rental in command.parameters[2]:
                self._rental_repo.add_rental(rental)

        elif command.command_type == "update client":
            self._client_repo.update(command.parameters[0], command.parameters[1])

        elif command.command_type == "add movie":
            self._movie_repo.remove(command.parameters[0])

        elif command.command_type == "remove movie":
            self._movie_repo.add_movie(
                Movie(command.parameters[0], command.parameters[1], command.parameters[2], command.parameters[3]))
            for rental in command.parameters[4]:
                self._rental_repo.add_rental(rental)

        elif command.command_type == "update title":
            self._movie_repo.update_title(command.parameters[0], command.parameters[1])

        elif command.command_type == "update description":
            self._movie_repo.update_description(command.parameters[0], command.parameters[1])

        elif command.command_type == "update genre":
            self._movie_repo.update_genre(command.parameters[0], command.parameters[1])

        elif command.command_type == "add rental":
            self._rental_repo.remove_rental(command.parameters[0])

        elif command.command_type == "update rental":
            self._rental_repo.update_rental(command.parameters[0], command.parameters[6])

    def map_command_and_execute2(self, command: HistoryCommand):

        if command.command_type == "add client":
            self._client_repo.add_client(Client(command.parameters[0], command.parameters[1]))

        elif command.command_type == "remove client":
            self._client_repo.remove(command.parameters[0])
            for rental in command.parameters[2]:
                self._rental_repo.remove_rental(rental.rental_id)

        elif command.command_type == "update client":
            self._client_repo.update(command.parameters[0], command.parameters[1])

        elif command.command_type == "add movie":
            self._movie_repo.add_movie(
                Movie(command.parameters[0], command.parameters[1], command.parameters[2], command.parameters[3]))

        elif command.command_type == "remove movie":
            self._movie_repo.remove(command.parameters[0])
            for rental in command.parameters[4]:
                self._rental_repo.remove_rental(rental.rental_id)

        elif command.command_type == "update title":
            self._movie_repo.update_title(command.parameters[0], command.parameters[2])

        elif command.command_type == "update description":
            self._movie_repo.update_description(command.parameters[0], command.parameters[2])

        elif command.command_type == "update genre":
            self._movie_repo.update_genre(command.parameters[0], command.parameters[2])

        elif command.command_type == "add rental":
            self._rental_repo.remove_rental(command.parameters[0])

        elif command.command_type == "update rental":
            self._rental_repo.update_rental(command.parameters[0], command.parameters[5])