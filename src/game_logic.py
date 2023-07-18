import pygame
from base_config import base_config
from score import score
from snake import snake
from apple import apple
from menu import menu


class game_logic:
    def __init__(self):
        self.base = base_config(800, 720)
        self.screen = self.base.configure_screen()

        self.snake = snake(self.screen)
        self.apple = apple(self.screen)
        self.score = score(self.screen)
        self.menu = menu(self.screen)

        self.menu_snake = self.base.import_background("menu/menu.png")
        self.background = self.base.import_background("snake/background.png")
        self.fps = 30

    def main_loop(self) -> None:
        """The main loop of the game"""

        game_loop = True

        while game_loop:
            self.screen.blit(self.menu_snake, (0, 0))

            self.menu.set_state()

            self.menu.draw_icon()

            game_loop = self.__start_screen()

            pygame.display.update()

    def __snake(self) -> None:
        """Game loop for snake"""

        play = True

        self.menu_snake = self.base.import_background("menu/menu_gameover.png")

        while play:
            self.base.set_frame_rate(self.fps)

            self.screen.blit(self.background, (0, 0))

            self.score.display_score(self.snake.get_score())

            self.apple.draw_apple()

            if self.apple.apple_collision(self.snake.get_position()):
                self.snake.update_score()

            self.snake.snake_body()

            self.snake.snake_tail()

            self.snake.snake_head()

            self.snake.move_snake()

            play = self.snake.valid_snake_position()

            if play:
                play = self.base.quit_game()

            pygame.display.update()

    def __start_screen(self) -> bool:
        """Method to determine start menu option"""

        game_loop = True

        key = pygame.key.get_pressed()

        if key[pygame.K_RETURN] and self.menu.get_state() == 0:
            self.__snake()

        elif key[pygame.K_RETURN] and self.menu.get_state() == 1:
            game_loop = False

        else:
            game_loop = self.base.quit_game()

        return game_loop
