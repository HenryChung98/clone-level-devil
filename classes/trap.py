import pygame

class Trap:
    def __init__(self, x, y, width, height, color):
        self.pos = [x, y]
        self.w = width
        self.h = height
        self.dx = 0
        self.dy = 0
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move_x(self):
        self.pos[0] += self.dx
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def move_y(self):
        self.pos[1] += self.dy
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]



