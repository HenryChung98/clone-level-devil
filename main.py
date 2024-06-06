import pygame
import sys
from variables import *

from classes.button import Button

import stages.stage1_1 as stage1_1
import stages.stage1_2 as stage1_2
import stages.stage1_3 as stage1_3
import stages.stage1_4 as stage1_4
import stages.stage1_5 as stage1_5
import stages.stage2_1 as stage2_1

def run():
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True


    #------------------------------------------------- check opened stages
    opened_stages = []

    try:
        with open('opened-stages.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                check_num = []
                for i in line:
                    try:
                        if int(i):
                            check_num.append(i)
                    except:
                        continue
                
                combined = ""
                for i in check_num:
                    combined += i

                opened_stages.append(int(combined))

    except:
        with open('opened-stages.txt', 'w') as file:
            file.write("1\n")

    #------------------------------------------------- check opened stages

    # button

    stage_btns = []
    button_details = {
        1: ('1 - 1', 100, 100, 50, 50, stage1_1.run),
        2: ('1 - 2', 200, 100, 50, 50, stage1_2.run),
        3: ('1 - 3', 300, 100, 50, 50, stage1_3.run),
        4: ('1 - 4', 400, 100, 50, 50, stage1_4.run),
        5: ('1 - 5', 500, 100, 50, 50, stage1_5.run),
        6: ('2 - 1', 600, 100, 50, 50, stage2_1.run)
    }

    for stage in opened_stages:
        if stage in button_details:
            label, x, y, width, height, action = button_details[stage]
            stage_btns.append(Button(label, x, y, width, height, action))


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
                for button in stage_btns:
                    button.check_click(event.pos)  

        # draw buttons
        for button in stage_btns:
            button.draw(screen)

        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()
    sys.exit()

run()