class Sentence:
    def __init__(self, content):
        self.content = content
        self.discovered = ['_' if c != ' ' else ' ' for c in content]


    def reveal_letter(self, letter):
        revealed = False
        for idx, char in enumerate(self.content):
            if char.lower() == letter.lower():
                self.discovered[idx] = self.content[idx]
                revealed = True
        return revealed

    def is_fully_revealed(self):
        return '_' not in self.discovered

    def __str__(self):
        return ''.join(self.discovered)
