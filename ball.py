#
# This file is part of Pong Extreme.  Pong Extreme is free software: you can
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
import random

# This defines the ball class
class ball:
    def __init__(self, screen):
        __info = pygame.display.Info()
        self.x = int(__info.current_w*0.5)
        self.y = int(__info.current_h*0.5)    
        self.__xdelta = -3*random.random()
        self.__ydelta = 3*random.random()
        self.size = 30
        self.__screen = screen
        if(abs(self.__xdelta) <= 1):
            self.__xdelta = 2
        if(abs(self.__ydelta) <= 1):
            self.__ydelta = 2
            
    def move(self):
        info = pygame.display.Info()
        # Reflect ball
        if(self.y <= 0 and self.__ydelta < 0):
            self.__ydelta = -self.__ydelta
        if(self.y >= info.current_h-self.size and self.__ydelta > 0):
            self.__ydelta = -self.__ydelta 
        self.x += self.__xdelta
        self.y += self.__ydelta
        
    def x_reflect(self):
        self.__xdelta = -self.__xdelta
        
    def y_reflect(self):
        self.__ydelta = -self.__ydelta
        
    def speed_up(self):
        if(self.__xdelta < 0):
            self.__xdelta -= 1
        else:
            self.__xdelta += 1
            
        if(self.__ydelta < 0):
            self.__ydelta -= 1
        else:
            self.__ydelta += 1
            
    def draw(self):
        # Draw box
        white = 255, 255, 255
        pygame.draw.rect(self.__screen,
                         white,
                         [int(self.x),
                         int(self.y),
                         int(self.size),
                         int(self.size)])
    
    def clear(self):
        # Clear box
        black = 0, 0, 0
        pygame.draw.rect(self.__screen,
                         black,
                         [int(self.x),
                         int(self.y),
                         int(self.size),
                         int(self.size)])