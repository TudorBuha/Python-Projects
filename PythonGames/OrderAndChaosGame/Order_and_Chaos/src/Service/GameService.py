from src.Domain.Entities import Board, GameError
from src.Repository.GameRepository import GameRepository

import random
import uuid

class GameService:
    def __init__(self):
        self.board = Board()
        self.repository = GameRepository()

    def start_new_game(self):
        self.board = Board()

    def save_and_exit(self):
        game_id = str(uuid.uuid4())[:8]  # Generate a short unique ID for the game
        filename = f"game_{game_id}.txt"
        self.repository.save_game(self.board, filename)
        self.repository.register_game(game_id, filename)
        return game_id

    def list_games(self):
        return self.repository.list_saved_games()

    def load_game_by_id(self, game_id):
        games = self.list_games()
        for game in games:
            if game.startswith(game_id):
                _, filename = game.split(',')
                return self.repository.load_game(self.board, filename)
        return False

    def make_move(self, player, x, y):
        symbol = 'X' if player == 'order' else 'O'
        try:
            self.board.make_move(x, y, symbol)
            if self.board.check_winner():
                return f"{player.capitalize()} wins!"
            if self.board.is_full():
                return "The board is full, Chaos wins!"
            return "Move registered."
        except GameError as e:
            return str(e)

    def find_threats_and_block(self, symbol):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.board[i][j] == ".":
                    # Temporarily make a move for the player
                    self.board.board[i][j] = symbol
                    if self.board.check_winner() == "Order":
                        # Undo the temporary move
                        self.board.board[i][j] = "."
                        # Make a blocking move
                        self.board.board[i][j] = 'O' if symbol == 'X' else 'X'
                        return True
                    else:
                        # Undo the temporary move
                        self.board.board[i][j] = "."
        return False
    def computer_move(self):
        # Try to block 'X' and 'O' threats
        if not self.find_threats_and_block('X'):
            if not self.find_threats_and_block('O'):
                # If no immediate block needed, make a random move
                while True:
                    x, y = random.randint(0, self.board.size-1), random.randint(0, self.board.size-1)
                    if self.board.board[x][y] == ".":
                        self.board.make_move(x, y, 'O')
                        break

    def save_game(self):
        self.repository.save_game(self.board)
        return "Game saved."

    def load_game(self):
        if self.repository.load_game(self.board):
            return "Game loaded successfully."
        else:
            return "No saved game found. Starting a new game."

    def get_game_board(self):
        return str(self.board)
