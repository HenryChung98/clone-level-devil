import pygame
import sys
import time
from variables import *

from classes.player import Player
from classes.wall import Wall
from classes.door import Door
from classes.trap import Trap
import stages.stage2_4 as stage2_4


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
            if line == "8\n":
                is_opened = True
                break
        
        if is_opened == False:
            with open('opened-stages.txt', 'a') as file:
                file.write("8\n")

#------------------------------------------------- /check is opened

    

    # setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    ground = SCREEN_HEIGHT

    player = Player(SCREEN_WIDTH / 2 + 5, 0, player_size)
    door = Door(SCREEN_WIDTH / 8 * 7, SCREEN_HEIGHT / 8 * 7 - door_size - 10, door_size)   
    walls = [
        Wall(0, SCREEN_HEIGHT / 8 * 7, SCREEN_WIDTH, SCREEN_HEIGHT / 8, WHITE),
        Wall(SCREEN_WIDTH / 2, 100, 30, 450, WHITE)
        ]
    traps = [
        Trap(590, walls[0].pos[1] - trap_h, trap_w, trap_h, RED),
        Trap(890, walls[0].pos[1] - trap_h, trap_w, trap_h, RED)
    ]

    font = pygame.font.Font(None, 30)
    text = font.render("Press Spacebar to Move Next Stage", True, AQUA)
    stage_num = font.render("2 - 1", True, AQUA)
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
                    if ground != SCREEN_HEIGHT:
                        player.jump()
                
                if event.key == pygame.K_SPACE:
                    if is_clear == True:
                        stage2_4.run()



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

        # wall collision 
        # if player.pos[0] < 540 and player.pos[1] < 190:
        #     player.pos[0] = 545

        # set ground
        if player.pos[0] >= 630 and player.pos[0] <= 670 and player.pos[1] <= 100:
            ground = SCREEN_HEIGHT / 8 + 5

        else:
            ground = walls[0].pos[1] - 5


#------------------------------------------------- event
        
        # falling down
        if player.pos[1] > 120 and player.pos[1] < 460:
            player.dx = 0
        
        if player.pos[0] > SCREEN_WIDTH / 2 - 20 and player.pos[0] < SCREEN_WIDTH / 2 + 30 and player.pos[1] <= 550 and player.pos[1] >= 110:
            player.pos[1] = 545
            


#------------------------------------------------- /event


#------------------------------------------------- trap collision

        for trap in traps:
            if player.rect.colliderect(trap.rect):
                player.dead(run)


        traps[0].dx  = 0
        if player.pos[1] >= 510:
            if traps[0].pos[0] >= 740:
                traps[0].pos[0] = 740
            else:
                traps[0].dx += 4
                traps[0].move_x()

        if player.pos[1] >= 510 and player.pos[0] >= SCREEN_WIDTH / 2:
            if traps[0].pos[0] <= 450:
                traps[0].pos[0] = 450
            else:
                traps[0].dx -= 1
                traps[0].move_x()

        


#------------------------------------------------- /trap collision



#------------------------------------------------- wall collision
        # for wall in walls:
        #     if player.rect.colliderect(wall.rect):
        #         if player.is_jump == False:
        #             player.pos[1] = wall.h - player.size - 5


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
