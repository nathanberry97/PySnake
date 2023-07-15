import pygame
from random import randrange


class apple:
    def __init__(self, display: pygame.Surface):
        self.display = display

        self.apple_sprite = "../assets/snake/apple.png"

        self.x_apple, self.y_apple = randrange(70, 700), randrange(75, 615)

    def draw_apple(self) -> None:
        """Method to create the apple sprite"""

        import_sprite = pygame.image.load(self.apple_sprite).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, 5)

        self.display.blit(resize_sprite, (self.x_apple, self.y_apple))

    def apple_collision(self, snake_position: tuple[int, int]) -> bool:
        """Method to detect if the apple has been ate"""

        x_snake, y_snake = snake_position

        updated = False

        pixel_range = 25

        x_range = range(self.x_apple - pixel_range, self.x_apple + pixel_range)
        y_range = range(self.y_apple - pixel_range, self.y_apple + pixel_range)

        if x_snake in x_range and y_snake in y_range:
            self.x_apple = randrange(70, 700)
            self.y_apple = randrange(75, 615)
            updated = True

        return updated
