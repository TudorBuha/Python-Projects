from src.service.GameService import GameService
from src.domain.GameBoard import GameBoard
from src.domain.Snake import Snake, Segment
from src.domain.Apple import Apple
from src.UI.UI import UI, GameView

import random


def read_settings():
    settings = {}
    with open('settings.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            settings[key] = int(value)
    return settings

def main():
    settings = read_settings()
    board_size = settings['board_size']
    num_apples = settings['num_apples']

    board = GameBoard(board_size)
    snake = Snake(initial_position=(4, 4))
    apples = [Apple(x=3, y=3)]

    game_service = GameService(board, snake, apples)
    game_service.place_new_apples(num_apples - 1)

    game_view = GameView(board)
    game_view.print_the_initial_board_with_all_instances(GameService(board, snake, apples))

    ui = UI(game_service)
    ui.start()


if __name__ == "__main__":
    main()