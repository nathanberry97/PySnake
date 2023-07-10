from pygame import Surface, display, image, transform


class base_config:
    def __init__(self, x_axis: int, y_axis: int):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def configure_screen(self) -> Surface:
        """Method to create base screen and import background img"""

        display.set_caption("Retro Games")

        size = (self.x_axis, self.y_axis)
        screen = display.set_mode(size)

        return screen

    def import_background(self) -> Surface:
        """Method to import and resize background image"""

        size = (self.x_axis, self.y_axis)

        import_background = image.load("../assets/background.png").convert()
        resize_background = transform.scale(import_background, size)

        return resize_background
