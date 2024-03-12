from src.Domain.Sentence import Sentence

class SentenceRepository:
    def __init__(self, filename):
        self._filename = filename
        self._sentences = []
        self._load()

    def _load(self):
        try:
            with open(self._filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self._sentences.append(Sentence(line))
        except FileNotFoundError:
            print(f"No such file: {self._filename}")

    def get_sentences(self):
        return self._sentences

    def add_sentence(self, content):
        if any(sentence.content.lower() == content.lower() for sentence in self._sentences):
            print("This sentence already exists. Not adding duplicate.")
            return False
        self._sentences.append(Sentence(content))
        self._save()
        return True

    def _save(self):
        with open(self._filename, 'w') as file:
            for sentence in self._sentences:
                file.write(sentence.content + '\n')
