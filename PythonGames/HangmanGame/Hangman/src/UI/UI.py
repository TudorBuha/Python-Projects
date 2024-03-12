from src.Service.HangmanService import HangmanService

class HangmanConsoleUI:
    def __init__(self, hangman_service):
        self._hangman_service = hangman_service

    def add_sentence_ui(self):
        sentence = input("Enter a new sentence: ")
        # The service method now handles printing feedback directly.
        self._hangman_service.add_sentence(sentence)

    def add_sentence(self, content):
        # Assuming SentenceRepository's add_sentence now returns True if added, False if not
        return self._sentence_repository.add_sentence(content)

    def play_game_ui(self):
        self._hangman_service.start_new_game()
        print("Game started. Try to guess the sentence!")

        while True:
            print(self._hangman_service.current_game.sentence)
            print(f"Hangman: {self._hangman_service.current_game.get_hangman_state()}")
            guess = input("Enter a letter: ")
            self._hangman_service.guess_letter(guess)

            if self._hangman_service.current_game.is_lost():
                print(f"Game Over. You lost!")
                break
            elif self._hangman_service.current_game.is_won():
                print("Congratulations! You won!")
                break
            else:
                print("Keep guessing...")

    def start(self):
        while True:
            print("1. Add a new sentence")
            print("2. Play Hangman")
            print("0. Exit")

            option = input("Choose an option: ")
            if option == '1':
                self.add_sentence_ui()
            elif option == '2':
                self.play_game_ui()
            elif option == '0':
                break
            else:
                print("Invalid option!")
