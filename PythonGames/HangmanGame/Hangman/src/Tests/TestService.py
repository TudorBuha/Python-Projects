import unittest
from src.Repository.SentenceRepo import SentenceRepository
from src.Service.HangmanService import HangmanService
from src.Domain.Sentence import Sentence

class MockRepository(SentenceRepository):
    def __init__(self):
        super().__init__("unused.txt")  # Filename is unused in mock
        self._sentences = [Sentence("Test sentence")]

class TestHangmanService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MockRepository()
        self.service = HangmanService(self.mock_repo)

    def test_start_new_game(self):
        self.service.start_new_game()
        self.assertIsNotNone(self.service.current_game, "A new game should be started")

    def test_guess_letter_correct(self):
        self.service.start_new_game()
        self.service.guess_letter('t')  # Known letter in "Test sentence"
        # Check if 't' is revealed
        self.assertIn('T', str(self.service.current_game.sentence), "Letter T should be revealed")



if __name__ == '__main__':
    unittest.main()
