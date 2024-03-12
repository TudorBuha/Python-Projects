class GameRepository:
    def __init__(self, registration_file='game_registry.txt'):
        self.registration_file = registration_file

    def list_saved_games(self):
        try:
            with open(self.registration_file, 'r') as file:
                games = file.readlines()
            return [game.strip() for game in games]
        except FileNotFoundError:
            return []

    def register_game(self, game_id, filename):
        with open(self.registration_file, 'a') as file:
            file.write(f"{game_id},{filename}\n")

    def save_game(self, board):
        with open(self.filename, 'w') as file:
            for row in board.board:
                file.write(''.join(row) + "\n")

    def load_game(self, board):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    board.board[i] = list(line.strip())
            return True
        except FileNotFoundError:
            return False
