from src.Domain.Game import Game

class GameService:
    def __init__(self, word_repository):
        self.word_repository = word_repository
        self.current_game = None

    def start_new_game(self):
        # Load the initial word from the repository
        initial_word = self.word_repository.load_initial_word()
        # Create a new game instance with the loaded word
        self.current_game = Game(initial_word)
        # Return the scrambled word to display in the UI
        return self.current_game.start()

    def swap_letters(self, index1, index2):
        # Perform the swap operation using the Game instance
        if not self.current_game:
            raise Exception("No game is currently running.")

        # Validate indices and perform the swap
        if self.current_game.swap_letters(index1, index2):
            # Optionally, save the game state after each move
            self.word_repository.save_game_state(self.current_game.current_state())
            return True
        else:
            return False

    def undo_last_swap(self):
        # Undo the last swap operation
        if not self.current_game:
            raise Exception("No game is currently running.")
        self.current_game.undo_last_swap()
        # Optionally, save the game state after undo operation
        self.word_repository.save_game_state(self.current_game.current_state())

    def get_game_state(self):
        # Get the current state of the game
        if not self.current_game:
            raise Exception("No game is currently running.")
        return self.current_game.current_state()
