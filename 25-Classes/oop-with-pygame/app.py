import pygame
from random import choice, randint
import os
from vehicles import Car, Truck, Tractor

# place Pygame window at a specific location
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (100, 100)

# Pygame settings:
pygame.init()
screen = pygame.display.set_mode((800, 800))
is_running = True
veh_types = ["car", "truck", "tractor"]
veh_colors = ["red", "green", "blue"]
veh_all = list()

# Set background color:
screen.fill("white")

for i in range(5):
    veh_color = choice(veh_colors)
    veh_pos_x = randint(0, 800)
    veh_pos_y = randint(0, 800)
    # Creating the vehicle/object:
    match choice(veh_types):
        case "car": veh_all.append(Car(veh_color, veh_pos_x, veh_pos_y))
        case "truck": veh_all.append(Truck(veh_color, veh_pos_x, veh_pos_y))
        case "Tractor": veh_all.append(Tractor(veh_color, veh_pos_x, veh_pos_y))

# place image on the screen:
for veh in veh_all:
    screen.blit(veh.img, veh.loc)

# Start game loop:
while is_running:
    # if the 'exit' button is clicked:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop game loop:
            is_running = False

    # flip() the display to put your work on screen:
    pygame.display.flip()

pygame.quit()
