#!/bin/python3
import pygame
from game_logic import game_logic
from base_config import base_config

pygame.init()


def main():
    """Main Method"""

    # Decare variables
    X_AXIS, Y_AXIS = 800, 720
    start_game = True

    # Configure screen and import background
    base = base_config(x_axis=X_AXIS, y_axis=Y_AXIS)
    screen = base.configure_screen()
    background = base.import_background()

    # Start game loop
    game = game_logic(screen=screen, background=background)
    game.main_loop(start_game)

    pygame.quit()


if __name__ == "__main__":
    main()
