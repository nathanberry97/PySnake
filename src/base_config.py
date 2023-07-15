import pygame


class base_config:
    def __init__(self, x_axis: int, y_axis: int):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.background_sprite = "../assets/snake/background.png"

    def configure_screen(self) -> pygame.Surface:
        """Method to create base screen"""

        pygame.display.set_caption("Retro Games")

        size = (self.x_axis, self.y_axis)
        screen = pygame.display.set_mode(size)

        return screen

    def import_background(self) -> pygame.Surface:
        """Method to import and resize background image"""

        import_background = pygame.image.load(self.background_sprite).convert()
        resize_background = pygame.transform.scale_by(import_background, 5)

        return resize_background
