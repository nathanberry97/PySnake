import pygame


class base_config:
    def __init__(self, x_axis: int, y_axis: int):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def configure_screen(self) -> pygame.Surface:
        """Method to create base screen"""

        pygame.display.set_caption("Retro Games")

        size = (self.x_axis, self.y_axis)
        screen = pygame.display.set_mode(size)

        return screen

    def import_background(self, background: str) -> pygame.Surface:
        """Method to import and resize background image"""

        sprit = f"../assets/{background}"
        import_background = pygame.image.load(sprit).convert()
        resize_background = pygame.transform.scale_by(import_background, 5)

        return resize_background

    def quit_game(self) -> bool:
        """Allow player to quit the game"""

        game_loop = True

        for eventType in pygame.event.get():
            if eventType.type == pygame.QUIT:
                return False

        return game_loop

    def set_frame_rate(self, fps: int) -> None:
        """Method to set the games frame rate"""

        clock = pygame.time.Clock()
        clock.tick(fps)
