from texttable import Texttable


class GameError(Exception):
    pass


class Board:
    def __init__(self):
        self.size = 6
        self.board = [["." for _ in range(self.size)] for _ in range(self.size)]

    def make_move(self, x, y, symbol):
        if not (0 <= x < self.size and 0 <= y < self.size):
            raise GameError("Move out of board bounds.")
        if self.board[x][y] != ".":
            raise GameError("Cell is already occupied.")
        if symbol not in ("X", "O"):
            raise GameError("Invalid symbol. Use 'X' or 'O'.")
        self.board[x][y] = symbol

    def is_full(self):
        return all(cell != "." for row in self.board for cell in row)

    def check_winner(self):
        # Check rows and columns for 5 consecutive identical symbols
        for i in range(self.size):
            for symbol in ["X", "O"]:
                # Check rows
                if any(self.board[i][j:j + 5] == [symbol] * 5 for j in range(self.size - 4)):
                    return "Order"
                # Check columns
                if any([self.board[j + k][i] for k in range(5)] == [symbol] * 5 for j in range(self.size - 4)):
                    return "Order"

        # Check diagonals
        for symbol in ["X", "O"]:
            for i in range(self.size - 4):
                for j in range(self.size - 4):
                    # Diagonal from top-left to bottom-right
                    if all(self.board[i + k][j + k] == symbol for k in range(5)):
                        return "Order"
                    # Diagonal from bottom-left to top-right
                    if all(self.board[i + k][j + 4 - k] == symbol for k in range(5)):
                        return "Order"

        # If the board is full and no winner, Chaos wins
        if all(self.board[i][j] != "." for i in range(self.size) for j in range(self.size)):
            return "Chaos"

        # No winner yet
        return None

    def check_winner3(self):
        # Placeholder for simplified logic
        # This should be replaced with actual game logic
        return False

    def check_winner2(self):
        # Check rows for 5 same symbols in a row
        for row in self.board:
            if self.check_sequence(row):
                return True

        # Check columns for 5 same symbols in a row
        for col in range(self.size):
            column = [self.board[row][col] for row in range(self.size)]
            if self.check_sequence(column):
                return True

        # Check diagonals
        diag1 = [self.board[i][i] for i in range(self.size)]
        diag2 = [self.board[i][self.size - i - 1] for i in range(self.size)]
        if self.check_sequence(diag1) or self.check_sequence(diag2):
            return True

        return False

    def check_sequence(self, sequence):
        return any(sequence[i:i + 5] == [sequence[i]] * 5 for i in range(len(sequence) - 4))

    def __str__(self):
        table = Texttable()
        table.set_cols_align(["c"] * self.size)
        table.set_cols_valign(["m"] * self.size)
        table.add_rows(self.board, header=False)
        return table.draw()
