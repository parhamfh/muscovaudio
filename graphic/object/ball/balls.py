'''
Created on 28 maj 2012

@author: emser
'''

from graphic.object.ball import Ball

import random
import pygame
import sys


class Balls(object):

    def __init__(self, amount, startvelocity, width, height):
        # Amount = number of balls on canvas 
        self.amount = amount 
        self.startvelocity = startvelocity 
        # List of Ball objects 
        self.ball_list = [] 
        self.width = width
        self.height = height
        
    def generate_coordinates(self):
        # Returns random coordinates for balls 
        return (random.randint(0,self.width), random.randint(0, self.height))
         
    def create_balls(self):
        for i in range(self.amount): 
            (x, y) = self.generate_coordinates()
            # print 'Coordinates for Ball %s: %s'%(i, (x,y))
            self.ball_list.append(Ball(x,y,1,self.start_velocity))
        # print "Created balls."
        
    def check_ball_collisions(self):
        i = 0
        for ball in self.ball_list:
            # TODO: balls get stuck when coordinates are (canvas_width, canvas_heigth) in generate_coordinates  
            if ball.boundary.left < 0:
                ball.velocity[0] = abs(ball.velocity[0])
            if ball.boundary.right > self.canvas_width:
                if ball.velocity[0] > 0: 
                    ball.velocity[0] = -1 * ball.velocity[0]
            if ball.boundary.top < 0: 
                ball.velocity[1] = abs(ball.velocity[1]) 
            if ball.boundary.bottom > self.canvas_height:
                if ball.velocity > 0: 
                    ball.velocity[1] = -1 * ball.velocity[1]
            
    def move_balls(self):
        for ball in self.ball_list: 
            ball.boundary = ball.boundary.move(ball.velocity)
    
    def blit_balls(self, canvas):
        for ball in self.ball_list: 
            canvas.blit(ball.image, ball.boundary)
    


# TODO in muscovaudio.py: 
# Create Balls object called 'balls' 
# Inserted in the while loop that handles events in muscovaudio.py : 
# For every event in pygame.event.get()
# balls.check_ball_collisions 
# balls.move_balls()
# balls.blit_balls(canvas) 
