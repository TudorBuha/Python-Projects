import random
from src.Domain.Game import Game
from src.Domain.Sentence import Sentence


class HangmanService:
    def __init__(self, sentence_repository):
        self._sentence_repository = sentence_repository
        self.current_game = None

    def _reveal_first_and_last_letters(self, sentence):
        words = sentence.content.split()
        for word in words:
            if len(word) > 1:
                first_letter, last_letter = word[0], word[-1]
                sentence.reveal_letter(first_letter)
                sentence.reveal_letter(last_letter)
            elif len(word) == 1:  # For single-letter words, just reveal that letter
                sentence.reveal_letter(word[0])

    def start_new_game(self):
        sentences = self._sentence_repository.get_sentences()
        if sentences:
            chosen_sentence = random.choice(sentences)
            self.current_game = Game(chosen_sentence)
            self._reveal_first_and_last_letters(self.current_game.sentence)
        else:
            raise ValueError("No sentences available to start a game.")


    def guess_letter(self, letter):
        if not self.current_game:
            raise ValueError("Game not started.")
        self.current_game.guess_letter(letter)
        if self.current_game.is_lost():
            return "Game Over. You lost!"
        elif self.current_game.is_won():
            return "Congratulations! You won!"
        else:
            return str(self.current_game.sentence)

    def add_sentence(self, content):
        # Validate the sentence to have at least one word with three or more letters
        if not any(len(word) >= 3 for word in content.split()):
            print("Sentence must contain at least one word with at least 3 letters.")
            return False
        # Check and add the sentence through the repository, preventing duplicates
        if self._sentence_repository.add_sentence(content):
            print("Sentence added successfully.")
            return True
        else:
            return False

