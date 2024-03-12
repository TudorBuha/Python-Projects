class Game:
    def __init__(self, sentence):
        self.sentence = sentence
        self.failed_attempts = 0
        self.hangman_state = ['_'] * 7  # "hangman" has 7 letters

    def guess_letter(self, letter):
        if not self.sentence.reveal_letter(letter):
            self.failed_attempts += 1
            # Update the hangman state to reveal the next letter
            if self.failed_attempts <= len("hangman"):
                self.hangman_state[self.failed_attempts - 1] = "hangman"[self.failed_attempts - 1]

    def get_hangman_state(self):
        return ''.join(self.hangman_state)

    def is_lost(self):
        return self.failed_attempts >= len("hangman")  # Game is lost if all letters of "hangman" are revealed


    def is_won(self):
        return self.sentence.is_fully_revealed()
