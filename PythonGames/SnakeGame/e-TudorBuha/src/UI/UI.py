from src.domain.GameBoard import GameBoard
from src.domain.Apple import Apple
from src.domain.Snake import Segment, Snake
from src.service.GameService import GameService

from texttable import Texttable
from random import random

class GameView:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        table = Texttable()
        for row in self.board.board:
            table.add_row(row)
        print(table.draw())

    def print_the_initial_board_with_all_instances(self, game_service):
        for apple in game_service.apples:
            self.board.add_apple(apple)
        self.board.add_snake(game_service.snake)
        self.draw_board()

class UI:
    def __init__(self, game_service):
        self.game_service = game_service
        self.game_view = GameView(game_service.board)

    def start(self):
        while not self.game_service.is_game_over():
            #self.game_view.draw_board()
            command = self.get_user_input()
            try:
                action, steps, direction = self.parse_command(command)
                self.execute_command(action, int(steps), direction)
                self.game_view.draw_board()
            except ValueError as e:
                print(e)
                print("Please enter a valid command, e.g., 'move 5 right'.")

    def get_user_input(self):
        print("Next command (e.g., 'move 5 right'): ", end='')
        return input().strip()

    def parse_command(self, command):
        parts = command.lower().split()
        if len(parts) != 3 or parts[0] != 'move' or not parts[1].isdigit() or parts[2] not in ['up', 'down', 'left', 'right']:
            raise ValueError("Invalid command format.")
        return parts[0], parts[1], parts[2]

    def execute_command(self, action, steps, direction):
        direction_mapping = {'up': 'UP', 'down': 'DOWN', 'left': 'LEFT', 'right': 'RIGHT'}
        for _ in range(steps):
            self.game_service.snake.change_direction(direction_mapping[direction])
            self.game_service.update()
            if self.game_service.is_game_over():
                print("Game over!")
                break