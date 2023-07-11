import pygame


class snake:
    def __init__(self, display):
        self.display = display

        self.snake_sprite = "../assets/snake_head.png"
        self.apple_sprite = "../assets/apple.png"

        # TODO I would like this var increase as the player score increases
        self.snake_speed = 5

        self.x_snake_speed = 0
        self.y_snake_speed = 0

        self.x_snake = 375
        self.y_snake = 375

        self.x_apple = 500
        self.y_apple = 375

        self.angle = 0

    def snake_head(self) -> None:
        """Method to create and resize the snakes head"""

        import_sprite = pygame.image.load(self.snake_sprite).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, 5)

        head_position = pygame.transform.rotate(resize_sprite, self.angle)
        self.display.blit(head_position, (self.x_snake, self.y_snake))

    def valid_boundary(self) -> bool:
        """Method to ensure that the snake has not hit the boundary"""

        valid_position = True

        if self.x_snake < 60 or self.x_snake > 710:
            valid_position = False

        elif self.y_snake < 65 or self.y_snake > 625:
            valid_position = False

        return valid_position

    def apple(self):
        """Method to create the apple sprite"""

        import_sprite = pygame.image.load(self.apple_sprite).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, 5)

        self.display.blit(resize_sprite, (self.x_apple, self.y_apple))

    def move_snake(self):
        """Method to allow movement of the snake"""

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.x_snake_speed = -self.snake_speed
            self.y_snake_speed = 0
            self.angle = 90

        elif key[pygame.K_d]:
            self.x_snake_speed = self.snake_speed
            self.y_snake_speed = 0
            self.angle = 270

        elif key[pygame.K_w]:
            self.y_snake_speed = -self.snake_speed
            self.x_snake_speed = 0
            self.angle = 0

        elif key[pygame.K_s]:
            self.y_snake_speed = self.snake_speed
            self.x_snake_speed = 0
            self.angle = 180

        self.y_snake += self.y_snake_speed
        self.x_snake += self.x_snake_speed
