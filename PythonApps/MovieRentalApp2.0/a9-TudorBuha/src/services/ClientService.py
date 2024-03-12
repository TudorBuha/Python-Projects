from src.domain.Client import *
from src.repository.ClientRepo import *


class ClientService:
    def __init__(self, client_repo: ClientRepo):
        self.__repo = client_repo
       # self.get_all_generated_clients()




    def add_client(self, client):
        """
        Function that adds a client to the list
        :param client: object of type Client
        :return:
        """
        self.__repo.add_client(client)


    def get_all_clients(self):
        """
        Function that returns the list of clients
        :return:
        """
        return self.__repo.get_all_clients()

    def remove(self, client_id:int):
        """
        Function that removes a client
        :param client_id: id of the client to be removed
        :return:
        """
        self.__repo.remove(client_id)

    def update(self, cl_id: int, new_name):
        """
        Function that updates a client
        :param cl_id: id of the client to be updated
        :param new_name: name that will replace the old one
        :return:
        """
        self.__repo.update(cl_id, new_name)

    def search(self, search_string: str):
        """
        Function that searches a client by name
        :param search_string: string to be searched
        :return:
        """
        return self.__repo.search(search_string)

    def get_client_by_id(self, id: int):
        """
        Function that returns a client by id
        :param id: id of the client to be returned
        :return:
        """
        return self.__repo.get_client_by_id(id)

