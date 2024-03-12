import pickle

from src.domain.Client import *
class NotUniqueClientIdError(Exception):
    def __init__(self, client_id):
        self.__client_id = client_id

    def __str__(self):
        return str(self.__client_id) + " is not an unique client id "

class NotFoundError(Exception):
    def __init__(self, entity_id):
        self.__entity_id = entity_id
    def __str__(self):
        return str(self.__entity_id) + " this id is not found"





class ClientRepo:
    def __init__(self):
        self._clientlist=[]
        self.generate_n_clients(20)

    def add_client(self, client:Client):
        """
        Function that adds a client to the list
        :param client: the client to be added
        :return:
        """
        if self.already_exists_client(client) is False:
            raise NotUniqueClientIdError(client.client_id)
        self._clientlist.append(client)

    def get_all_clients(self):
        """
        Function that returns the list of clients
        :return:
        """
        return self._clientlist
    def update(self, cl_id, new_name):
        """
        Function that updates a client
        :param cl_id: id of the client to be updated
        :param new_name: name that will replace the old one
        :return:
        """
        found=0
        for client in self._clientlist:
            if cl_id==client.client_id:
                client.name = new_name
                found=1

        if found==0:
            raise NotFoundError(cl_id)
    def remove(self, cl_id):
        """
        Function that removes a client
        :param cl_id: id of the client to be updated
        :return:
        """
        found=0
        for client in self._clientlist:
            if cl_id==client.client_id:
                found=1
                self._clientlist.remove(client)

        if found==0:
            raise NotFoundError(cl_id)

    def search(self, search_string: str):
        """
        Function that searches for a client
        :param search_string: the string to be searched
        :return:
        """
        result = []
        search_string = search_string.lower()
        for el in self._clientlist:
            if search_string in el.name.lower() or search_string in str(el.client_id).lower():
                result.append(el)
        return result

    def get_client_by_id(self, id: int):
        """
        Function that returns a client by id
        :param id:
        :return:
        """
        found=0
        for client in self._clientlist:
            if client.client_id == id:
                found=1
                return client

        if found==0:
            raise NotFoundError(id)


    def already_exists_client(self, client: Client):

        """
        Function that checks if a client already exists

        :param client: object of type Client
        :return:
        """
        for x in self._clientlist:

            if client.client_id == x.client_id:
                return False
        return True

    def generate_clients(self, idd: int):
        str1 = [
            "Alice Anderson",
            "Bob Brown",
            "Charlie Clark",
            "David Davis",
            "Emma Evans",
            "Frank Fisher",
            "Grace Garcia",
            "Henry Harrison",
            "Ivy Irwin",
            "Jack Johnson",
            "Katherine Khan",
            "Leo Lopez",
            "Mia Miller",
            "Nathan Nguyen",
            "Olivia Owens",
            "Peter Patel",
            "Quinn Quinn",
            "Rachel Reyes",
            "Samuel Smith",
            "Taylor Thompson"]

        id_ = idd
        name = random.choice(str1)

        return Client(id_, name)


    def generate_n_clients(self, n: int):
        for i in range(1, n + 1):
            new = self.generate_clients(i)
            self._clientlist.append(new)

class ClientTextFileRepo(ClientRepo):
    def __init__(self, file_name):
        self._clientlist=[]
        self.__file_name=file_name

        self.load()

    def load(self):
        try:
            file =open(self.__file_name, "r")
            values = file.readlines()
            for value in values:
                parsed_values = value.split("|")
                self.add_client(Client(int(parsed_values[0]), parsed_values[1].removesuffix("\n")))

            file.close()
        except FileNotFoundError as ve:
            self.generate_n_clients(20)
            self.save()
            pass

    def save(self):
        array=[]
        for client in self._clientlist:
             array.append(str(client.client_id) + "|" + str(client.name) + "\n")
        file=open(self.__file_name, "w")
        file.writelines(array)
        file.close()

    def add_client(self, clientel:Client):
        super().add_client(clientel)
        self.save()

    def update(self, id:int, name:str):
        super().update(id, name)
        self.save()

    def remove(self, id:int):
        super().remove(id)
        self.save()

class ClientBinaryRepo(ClientRepo):
    def __init__(self, file_name: str):
        self._clientlist = []
        self.__file_name = file_name

        self.load()


    def load(self):
        try:
            file = open(self.__file_name, "rb")
            self._clientlist = pickle.load(file)
            file.close()

        except:
            self.generate_n_clients(20)
            self.save()
            pass



    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._clientlist, file)
        file.close()

    def add_client(self, clientel:Client):
        super().add_client(clientel)
        self.save()

    def update(self, id:int, name:str):
        super().update(id, name)
        self.save()

    def remove(self, id:int):
        super().remove(id)
        self.save()

