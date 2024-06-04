import pygame
import sys
from variables import *

from classes.button import Button

import stages.stage1_1 as stage1_1
import stages.stage1_2 as stage1_2
import stages.stage1_3 as stage1_3


# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

# button
stage1_btn = Button('Stage 1', 100, 100, 50, 50, stage1_1.run)
stage2_btn = Button('Stage 2', 200, 100, 50, 50, stage1_2.run)
stage3_btn = Button('Stage 3', 300, 100, 50, 50, stage1_3.run)

# loop
while running:
    
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            stage1_btn.check_click(event.pos)   
            stage2_btn.check_click(event.pos)   
            stage3_btn.check_click(event.pos)   

    # draw buttons
    stage1_btn.draw(screen)
    stage2_btn.draw(screen) 
    stage3_btn.draw(screen)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
sys.exit()