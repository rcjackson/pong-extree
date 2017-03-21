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

class power_up:
    def __init__(self,type):
        info = pygame.display.Info()
        self.__type = type
        self.x = int(info.current_w*random.random())
        self.y = int(info.current_h*random.random())
        self.__deltax = int(2*random.random()-1)
        self.__deltay = int(2*random.random()-1)
    def update_position(self):
        # Move power up
        self.x += self.__xdelta
        self.y += self.__ydelta