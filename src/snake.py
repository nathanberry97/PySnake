import pygame


class snake:
    def __init__(self, display):
        self.display = display

        self.head_sprite = "../assets/snake/snake_head.png"
        self.body_sprite = "../assets/snake/snake_body.png"
        self.tail_sprite = "../assets/snake/snake_tail.png"

        self.snake_speed = 5
        self.scale = 5

        self.x_snake_speed = 0
        self.y_snake_speed = 0

        self.x_snake = 375
        self.y_snake = 375

        self.snake_body_dict = [[self.x_snake, self.y_snake, 0]]

        self.angle = 0
        self.score = 0

    def snake_head(self) -> None:
        """Method to create and resize the snakes head"""

        sprite = self.head_sprite
        x, y = self.x_snake, self.y_snake
        angle = self.angle

        self.__draw_snake(sprite, x, y, angle)

    def snake_tail(self) -> None:
        """Method to create and resize the snakes head"""

        x_axis = self.snake_body_dict[0][0]
        y_axis = self.snake_body_dict[0][1]
        angle = self.snake_body_dict[0][2]

        if angle == 0:
            y_axis += 20

        elif angle == 90:
            x_axis += 20

        elif angle == 180:
            y_axis -= 20

        elif angle == 270:
            x_axis -= 20

        self.__draw_snake(self.tail_sprite, x_axis, y_axis, angle)

    def snake_body(self) -> None:
        """Method to draw the snakes body"""

        self.snake_body_dict.append([self.x_snake, self.y_snake, self.angle])

        if len(self.snake_body_dict) > self.score * 3:
            del self.snake_body_dict[0]

        for index in self.snake_body_dict:
            self.__draw_snake(self.body_sprite, index[0], index[1], index[2])

    def valid_snake_position(self) -> None:
        """Method to ensure that the snake has not hit the boundary"""

        if self.x_snake < 65 or self.x_snake > 710:
            self.__reset_snake()

        elif self.y_snake < 65 or self.y_snake > 630:
            self.__reset_snake()

        for index in self.snake_body_dict[:-1]:
            if index[0] == self.x_snake and index[1] == self.y_snake:
                self.__reset_snake()

    def move_snake(self) -> None:
        """Method to allow movement of the snake"""

        key = pygame.key.get_pressed()

        if key[pygame.K_a] and self.angle != 270:
            self.x_snake_speed = -self.snake_speed
            self.y_snake_speed = 0
            self.angle = 90

        elif key[pygame.K_d] and self.angle != 90:
            self.x_snake_speed = self.snake_speed
            self.y_snake_speed = 0
            self.angle = 270

        elif key[pygame.K_w] and self.angle != 180:
            self.y_snake_speed = -self.snake_speed
            self.x_snake_speed = 0
            self.angle = 0

        elif key[pygame.K_s] and self.angle != 0:
            self.y_snake_speed = self.snake_speed
            self.x_snake_speed = 0
            self.angle = 180

        self.y_snake += self.y_snake_speed
        self.x_snake += self.x_snake_speed

    def get_position(self) -> tuple[int, int]:
        """Method to return snakes current position"""

        return self.x_snake, self.y_snake

    def get_score(self) -> int:
        """Method to return current score"""

        return self.score

    def update_score(self) -> None:
        """Method to update the score"""

        self.score += 1
        if self.score % 5 == 0 and self.snake_speed < 9:
            self.snake_speed += 1

    def __draw_snake(self, sprite: str, x: int, y: int, angle: int) -> None:
        """Method to draw snake onto the display"""

        import_sprite = pygame.image.load(sprite).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        head_position = pygame.transform.rotate(resize_sprite, angle)
        self.display.blit(head_position, (x, y))

    def __reset_snake(self) -> None:
        """Method to reset snake vars on restart of the game"""

        self.x_snake_speed = 0
        self.y_snake_speed = 0
        self.snake_speed = 5

        self.x_snake = 375
        self.y_snake = 375
        self.angle = 0
        self.score = 0

        self.snake_body_dict.clear()
        self.snake_body_dict = [[self.x_snake, self.y_snake, 0]]
