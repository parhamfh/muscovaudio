'''
Created on 28 maj 2012

@author: emser
'''

from graphic.object.ball import Ball


import random


class Balls(object):

    # canvas_width n heiht should be an input parameter instead
    # they should not be inserted as inputs into the functions
    def __init__(self, amount, start_velocity, canvas_width, canvas_height):
        # Amount = number of balls on canvas 
        self.amount = amount 
        self.start_velocity = start_velocity 
        # List of Ball objects 
        self.ball_list = [] 
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
    def generate_coordinates(self):
        #return (random.randint(0,self.canvas_width), random.randint(0, self.canvas_height))
        return self.canvas_width,self.canvas_height
         
    def create_balls(self):
        for i in range(self.amount): 
            (x, y) = self.generate_coordinates()
            print 'Coordinates for Ball %s: %s'%(i, (x,y))
            # random velocity vector is needed!
            self.ball_list.append(Ball(x,y,1,self.start_velocity))
        print "Created balls."
        
    def check_ball_collisions(self):
        i = 0
        for ball in self.ball_list:
            #print ball.ball_image
            if ball.ball_boundary.left < 0:
                ball.velocity[0] = abs(ball.velocity[0])
            if ball.ball_boundary.right > self.canvas_width:
                if ball.velocity[0] > 0: 
                    ball.velocity[0] = -1 * ball.velocity[0]
            if ball.ball_boundary.top < 0: 
                ball.velocity[1] = abs(ball.velocity[1]) 
            if ball.ball_boundary.bottom > self.canvas_height:
                if ball.velocity > 0: 
                    ball.velocity[1] = -1 * ball.velocity[1]
            print "%s printing vel:"%i
            print ball.velocity
            print "Did that shit"
            i += 1
    def move_balls(self):
        for ball in self.ball_list: 
            ball.ball_boundary = ball.ball_boundary.move(ball.velocity)
    
    def blitting_balls(self):
        for ball in self.ball_list: 
            frame.blit(ball.ball_image, ball.ball_boundary)


import pygame
import sys 

pygame.init()
frame = pygame.display.set_mode((630, 470))

bolltest=Balls(5, [3,4], 628,468)
bolltest.create_balls()
# print bolltest.ball_list


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit(0)
    frame.fill((30,30,30))

    bolltest.check_ball_collisions()
    bolltest.move_balls()
    bolltest.blitting_balls()
    
    pygame.display.flip()