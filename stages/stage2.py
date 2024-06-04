import pygame
import sys
import time
from variables import *

from classes.player import Player
from classes.wall import Wall
from classes.door import Door
from classes.button import Button

import stages.stage2 as stage2


def run():
# pygame setup
    pygame.init()

    clock = pygame.time.Clock()
    running = True

    ground = SCREEN_HEIGHT
# --------------------------------------------------------------------
    player = Player(SCREEN_WIDTH / 3 - 30, SCREEN_HEIGHT / 2 - 45, player_size)
    door = Door(910, SCREEN_HEIGHT / 2 - 50, door_size)   
    next_btn = Button('Next Stage', SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 50, 70, 50, stage2.run)

    walls = [Wall(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, WHITE),
             Wall(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, SCREEN_HEIGHT / 2, WHITE),
             Wall(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2, 250, SCREEN_HEIGHT / 2, WHITE)
             ]
    
    

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:
                    if ground != SCREEN_HEIGHT and player.pos[1] <= SCREEN_HEIGHT / 3 * 2:
                        player.jump()

                if event.key == pygame.K_LEFT:
                    player.dx -= 3
                if event.key == pygame.K_RIGHT:
                    player.dx += 3


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.dx = 0
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                next_btn.check_click(event.pos)   
                print(event.pos)

        screen.fill(BLACK)

        # # cheat
        # if ground == SCREEN_HEIGHT:
        #     player.is_jump = True

        # for wall in walls:
        #     if player.pos[0] >= wall.pos[0] and player.pos[0] <= wall.pos[0] + wall.w:
        #         ground = wall.h
        if player.pos[0] >= walls[0].pos[0] and player.pos[0] <= walls[0].pos[0] + walls[0].w:
            ground = walls[0].h
        elif player.pos[0] >= walls[1].pos[0] and player.pos[0] <= walls[1].pos[0] + walls[1].w:
            ground = walls[1].h
        elif player.pos[0] >= walls[2].pos[0] and player.pos[0] <= walls[2].pos[0] + walls[2].w:
            ground = walls[2].h

        else:
            ground = SCREEN_HEIGHT

#------------------------------------------------- event

        if player.pos[0] >= SCREEN_WIDTH / 2 - 30:
            if walls[1].pos[0] >= SCREEN_WIDTH / 2 + 75:
                walls[1].pos[0] = SCREEN_WIDTH / 2 + 75
            else:
                walls[1].dx += 0.5
                walls[1].move_x()
            # if walls[2].pos[0] >= SCREEN_WIDTH / 2 + 75:
            #     walls[2].pos[0] = SCREEN_WIDTH / 2 + 75
            # else:
            #     walls[2].dx += 0.5
            #     walls[2].move_x()
        
        if player.pos[0] >= 700:
            if walls[2].pos[0] >= 900:
                walls[2].pos[0] = 900
            else:
                walls[2].dx += 0.8
                walls[2].move_x()

                


        # initialize
        player.draw(screen)
        player.move_x()
        player.update(ground)

        for wall in walls:
            wall.draw(screen)
        # wall1.draw(screen)
        # wall2.draw(screen)

        door.draw(screen)
        

#-------------------------------------------------wall collision
        for wall in walls:
            if player.rect.colliderect(wall.rect):
                if player.is_jump == False:
                    player.pos[1] = wall.h - player.size - 5


        player_dead = False


        if player.pos[1] >= SCREEN_HEIGHT - player_size * 3:
            player_dead = True


        if player_dead:
            player.texture = pygame.image.load("imgs/player-dead-img.png")
            time.sleep(0.5)
            run()

#-------------------------------------------------door collision 
        if player.pos[0] >= door.pos[0] and player.pos[0] <= door.pos[0] + door_size:
            next_btn.draw(screen)
            

        pygame.display.flip()

        clock.tick(60) 

    pygame.quit()
    sys.exit()
