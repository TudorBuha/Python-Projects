class WordRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_initial_word(self):
        # Load the initial word or sentence from a text file
        try:
            with open(self.file_path, 'r') as file:
                # Assuming the first line contains the word or sentence
                initial_word = file.readline().strip()
                return initial_word
        except FileNotFoundError:
            raise Exception(f"The file at {self.file_path} was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading from {self.file_path}: {e}")

    def save_game_state(self, game_state):
        # Save the current game state to a file (if needed)
        try:
            with open(self.file_path, 'a') as file:
                file.write(f"{game_state}\n")
        except Exception as e:
            raise Exception(f"An error occurred while writing to {self.file_path}: {e}")
