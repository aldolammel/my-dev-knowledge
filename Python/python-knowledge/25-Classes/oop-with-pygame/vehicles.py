import pygame

# CONSTANTS:
IMG_PATH = "images"
IMG_EXT = "png"


class Car:
    def __init__(self, x=400, y=400, color="red", skin=""):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        self.pos = x, y
        self.color = color
        self.skin = skin
        self.file = f"{IMG_PATH}/sedan_{self.color}.{IMG_EXT}"
        self.img = None
        self.loc = None
        self.type_1 = "Light"
        self.type_2 = ""
        self.check_skin()
        self.draw()

    def __repr__(self):
        return f"1x vehicle: {self.type_1}{self.type_2} {self.color}"

    def check_skin(self):
        if self.skin != "":
            self.color = ""
            self.type_2 = " (Skin customized)"
            self.file = f"{IMG_PATH}/{self.skin}.{IMG_EXT}"

    def draw(self):
        self.img = pygame.image.load(self.file)
        self.img = pygame.transform.scale(self.img, (60, 60))
        self.loc = self.img.get_rect()
        self.loc.center = self.pos


class Truck(Car):
    def __init__(self, x, y, skin=""):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__()
        self.pos = x, y
        self.color = ""
        self.skin = skin
        self.file = f"{IMG_PATH}/box_truck.{IMG_EXT}"
        self.type_1 = "Medium"
        self.check_skin()
        self.draw()
