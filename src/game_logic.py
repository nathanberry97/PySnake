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
        self.SCORE = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
        }

    def main_loop(self, game_loop: bool) -> None:
        """The main loop of the game"""

        while game_loop:
            self.__set_frame_rate(self.fps)

            self.screen.blit(self.background, (0, 0))

            self.__display_score()

            self.apple.draw_apple()

            if self.apple.apple_collision(self.snake.get_position()):
                self.snake.update_score()

            self.snake.snake_body()

            self.snake.snake_tail()

            self.snake.snake_head()

            self.snake.move_snake()

            self.snake.valid_snake_position()

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

    def __display_score(self) -> None:
        """Method to display current score"""

        score_list = list(str(self.snake.get_score()))

        digit_one = self.__get_digit(score_list, 0, 1)
        digit_two = self.__get_digit(score_list, 1, 2)
        digit_three = self.__get_digit(score_list, 2, 3)

        self.__draw_sore(digit_one, 265, 18)
        self.__draw_sore(digit_two, 240, 18)
        self.__draw_sore(digit_three, 215, 18)

    def __draw_sore(self, sprite: str, x: int, y: int) -> None:
        """Method to draw score onto the display"""

        import_sprite = pygame.image.load(
            f"../assets/numbers/{sprite}.png"
        ).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, 5)

        self.screen.blit(resize_sprite, (x, y))

    def __get_digit(self, score: list[str], index: int, num: int) -> str:
        """Method get the digit for the score"""

        digit = "zero"

        if len(score) > index:
            digit = self.SCORE[score[-num]]

        return digit
