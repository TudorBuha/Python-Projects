import unittest

from src.domain.Client import Client
from src.repository.ClientRepo import *

class TestClientRepo(unittest.TestCase):

    def setUp(self):
        self.client_repo = ClientRepo()
        self.client_repo2 = ClientTextFileRepo("clientteststext.txt")
        self.client_repo3 = ClientBinaryRepo("clientbinary.bin")


    def test_add_client(self):
        # Test adding a new client
        client = Client(len(self.client_repo.get_all_clients()) + 1, name="John Doe")
        self.client_repo.add_client(client)
        self.assertIn(client, self.client_repo.get_all_clients())
        self.client_repo.remove(client.client_id)

    def test_add_client2(self):
        client = Client( len(self.client_repo2.get_all_clients()) + 1, name="Coco")
        self.client_repo2.add_client(client)
        self.assertIn(client, self.client_repo2.get_all_clients())
        self.client_repo2.remove(client.client_id)
    def test_add_client3(self):
        clientel = Client(len(self.client_repo3.get_all_clients()) + 1, name= "Oana")
        self.client_repo3.add_client(clientel)
        self.assertIn(clientel, self.client_repo3.get_all_clients())
        self.client_repo3.remove(clientel.client_id)



    def test_get_all_clients(self):
        array = []
        for el in self.client_repo.get_all_clients():
            array.append(el)

        # Test getting all clients after adding some clients
        clients = [
            Client(client_id=70, name="John Doe"),
            Client(client_id=71, name="Jane Doe"),
            Client(client_id=72, name="Bob Smith")
        ]
        for client in clients:
            self.client_repo.add_client(client)
        self.assertEqual(self.client_repo.get_all_clients(), array + clients)
        self.client_repo.remove(70)
        self.client_repo.remove(71)
        self.client_repo.remove(72)


    def test_get_all_clients2(self):
        array = []
        for el in self.client_repo2.get_all_clients():
            array.append(el)

        clients = [
            Client(client_id=80, name="David Johnson"),
            Client(client_id=81, name="William Boney"),
            Client(client_id=82, name="Coochie Patoochie")
        ]
        for client in clients:
            self.client_repo2.add_client(client)
        self.assertEqual( self.client_repo2.get_all_clients(), array + clients)
        self.client_repo2.remove(80)
        self.client_repo2.remove(81)
        self.client_repo2.remove(82)




    def test_get_all_clients3(self):
        array = []
        for el in self.client_repo3.get_all_clients():
            array.append(el)

        clients = [
            Client(client_id=90, name="Steve Wonder"),
            Client(client_id=91, name= "Marie Stew"),
            Client(client_id=92, name= "Lary Mandel")
        ]
        for client in clients:
            self.client_repo3.add_client(client)
        self.assertEqual(self.client_repo3.get_all_clients(), array + clients)
        self.client_repo3.remove(90)
        self.client_repo3.remove(91)
        self.client_repo3.remove(92)

    def test_update(self):
        # Test updating the name of an existing client
        client = Client(len(self.client_repo.get_all_clients()) + 1, name="John Doe")
        self.client_repo.add_client(client)
        new_name = "John Updated"
        self.client_repo.update(client.client_id, new_name)
        self.assertEqual(client.name, new_name)
        initial_name="John Doe"
        self.client_repo.update(client.client_id, initial_name)

    def test_update2(self):
        client= Client(len(self.client_repo2.get_all_clients()) + 1, name="Luchian Cosmin")
        self.client_repo2.add_client(client)
        new_name="updated name"
        self.client_repo2.update(client.client_id, new_name)
        self.assertEqual(client.name, new_name)
        initial_name = "Luchian Cosmin"
        self.client_repo2.update(client.client_id, initial_name)
    def test_update3(self):
        client= Client(len(self.client_repo3.get_all_clients()) + 1, name="Bartholomeo")
        self.client_repo3.add_client(client)
        new_name="updated name"
        self.client_repo3.update(client.client_id, new_name)
        self.assertEqual(client.name, new_name)
        initial_name = "Bartholomeo"
        self.client_repo3.update(client.client_id, initial_name)
    def test_remove(self):
        # Test removing an existing client
        client = Client(len(self.client_repo.get_all_clients()) + 1, name="John Doe")
        self.client_repo.add_client(client)
        self.client_repo.remove(client.client_id)
        self.assertNotIn(client, self.client_repo.get_all_clients())
    def tets_remove2(self):
        client = Client(len(self.client_repo2.get_all_clients()) + 1, name= "Johnny Deep")
        self.client_repo2.add_client(client)
        self.client_repo2.remove(client.client_id)
        self.assertNotIn(client, self.client_repo2.get_all_clients())



if __name__ == '__main__':
    unittest.main()