import pygame

class Door:
    def __init__(self, x, y, size):
        self.pos = [x, y]
        self.size = size
        self.texture = pygame.image.load("imgs/door.png")
        # self.texture = pygame.transform.scale(self.texture, (size, size))
        self.rect = self.texture.get_rect(center=(self.pos[0], self.pos[1]))

    def draw(self, screen):
        screen.blit(self.texture, self.pos)