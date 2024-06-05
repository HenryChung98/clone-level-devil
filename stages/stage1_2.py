import pygame
import sys
import time
from variables import *

from classes.player import Player
from classes.wall import Wall
from classes.door import Door
from classes.button import Button

import stages.stage1_2 as stage1_2


def run():

#------------------------------------------------- check is opened

    with open('opened-stages.txt', 'r') as file:
        lines = file.readlines()
        is_opened = False
        for line in lines:
            if line == "2\n":
                is_opened = True
                break
        
        if is_opened == False:
            with open('opened-stages.txt', 'a') as file:
                file.write("2\n")

#------------------------------------------------- check is opened


    # setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    ground = SCREEN_HEIGHT

    player = Player(SCREEN_WIDTH / 3 - 30, SCREEN_HEIGHT / 2 - 45, player_size)
    door = Door(910, SCREEN_HEIGHT / 2 - 50, door_size)   
    next_btn = Button('Next Stage', SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 50, 70, 50, stage1_2.run)
    walls = [
        Wall(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, WHITE),
        Wall(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, SCREEN_HEIGHT / 2, WHITE),
        Wall(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2, 250, SCREEN_HEIGHT / 2, WHITE)
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

                if event.key == pygame.K_UP:
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

        
        # set ground to walls pos y
        if player.pos[0] >= walls[0].pos[0] and player.pos[0] <= walls[0].pos[0] + walls[0].w:
            ground = walls[0].h
        elif player.pos[0] >= walls[1].pos[0] and player.pos[0] <= walls[1].pos[0] + walls[1].w:
            ground = walls[1].h
        elif player.pos[0] >= walls[2].pos[0] and player.pos[0] <= walls[2].pos[0] + walls[2].w:
            ground = walls[2].h

        else:
            ground = SCREEN_HEIGHT

#------------------------------------------------- event

        # falling down


        # walls move
        if player.pos[0] >= SCREEN_WIDTH / 2 - 30:
            if walls[1].pos[0] >= SCREEN_WIDTH / 2 + 75:
                walls[1].pos[0] = SCREEN_WIDTH / 2 + 75
            else:
                walls[1].dx += 0.5
                walls[1].move_x()
        
        if player.pos[0] >= 760:
            if walls[2].pos[0] >= 900:
                walls[2].pos[0] = 900
            else:
                walls[2].dx += 0.8
                walls[2].move_x()


#------------------------------------------------- event


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
#-------------------------------------------------wall collision


        # door collision 
        if player.pos[0] >= door.pos[0] and player.pos[0] <= door.pos[0] + door_size:
            next_btn.draw(screen)
            

        # draw
        player.draw(screen)
        door.draw(screen)
        for wall in walls:
            wall.draw(screen)


        # update
        player.move_x()
        player.update(ground)
        pygame.display.flip()

        clock.tick(60) 

    pygame.quit()
    sys.exit()
