import unittest
from src.Repository.SentenceRepo import SentenceRepository
from src.Domain.Sentence import Sentence


class TestSentenceRepository(unittest.TestCase):
    def setUp(self):
        # Use a test file to prevent modifying actual sentences
        self.filename = "test_sentences.txt"
        with open(self.filename, 'w') as f:
            f.write("The quick brown fox\n")
        self.repo = SentenceRepository(self.filename)

    def test_add_sentence(self):
        self.repo.add_sentence("Jumps over the lazy dog")
        sentences = [sentence.content for sentence in self.repo.get_sentences()]
        self.assertIn("Jumps over the lazy dog", sentences, "Sentence should be added")

    def test_prevent_duplicates(self):
        initial_count = len(self.repo.get_sentences())
        self.repo.add_sentence("The quick brown fox")  # Duplicate
        self.assertEqual(len(self.repo.get_sentences()), initial_count, "Duplicate sentence should not be added")



if __name__ == '__main__':
    unittest.main()
