import pygame
from pygame import Surface, display, event


class game_logic:
    def __init__(self, screen: Surface, background: Surface):
        self.screen = screen
        self.background = background

    def main_loop(self, game_loop: bool) -> None:
        """The main loop of the game"""

        while game_loop:
            game_loop = self.__quit_game()
            self.screen.blit(self.background, (0, 0))
            display.update()

    def __quit_game(self) -> bool:
        """Allow player to quit the game"""

        for eventType in event.get():
            if eventType.type == pygame.QUIT:
                return False

        return True
