from src.Domain.Word import Word
import random

class Game:
    def __init__(self, word_text):
        self.word = Word(word_text)
        self.moves_made = []  # Keep track of moves for undo feature

    def start(self):
        # Initially, no moves are made and the game starts with a scrambled word
        return self.word.scrambled_text

    def swap_letters(self, index1, index2):
        successful_swap = self.word.swap_letters(index1, index2)
        if successful_swap:
            self.moves_made.append((index1, index2))  # Record the move
        return successful_swap

    def undo_last_swap(self):
        if self.moves_made:
            last_move = self.moves_made.pop()
            self.word.swap_letters(*last_move)  # Swap back the last move

    def current_state(self):
        # Return the current game state information
        return {
            "scrambled_text": self.word.scrambled_text,
            "score": self.word.score,
            "original_text": self.word.original_text,  # This might be hidden depending on game rules
            "is_solved": self.word.is_solved()
        }