import pygame
from snake import snake


class game_logic:
    def __init__(self, screen: pygame.Surface, background: pygame.Surface):
        self.screen = screen
        self.background = background
        self.snake = snake(self.screen)

    def main_loop(self, game_loop: bool) -> None:
        """The main loop of the game"""

        while game_loop:
            self.__set_frame_rate(60)

            self.screen.blit(self.background, (0, 0))

            self.snake.apple()

            self.snake.snake_head()

            self.snake.move_snake()

            game_loop = self.snake.valid_boundary()

            if game_loop:
                game_loop = self.__quit_game()

            pygame.display.update()

    def __quit_game(self) -> bool:
        """Allow player to quit the game"""

        game_loop = True

        for eventType in pygame.event.get():
            if eventType.type == pygame.QUIT:
                return False

        return game_loop

    def __set_frame_rate(self, fps: int) -> None:
        """Method to set the games frame rate"""

        clock = pygame.time.Clock()
        clock.tick(fps)
