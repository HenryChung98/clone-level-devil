import pygame
import sys
import time
from variables import *

from classes.player import Player
from classes.wall import Wall
from classes.trap import Trap
from classes.door import Door
from classes.button import Button

import stages.stage1_5 as stage1_5


def run():

    # setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    ground = SCREEN_HEIGHT

    player = Player(SCREEN_WIDTH / 3 - 30, SCREEN_HEIGHT / 2 - 45, player_size)
    door = Door(SCREEN_WIDTH / 3 * 2 + 30, SCREEN_HEIGHT / 2 - 50, door_size)   
    next_btn = Button('Next Stage', SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 50, 70, 50, stage1_5.run)
    wall = Wall(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, WHITE)
    traps = [
        Trap(SCREEN_WIDTH / 3 + 30, SCREEN_HEIGHT / 2 - 20, trap_w, trap_h, RED),
        Trap(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20, trap_w, trap_h, RED),
        Trap(SCREEN_WIDTH / 3 * 2 - 30, SCREEN_HEIGHT / 2 - 20, trap_w, trap_h, RED)
    ]


    while running:
        screen.fill(BLACK)
        
        # cheat
        # if ground == SCREEN_HEIGHT:
        #     player.is_jump = True
        

        # key event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:
                    player.jump()

                if event.key == pygame.K_LEFT:
                    player.dx -= 2
                if event.key == pygame.K_RIGHT:
                    player.dx += 2


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.dx = 0
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                next_btn.check_click(event.pos)
                print(event.pos)   


        # set ground to walls pos y
        if player.pos[0] >= wall.pos[0] and player.pos[0] <= wall.pos[0] + wall.w:
            ground = wall.h
        else:
            ground = SCREEN_HEIGHT




#-------------------------------------------------wall collision
        if player.rect.colliderect(wall.rect):
            
            if player.is_jump == False:
                player.pos[1] = wall.h - player.size - 5
        else:
            wall.color = WHITE


#-------------------------------------------------trap collision
        player_dead = False

        for trap in traps:
            if player.rect.colliderect(trap.rect):
                player_dead = True
                break


        if player.pos[1] >= SCREEN_HEIGHT - player_size:
            player_dead = True


        if player_dead:
            player.texture = pygame.image.load("imgs/player-dead-img.png")
            time.sleep(0.5)
            run()



        # door collision 
        if player.pos[0] >= door.pos[0] and player.pos[0] <= door.pos[0] + door_size:
            next_btn.draw(screen)
            
        
        # update
        player.draw(screen)
        door.draw(screen)
        wall.draw(screen)
        for trap in traps:
            trap.draw(screen)


        # update
        player.move_x()
        player.update(ground)
        pygame.display.flip()

        clock.tick(60) 

    pygame.quit()
    sys.exit()
