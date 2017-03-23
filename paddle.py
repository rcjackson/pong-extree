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

class paddle:
    def __init__(self, screen_surface, player):
        # Get display information
        info = pygame.display.Info()
        if(player == 1):
            self.x = 0
        else:
            self.x = info.current_w - 30
        self.y = 0.4*info.current_h
        self.__screen = screen_surface
        self.size_x = 30
        self.size_y = 90
        
    # Move paddle
    def move_paddle(self,delta):
        info = pygame.display.Info()
        if(self.y+delta > 0 and self.y+delta+self.size_y < info.current_h):
            self.y += delta
        
    # Update paddle image
    def draw(self):
        # Draw box
        white = 255, 255, 255
        pygame.draw.rect(self.__screen,
                         white,
                         [int(self.x),
                         int(self.y),
                         int(self.size_x),
                         int(self.size_y)])
    
    def clear(self):
        # Clear box
        black = 0, 0, 0
        pygame.draw.rect(self.__screen,
                         black,
                         [int(self.x),
                         int(self.y),
                         int(self.size_x),
                         int(self.size_y)])
        
    