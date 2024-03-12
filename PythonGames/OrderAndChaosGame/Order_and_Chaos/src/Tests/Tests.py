import unittest
from src.Service.GameService import GameService

class TestComputerMoves(unittest.TestCase):

    def setUp(self):
        self.game_service = GameService()

    def test_block_horizontal_win(self):
        # Simulate a board state where 'X' is about to win horizontally
        self.game_service.board.board = [
            ['X', 'X', 'X', 'X', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']
        ]
        self.game_service.computer_move()
        # Check if the computer blocks the win
        self.assertEqual(self.game_service.board.board[0][4], 'O', "Computer failed to block horizontal win")

    def test_block_vertical_win(self):
        # Simulate a board state where 'X' is about to win vertically
        self.game_service.board.board = [
            ['X', '.', '.', '.', '.', '.'],
            ['X', '.', '.', '.', '.', '.'],
            ['X', '.', '.', '.', '.', '.'],
            ['X', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']
        ]
        self.game_service.computer_move()
        # Check if the computer blocks the win
        self.assertEqual(self.game_service.board.board[4][0], 'O', "Computer failed to block vertical win")

    def test_block_diagonal_win(self):
        # Simulate a board state where 'X' is about to win diagonally
        self.game_service.board.board = [
            ['X', '.', '.', '.', '.', '.'],
            ['.', 'X', '.', '.', '.', '.'],
            ['.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', 'X', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']
        ]
        self.game_service.computer_move()
        # Check if the computer blocks the win
        self.assertEqual(self.game_service.board.board[4][4], 'O', "Computer failed to block diagonal win")


if __name__ == "__main__":
    unittest.main()
