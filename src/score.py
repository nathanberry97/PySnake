import pygame


class score:
    def __init__(self, screen: pygame.Surface):
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
        self.screen = screen

    def display_score(self, score: int) -> None:
        """Method to display current score"""

        score_list = list(str(score))

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
