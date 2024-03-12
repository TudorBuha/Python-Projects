from src.domain.GameBoard import GameBoard
from src.domain.Apple import Apple
from src.domain.Snake import Snake, Segment

import random

class GameService:
    def __init__(self, board, snake, apples = None):
        self.board = board
        self.snake = snake
        self.apples = apples
        self.game_over = False

    def update(self):
        self.snake.move()
        self.check_collision()
        self.board.clear()
        self.board.add_snake(self.snake)
        for apple in self.apples:
            self.board.add_apple(apple)

    def check_collision(self):
        head = self.snake.segments[0]
        # Check for collision with walls
        if head.x < 0 or head.x >= self.board.size or head.y < 0 or head.y >= self.board.size:
            self.game_over = True
            return

        # Check for collision with itself
        for segment in self.snake.segments[1:]:
            if head.x == segment.x and head.y == segment.y:
                self.game_over = True
                return

        # Check for collision with any apple
        for apple in self.apples:
            if head.x == apple.x and head.y == apple.y:
                self.snake.grow()
                self.apples.remove(apple)  # Remove the eaten apple
                self.place_new_apples()
                break

    def place_new_apples(self, count=1):
        for _ in range(count):
            apple_position = self.get_random_empty_position()
            if apple_position:
                self.apples.append(Apple(*apple_position))
            else:
                break

    def get_random_empty_position(self):
        empty_positions = [(x, y) for x in range(self.board.size) for y in range(self.board.size)
                           if not any(segment.x == x and segment.y == y for segment in self.snake.segments)
                           and not any(apple.x == x and apple.y == y for apple in self.apples)]
        return random.choice(empty_positions) if empty_positions else None

    def is_game_over(self):
        return self.game_over
