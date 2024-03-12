from src.Service.GameService import GameService

class GameUI:
    def __init__(self):
        self.service = GameService()

    def display_board(self):
        print(self.service.get_game_board())

    def prompt_move(self):
        try:
            x = int(input("Enter the row (0-5): "))
            y = int(input("Enter the column (0-5): "))
            if not (0 <= x < 6 and 0 <= y < 6):
                print("Invalid coordinates. Try again.")
                return None, None
            return x, y
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return None, None

    def play_game2(self):
        self.service.start_new_game()

        while True:
            self.display_board()
            print("Player's turn. Where would you like to place your piece?")
            x, y = self.prompt_move()

            if x is not None and y is not None:
                player_result = self.service.make_move('order', x, y)
                print(player_result)
                if player_result == "Order wins!":
                    print("Congratulations, you won!")
                    break

                # Computer's turn
                self.service.computer_move()
                print("Computer made its move.")
                if self.service.board.is_full():
                    print("The board is full, it's a draw!")
                    break

    def play_game(self):
        # Modify to include a command that saves the current game state and exits
        while True:
            command = input("Enter a command ('move', 'save'): ")
            if command == 'save':
                game_id = self.service.save_and_exit()
                print(f"Game saved with ID: {game_id}. Exiting.")
                break

    def start(self):
        action = input("Do you want to start a new game (n), load a saved game (l), or list saved games (s)? [n/l/s]: ").strip().lower()
        if action == 'l':
            game_id = input("Enter the game ID to load: ")
            if self.service.load_game_by_id(game_id):
                print("Game loaded successfully.")
            else:
                print("Game not found.")
        elif action == 's':
            saved_games = self.service.list_games()
            if saved_games:
                print("\n".join(saved_games))
            else:
                print("No saved games.")
        else:
            self.play_game()

if __name__ == "__main__":
    ui = GameUI()
    ui.start()
