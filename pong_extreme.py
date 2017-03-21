#
# This file is part of Pong Extree.  Pong Extreme is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Robert Jackson

import pygame
import paddle
import main_menu
import game_engine
import time
import random

# Start the screen
pygame.init()
size = width, height = 800, 600

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pong Extreme v.0.1')
pygame.mixer.init()
# Set random seed
random.seed()

# Initalize colors
black = 0, 0, 0
white = 255, 255, 255
get_option = 0
while get_option == 0:
    get_option = main_menu.do_menu(screen)
    if(get_option == 1):
        game = game_engine.game_engine(1,screen)
    elif(get_option == 2):
        game = game_engine.game_engine(2,screen)

# Enable key hold down
pygame.key.set_repeat(1,1)


if('game' in globals()):
    state = 1
    while(game.p1_score < 30 and game.p2_score < 30 and state != -1):
        while(state == 1):
            initial_time = time.time()
            # Clear screen
            pygame.draw.rect(screen, black, (0,0,800,600))
            # Update game
            state = game.update_state()
            
            # Display score
            info = pygame.display.Info()
            Font = pygame.font.SysFont('Calibri', 130, bold=1)
            Title_Surface = Font.render(str(game.p1_score),
                                        1,
                                        white)
            screen.blit(Title_Surface, (int(0.3*info.current_w),
                                        0))
            Title_Surface = Font.render(str(game.p2_score),
                                        1,
                                        white)
            screen.blit(Title_Surface, (int(0.6*info.current_w),
                                        0))
            pygame.display.flip()
        
            # Throttle speed to 120 fps
            cur_time = time.time()
            while(cur_time - initial_time < 1/120):
                cur_time = time.time()
            
        if(state == 2):
            game.p2_score += 1
        elif(state == 3):
            game.p1_score += 1        
        game.reset_positions()
        print(game.p2_score)
        print(game.p1_score)
pygame.display.quit()


    