import pygame

# CONSTANTS:
IMG_PATH = "images"
IMG_EXT = "png"


class Car:
    def __init__(self, color="red", x=400, y=400):
        self.file = f"{IMG_PATH}/sedan_{color}.{IMG_EXT}"
        self.img = None
        self.loc = None
        self.color = color
        self.pos = x, y
        self.draw()

    def draw(self):
        self.img = pygame.image.load(self.file)
        self.loc = self.img.get_rect()
        self.loc.center = self.pos


class Truck(Car):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.pos = x, y
        self.file = f"{IMG_PATH}/box_truck.{IMG_EXT}"


class Tractor(Truck):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.color = color
        self.pos = x, y
        self.file = f"{IMG_PATH}/truck_tractor.{IMG_EXT}"







