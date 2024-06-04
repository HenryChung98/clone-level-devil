import pygame

# screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# physics
VELOCITY = 4
MASS = 3

# objects
player_size = 40
door_size = 40
trap_w = 20
trap_h = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))