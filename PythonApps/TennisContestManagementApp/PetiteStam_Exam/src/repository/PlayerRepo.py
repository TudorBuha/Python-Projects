from src.domain.Player import *
class PlayerRepository:
    def __init__(self):
        self._players = []

    def read_players(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(', ')
            if len(data) == 3:
                player = Player(int(data[0]), data[1], int(data[2]))
                self._players.append(player)
            else:
                print(f"Invalid data format in line: {line}")

    def get_players(self):
        return self._players