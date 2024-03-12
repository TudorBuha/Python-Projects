import random

class Word:
    def __init__(self, text):
        self.original_text = text
        self.scrambled_text = self._scramble_text()
        self.score = len(text)  # Initial score is the length of the text

    def _scramble_text(self):
        if len(self.original_text) <= 3:
            return self.original_text  # Not enough length to scramble

        text_array = list(self.original_text)
        middle = text_array[1:-1]
        random.shuffle(middle)
        return text_array[0] + ''.join(middle) + text_array[-1]

    def swap_letters(self, index1, index2):
        if index1 == index2 or not (0 <= index1 < len(self.scrambled_text)) or not (0 <= index2 < len(self.scrambled_text)):
            return False  # Invalid indices or no swap needed

        scrambled_array = list(self.scrambled_text)
        scrambled_array[index1], scrambled_array[index2] = scrambled_array[index2], scrambled_array[index1]
        self.scrambled_text = ''.join(scrambled_array)

        # Score update logic can be implemented here
        return True  # Swap was successful

    def is_solved(self):
        return self.scrambled_text == self.original_text