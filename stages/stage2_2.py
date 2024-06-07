import pygame
import sys
import time
from variables import *

from classes.player import Player
from classes.wall import Wall
from classes.door import Door
from classes.trap import Trap
import stages.stage1_5 as stage1_5


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
            if line == "7\n":
                is_opened = True
                break
        
        if is_opened == False:
            with open('opened-stages.txt', 'a') as file:
                file.write("7\n")

#------------------------------------------------- /check is opened

    

    # setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    ground = SCREEN_HEIGHT

    player = Player(100, SCREEN_HEIGHT / 2 - 45, player_size)
    door = Door(SCREEN_WIDTH / 4 * 3 + 30, SCREEN_HEIGHT / 2 - 50, door_size)   
    walls = [
        Wall(0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2, WHITE)
        ]
    traps = [
        Trap(305, walls[0].pos[1] - trap_h, trap_w, trap_h, RED),
        Trap(565, walls[0].pos[1] - trap_h, trap_w, trap_h, RED),
        Trap(715, walls[0].pos[1] - trap_h, trap_w, trap_h, RED)
    ]

    font = pygame.font.Font(None, 30)
    text = font.render("Press Spacebar to Move Next Stage", True, AQUA)
    stage_num = font.render("2 - 2", True, AQUA)
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
                        stage1_5.run()



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

        else:
            ground = SCREEN_HEIGHT

#------------------------------------------------- event
        
        # falling down
        # if player.pos[0] > 150 and player.pos[0] < SCREEN_WIDTH / 4 * 3 and player.pos[1] > 370:
        #     player.dx = 0


#------------------------------------------------- /event


#------------------------------------------------- trap collision

        for trap in traps:
            if player.rect.colliderect(trap.rect):
                player.dead(run)

        if player.pos[0] >= 465:
            if traps[1].pos[0] <= 510:
                traps[1].pos[0] = 510
            else:
                traps[1].dx -= 4
                traps[1].move_x()

        if player.pos[0] >= 685:
            if traps[2].pos[1] <= 240:
                traps[2].pos[1] = 240
            else:
                traps[2].dy -= 4
                traps[2].move_y()


#------------------------------------------------- /trap collision


#-------------------------------------------------wall collision

        if player.pos[1] >= SCREEN_HEIGHT - player_size:
            player.dead(run)
            
#------------------------------------------------- /wall collision
            
        # draw
        screen.blit(back_btn, back_btn_rect.topleft)
        door.draw(screen)
        player.draw(screen)
        for wall in walls:
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
