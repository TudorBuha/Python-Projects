from src.domain.Client import *
from random import randint, choice
import pickle
import json


class NotUniqueClientIdError(Exception):
    def __init__(self, client_id):
        self.__client_id = client_id

    def __str__(self):
        return str(self.__client_id) + " is not an unique client id "


class NotFoundID(Exception):
    def __init__(self, entity_id):
        self.__entity_id = entity_id

    def __str__(self):
        return str(self.__entity_id) + " this id is not found"


class ClientRepo:
    def __init__(self):
        self._client_list = []

    def generate(self):
        """
        Generates 20 random clients
        :return:
        """
        name_list = ["Tudor", "John", "Mary", "Bob", "Alice", "Mark", "Megan", "James", "Lily", "Michael", "Emma",
                     "David", "Olivia", "Richard", "Sophia", "Joseph", "Elizabeth", "Thomas", "Grace", "Charles",
                     "Sarah"]
        family_name_list = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez",
                            "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin",
                            "Jackson", "Thompson", "White"]
        for i in range(1, 21):
            client_id = i
            client_name = choice(name_list) + " " + choice(family_name_list)
            client = Client(client_id, client_name)
            self._client_list.append(client)

    def add_client(self, client):
        if self.already_exists_client(client) is False:
            raise NotUniqueClientIdError(client.client_id)
        self._client_list.append(client)

    def display_clients(self):
        return self._client_list

    def update_name(self, new_client, client_id):
        found = False
        for client in self._client_list:
            if int(client_id) == int(client.client_id):
                found = True
                client.name = str(new_client)
                break
        if found is False:
            raise NotFoundID(client_id)

    def remove(self, client_id):
        found = False
        for client in self._client_list:
            if int(client_id) == int(client.client_id):
                self._client_list.remove(client)
                found = True
        if found == False:
            raise NotFoundID(client_id)

    def search_by_name(self, name_to_search_for):
        client_name_list = []
        for client in self._client_list:
            copy_name = client.name
            if name_to_search_for.lower() in copy_name.lower():
                client_name_list.append(client)
        return client_name_list

    def get_client_by_id(self, id_to_search_for):
        for client in self._client_list:
            if client.client_id == id_to_search_for:
                return client

    def already_exists_client(self, client_to_search_for):
        for current_client in self._client_list:
            if current_client.client_id == client_to_search_for.client_id:
                return False
        return True