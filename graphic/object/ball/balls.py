'''
Created on 28 maj 2012

@author: emser
'''
import random

import pygame

from graphic.object.ball import Ball
from event.manager import EventManager
from event.hook.ball import BallCollision
from event.hook.ball import LineCollision
import graphic.collision.pixelperfect as pp


# TODO make inherit from list
class Balls(object):

    def __init__(self, amount, start_velocity, boundary_width, boundary_height, colorkey):
        # Amount = number of balls on canvas 
        self.amount = amount 
        self.start_velocity = start_velocity 
        # Ball boundaries 
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        self.colorkey = colorkey
        self.create_balls()
        self.em = EventManager()
        
    def generate_random_coordinates(self):
        # Returns random coordinates for balls 
        return (random.randint(0,self.boundary_width), random.randint(0, self.boundary_height))
         
    def create_balls(self):
        self.ball_list = []
        for i in range(self.amount):
            (x, y) = self.generate_random_coordinates()
#            # print 'Coordinates for Ball %s: %s'%(i, (x,y))
            self.ball_list.append(Ball(x,y,1,self.start_velocity, i, self.colorkey))
#        self.ball_list.append(Ball(400,20,1,[-1,1],0,self.colorkey))
#        self.ball_list.append(Ball(20,400,1,[1,-1],1,self.colorkey))
        print "Created balls."
        
    def detect_collisions(self, lines, width=None, height=None):
        self._detect_wall_collision(width, height)
        self._detect_ball_collision()
        self._detect_line_collision(lines)

    def _detect_wall_collision(self, b_width=None, b_height=None):
        if b_width == None:
            b_width = self.boundary_width
        if b_height == None:
            b_height = self.boundary_height
        
        for ball in self.ball_list:
            # TODO: balls get stuck when coordinates are (canvas_width, canvas_heigth) in generate_random_coordinates 
            # TODO: send WallCollision
            
            
            if ball.boundary.left < 0:
                ball.image = pygame.image.load('resources/img/ball_red.png')
                ball.velocity[0] = abs(ball.velocity[0])
                #print 'Left wall collision!'
                # self.em[WallCollision].fire('left')
            if ball.boundary.right > b_width:
                ball.image = pygame.image.load('resources/img/ball_red.png')
                if ball.velocity[0] > 0: 
                    ball.velocity[0] = -1 * ball.velocity[0]
                    #print 'Right wall collision!'
                    # self.em[WallCollision].fire('right')
            if ball.boundary.top < 0: 
                ball.image = pygame.image.load('resources/img/ball_red.png')
                ball.velocity[1] = abs(ball.velocity[1])
                #print 'Top wall collision!'
                # self.em[WallCollision].fire('top')
            if ball.boundary.bottom > b_height:
                ball.image = pygame.image.load('resources/img/ball_red.png')
                if ball.velocity > 0: 
                    ball.velocity[1] = -1 * ball.velocity[1]
                    #print 'Bottom wall collision!'
                    # self.em[WallCollision].fire('bottom')
    
    def _detect_ball_collision(self):
        for i in range(len(self.ball_list)):
            for j in range (i+1,len(self.ball_list)):
                if pp.check_collision(self.ball_list[i], self.ball_list[j]):
#                if self.ball_list[i].boundary.colliderect(self.ball_list[j].boundary):
                    # reverse direction
                    if not self.ball_list[i].colliding_with(self.ball_list[j]):
                        self._resolve_collision(self.ball_list[i], self.ball_list[j])
                        self.ball_list[i].set_colliding_with(self.ball_list[j])
                        self.ball_list[j].set_colliding_with(self.ball_list[i])
                else:
                    if self.ball_list[i].colliding_with(self.ball_list[j]):
                        self.ball_list[i].set_not_colliding_with(self.ball_list[j])
                        self.ball_list[j].set_not_colliding_with(self.ball_list[i])
                        
    def _resolve_collision(self, ball, ball2):
        #print "Collision between, ball %s and %s!"%(ball.id, ball2.id)
        self.em[BallCollision].fire(ball, ball2)
        ball.reverse()
        ball2.reverse()
        
    def _detect_line_collision(self, lines):
        for ball in self.ball_list:
            for line in lines:
                if pp.check_collision(ball, line):
                    if not ball.colliding:
                        self.em[LineCollision].fire()
                        ball.reverse()
                        ball.set_colliding_with(line)
                        ball.set_colliding(True)
                    if ball.colliding:
                        if not ball.colliding_with(line):
                            ball.set_colliding_with(line)
                else:
                    if ball.colliding_with(line):
                        ball.set_not_colliding_with(line)
                    
    
    def move_balls(self):
        for ball in self.ball_list: 
            ball.set_boundary(ball.boundary.move(ball.velocity))
    
    def blit_balls(self, canvas):
        for ball in self.ball_list: 
            canvas.blit(ball.image, ball.boundary)
    

