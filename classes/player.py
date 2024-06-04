import pygame
from variables import *



class Player:
    def __init__(self, x, y, size):
        self.size = size
        self.pos = [x, y]
        self.dx = 0
        self.dy = 0
        self.texture = pygame.image.load("imgs/player-img.png")
        # self.texture = pygame.transform.scale(self.texture, (size, size))
        self.rect = self.texture.get_rect(center=(self.pos[0], self.pos[1]))

        # physics
        self.is_jump = False
        self.v = VELOCITY
        self.m = MASS
        self.gravity = 30

    def draw(self, screen):
        screen.blit(self.texture, self.pos)

    def move_x(self):
        self.pos[0] += self.dx
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def jump(self):
        self.is_jump = True
        

    def update(self, ground):
        if self.is_jump == True:
            if self.v > 0:
                F = (0.5 * self.m * (self.v * self.v))
            else:
                F = -(0.5 * self.m * (self.v * self.v))

            self.pos[1] -= round(F)
            self.v -= 0.3
            if self.pos[1] > ground - self.size:
                self.pos[1] = ground - self.size
                self.is_jump = False
                self.v = VELOCITY

        else:
            self.pos[1] += self.gravity
            if self.pos[1] >= ground - self.size:
                self.pos[1] = ground - self.size
                self.dy = 0

            self.rect.y = self.pos[1]
            
            # # self.v += MASS * 0.1
            # self.pos[1] += self.v 
            
            # if self.pos[1] > ground - self.size:
            #     self.pos[1] = ground - self.size
            #     self.v = -self.v
        

