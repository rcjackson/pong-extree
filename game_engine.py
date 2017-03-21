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
import paddle
import random
import ball
import power_up
     
class game_engine:
    def __init__(self, num_players, screen):
        info = pygame.display.Info()
        self.num_players = num_players
        
        # Set ball, player 1 position
        self.balls = [ball.ball(screen)]
        self.player1 = paddle.paddle(screen,1)
        
        # Set player 2 positon
        self.__screen = screen
        self.player2 = paddle.paddle(screen,2)
        self.p1_score = 0
        self.p2_score = 0
        
        self.ting_sound = pygame.mixer.Sound('reflect.wav')

    def reset_positions(self):
        __info = pygame.display.Info()
        self.x = int(__info.current_w*0.5)
        self.y = int(__info.current_h*0.5)    
               
    def update_state(self):
        # If num_players is one, take in keyboard input and do AI's move
        self.player1.clear()
        self.player2.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            # Handle keyboard up and down
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                self.player1.move_paddle(2)
            
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                self.player1.move_paddle(-2)
            
            if(self.num_players == 2):
                # Handle keyboard up and down
                if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                    self.player2.move_paddle(2)
            
                if(event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                    self.player2.move_paddle(-2)   
                # Add joystick support later
        
        if(self.num_players == 1):
            # Right now have the AI just chase the ball it is closest to in y
            minimum = abs(self.player2.y + self.player2.size_y/2 - self.balls[0].y)
            i = 0
            for a_ball in self.balls:
                if((self.player2.y + self.player2.size_y/2 - a_ball.y) <= minimum):
                    closest_index = i
                i += 1
                
            if(self.balls[closest_index].y > self.player2.y + self.player2.size_y/2):
                paddle_delta = 2
            elif(self.balls[closest_index].y <= self.player2.y):
                paddle_delta = -2
            else:
                paddle_delta = 0
            self.player2.move_paddle(paddle_delta)
            
        self.player1.draw()
        self.player2.draw()
        # Move the ball
        for a_ball in self.balls:
            a_ball.clear()
            a_ball.move()
            a_ball.draw()
        
            # Check to see if ball is touching paddle
            if(a_ball.x <= self.player1.x+self.player1.size_x):
                # Reflect if paddle touches ball, lose if not
                if(a_ball.y+a_ball.size >= self.player1.y and
                   a_ball.y <= self.player1.y+self.player1.size_y):
                    a_ball.x_reflect()
                    self.ting_sound.play()
                else:
                    self.p2_score += 1   # 2 = player 1 loses
                    self.balls.remove(a_ball)
                    
           
            # Check to see if ball is touching paddle
            if(a_ball.x+a_ball.size >= self.player2.x):
                # Reflect if paddle touches ball, lose if not
                if(a_ball.y+a_ball.size >= self.player2.y and
                   a_ball.y <= self.player2.y+self.player2.size_y):
                    a_ball.x_reflect()
                    self.ting_sound.play()
                else:
                    self.p1_score += 1   # 2 = player 1 loses
                    self.balls.remove(a_ball)
                   
        # If no balls are left add a ball
        if(len(self.balls) == 0):
            self.balls.append(ball.ball(self.__screen))
            
        # Randomly determine if a new ball will pop up (1 in 1000 chance)
        if(random.random() < 1/1000):
            self.balls.append(ball.ball(self.__screen))
            
        return 1 # Keep going        
        
        # Randomly generate power-ups
        
        
        
         
        