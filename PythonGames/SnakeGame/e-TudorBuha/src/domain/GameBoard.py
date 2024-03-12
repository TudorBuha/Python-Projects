class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def add_snake(self, snake):
        if not snake.segments:
            return

        head = snake.segments[0]
        if 0 <= head.x < self.size and 0 <= head.y < self.size:
            self.board[head.y][head.x] = '*'

        for segment in snake.segments[1:]:
            if 0 <= segment.x < self.size and 0 <= segment.y < self.size:
                self.board[segment.y][segment.x] = '+'

    def add_apple(self, apple):
        if 0 <= apple.x < self.size and 0 <= apple.y < self.size:
            self.board[apple.y][apple.x] = 'A'

    def clear(self):
        for y in range(self.size):
            for x in range(self.size):
                self.board[y][x] = ' '


