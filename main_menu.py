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

# Do the menu. This takes in the current screen surface as input
def do_menu(screen):
    # Disable holding key down
    pygame.key.set_repeat()
    # Initalize colors
    black = 0, 0, 0
    white = 255, 255, 255
    
    # Get display information
    info = pygame.display.Info()
    # Place text at top of screen
    spacing = 0.15
    Font = pygame.font.SysFont('Calibri', 30, bold=1)
    Title_Surface = Font.render('Pong Extreme v. 0.1',
                                1,
                                white)
    screen.blit(Title_Surface, (int(0.2*info.current_h),
                                int(0.2*info.current_w)))
    
    # Do one player, two player, options, exit
    Font = pygame.font.SysFont('Calibri', 20, bold=1)
    Title_Surface = Font.render('1 Player Game',
                                1,
                                white)
    screen.blit(Title_Surface, (int(0.2*info.current_w),
                                int((0.2+spacing)*info.current_h)))
    
    
    Title_Surface2 = Font.render('2 Player Game',
                                1,
                                white)
    screen.blit(Title_Surface2, (int(0.2*info.current_w),
                                int((0.2+2*spacing)*info.current_h)))
    
    
    Title_Surface3 = Font.render('Options',
                                1,
                                white)
    screen.blit(Title_Surface3, (int(0.2*info.current_w),
                                int((0.2+3*spacing)*info.current_h)))
    
    Title_Surface4 = Font.render('Exit',
                                1,
                                white)
    screen.blit(Title_Surface4, (int(0.2*info.current_w),
                                int((0.2+4*spacing)*info.current_h)))
    
    cur_option = 1
    enter_entered = 0
    while enter_entered == 0:
        # Draw empty rectangle to clear left menu choices
        pygame.draw.rect(screen,
                         black,
                         [int(0.15*info.current_w),
                         int((0.2+spacing)*info.current_h),
                         int(0.03*info.current_w),
                         int(0.8*info.current_h)])
        # Draw box
        pygame.draw.rect(screen,
                         white,
                         [int(0.15*info.current_w),
                         int((0.2+cur_option*spacing)*info.current_h),
                         int(0.03*info.current_w),
                         int(0.03*info.current_h)])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 4
            
            # Handle keyboard up and down
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                if(cur_option < 4):
                    cur_option += 1
                else:
                    cur_option = 1
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                if(cur_option > 1):
                    cur_option -= 1
                else:
                    cur_option = 4
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                enter_entered == 1
                return cur_option
                    
        
    return -4