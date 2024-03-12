from src.Repository.WordRepository import WordRepository
from src.Service.GameService import GameService
class GameUI:
    def __init__(self, game_service):
        self.game_service = game_service

    def display_welcome_message(self):
        print("Welcome to Scramble!")
        print("Try to unscramble the word to its original form.")
        print("Enter two indices to swap letters. Type 'undo' to revert the last swap.")
        print("Type 'exit' to quit the game.")

    def start_game(self):
        scrambled_word = self.game_service.start_new_game()
        print(f"Scrambled word: {scrambled_word}")

    def get_user_input(self):
        return input("Enter two indices to swap (or 'undo', 'exit'): ").strip()

    def play(self):
        self.display_welcome_message()
        self.start_game()

        while True:
            user_input = self.get_user_input()
            if user_input.lower() == 'exit':
                print("Exiting game.")
                break
            elif user_input.lower() == 'undo':
                self.game_service.undo_last_swap()
            else:
                try:
                    indices = [int(x) for x in user_input.split()]
                    if len(indices) != 2:
                        raise ValueError("Please enter exactly two indices.")
                    if self.game_service.swap_letters(indices[0], indices[1]):
                        game_state = self.game_service.get_game_state()
                        print(f"Current scramble: {game_state['scrambled_text']}")
                        print(f"Current score: {game_state['score']}")
                        if game_state['is_solved']:
                            print("Congratulations, you've unscrambled the word!")
                            break
                    else:
                        print("Swap failed. Try different indices.")
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"An error occurred: {e}")

        print("Game over.")


def main():
    word_repository = WordRepository('input.txt')
    game_service = GameService(word_repository)
    game_ui = GameUI(game_service)
    game_ui.play()

if __name__ == "__main__":
    main()