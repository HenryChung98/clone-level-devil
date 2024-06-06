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
    import main
    back_btn = pygame.image.load("imgs/back.png")
    back_btn_rect = back_btn.get_rect(center=(32, 32))
    is_clear = False

    # setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    ground = SCREEN_HEIGHT

    player = Player(SCREEN_WIDTH / 3 - 30, SCREEN_HEIGHT / 2 - 45, player_size)
    door = Door(SCREEN_WIDTH / 3 * 2 + 30, SCREEN_HEIGHT / 2 - 50, door_size)   
    wall = Wall(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, WHITE)
    traps = [
        Trap(SCREEN_WIDTH / 3 + 30, SCREEN_HEIGHT / 2 - 20, trap_w, trap_h, RED),
        Trap(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20, trap_w, trap_h, RED),
        Trap(SCREEN_WIDTH / 3 * 2 - 30, SCREEN_HEIGHT / 2 - 20, trap_w, trap_h, RED)
    ]
    font = pygame.font.Font(None, 30)
    text = font.render("Press Spacebar to Move Next Stage", True, AQUA)
    stage_num = font.render("1_4", True, AQUA)
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7))
    stage_num_rect = stage_num.get_rect(center=(SCREEN_WIDTH / 2, 30))


    while running:
        screen.fill(BLACK)
        screen.blit(stage_num, stage_num_rect.center)
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
                    player.jump()

                if event.key == pygame.K_LEFT:
                    player.dx -= 2
                if event.key == pygame.K_RIGHT:
                    player.dx += 2

                if event.key == pygame.K_SPACE:
                    if is_clear == True:
                        stage1_5.run()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.dx = 0
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    running = False
                    main.run()
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
            
        
        # update
        screen.blit(back_btn, back_btn_rect.topleft)
        door.draw(screen)
        player.draw(screen)
        wall.draw(screen)
        for trap in traps:
            trap.draw(screen)

        
        # door collision 
        if player.pos[0] >= door.pos[0] and player.pos[0] <= door.pos[0] + door_size:
            is_clear = True
            screen.blit(text, text_rect.topleft)
        else:
            is_clear = False


        # update
        player.move_x()
        player.update(ground)
        pygame.display.flip()

        clock.tick(60) 

    pygame.quit()
    sys.exit()
