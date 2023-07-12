import pygame
from snake import snake
from apple import apple


class game_logic:
    def __init__(self, screen: pygame.Surface, background: pygame.Surface):
        self.screen = screen
        self.fps = 60
        self.background = background
        self.snake = snake(self.screen)
        self.apple = apple(self.screen)

    def main_loop(self, game_loop: bool) -> None:
        """The main loop of the game"""

        while game_loop:
            self.__set_frame_rate(self.fps)

            self.screen.blit(self.background, (0, 0))

            self.apple.draw_apple()

            self.apple.update_apple_position(self.snake.get_position())

            self.snake.snake_head()

            self.snake.move_snake()

            self.snake.valid_boundary()

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
