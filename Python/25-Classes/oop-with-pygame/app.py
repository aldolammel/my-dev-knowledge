import pygame
from random import choice, randint
from vehicles import Car, Truck

# CONSTANTS:
SCN_WIDTH = 1200
SCN_HEIGHT = 800
SCR_PADDING = 30

# Pygame settings:
pygame.init()
screen = pygame.display.set_mode((SCN_WIDTH, SCN_HEIGHT))
is_running = True
veh_types = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 4]  # proportion
veh_colors = ["red", "green", "blue"]
veh_all = list()

# Set background color:
screen.fill("#f1f1f1")

for i in range(30):
    color = choice(veh_colors)
    x = randint(SCR_PADDING, SCN_WIDTH-SCR_PADDING)
    y = randint(SCR_PADDING, SCN_HEIGHT-SCR_PADDING)
    # Creating the vehicle/object:
    match choice(veh_types):
        case 1: veh_all.append(Car(x, y, color))
        case 2: veh_all.append(Car(x, y, skin="police_car"))
        case 3: veh_all.append(Truck(x, y))
        case 4: veh_all.append(Truck(x, y, skin="truck_tractor"))

# place image on the screen:
for veh in veh_all:
    screen.blit(veh.img, veh.loc)
    print(veh)

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
