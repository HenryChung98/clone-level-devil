import pygame
import sys
import time
from variables import *

from classes.player import Player
from classes.wall import Wall
from classes.door import Door

import stages.stage1_3 as stage1_3


def run():
    import main
    back_btn = pygame.image.load("imgs/back.png")
    back_btn_rect = back_btn.get_rect(center=(32, 32))
    is_clear = False

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

#------------------------------------------------- /check is opened


    # setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    ground = SCREEN_HEIGHT

    player = Player(100, SCREEN_HEIGHT / 2 - 45, player_size)
    door = Door(SCREEN_WIDTH / 4 * 3 + 30, SCREEN_HEIGHT / 2 - 50, door_size)   
    walls = [
        Wall(0, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, WHITE),
        Wall(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100, SCREEN_HEIGHT / 2, WHITE),
        Wall(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2, WHITE)
        ]
    font = pygame.font.Font(None, 30)
    text = font.render("Press Spacebar to Move Next Stage", True, AQUA)
    stage_num = font.render("1 - 2", True, AQUA)
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
                    if ground != SCREEN_HEIGHT and player.pos[1] <= SCREEN_HEIGHT / 3 * 2:
                        player.jump()

                if event.key == pygame.K_SPACE:
                    if is_clear == True:
                        stage1_3.run()


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
                if back_btn_rect.collidepoint(event.pos):
                    running = False
                    main.run()
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
        if player.pos[0] > 660 and player.pos[0] < 690 and player.pos[1] > 370:
            player.dx = 0

        if player.pos[0] > 830 and player.pos[0] < 900 and player.pos[1] > 370:
            player.dx = 0


        # walls move
        if player.pos[0] >= SCREEN_WIDTH / 2 - 30:
            if walls[1].pos[0] >= SCREEN_WIDTH / 2 + 75:
                walls[1].pos[0] = SCREEN_WIDTH / 2 + 75
            else:
                walls[1].dx += 0.5
                walls[1].move_x()
        
        if player.pos[0] >= 760:
            if walls[2].pos[0] >= 895:
                walls[2].pos[0] = 895
            else:
                walls[2].dx += 0.8
                walls[2].move_x()


#------------------------------------------------- /event


#------------------------------------------------- wall collision
        for wall in walls:
            if player.rect.colliderect(wall.rect):
                if player.is_jump == False:
                    player.pos[1] = wall.h - player.size - 5


        if player.pos[1] >= SCREEN_HEIGHT - player_size:
            player.dead(run)
#------------------------------------------------- /wall collision
            

        # draw
        screen.blit(back_btn, back_btn_rect.topleft)
        door.draw(screen)
        player.draw(screen)
        for wall in walls:
            wall.draw(screen)


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
