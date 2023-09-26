# ANOTHER IMPORT EXAMPLE:

import pygame

# initializing the PyGame mixer:
pygame.mixer.init()

# initializing the own PyGame:
pygame.init()

# CHALLENGE 021
print('\n021 >> I\'m a nice pal, so let me drop a song, banger:\n')
pygame.mixer.music.load('../slaughterToPrevail.mp3')
pygame.mixer.music.play(loops=0)
pygame.event.wait()          # it will wait the music get finished first before the program ends.
