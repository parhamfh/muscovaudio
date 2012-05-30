'''
Created on 28 maj 2012

@author: emser
'''

from ball import Ball

import random

class Balls(object):

    def __init__(self, amount, start_velocity, boundary_width, boundary_height):
        # Amount = number of balls on canvas 
        self.amount = amount 
        self.start_velocity = start_velocity 
        # Ball boundaries 
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        
        self.create_balls()
        
        
    def generate_random_coordinates(self):
        # Returns random coordinates for balls 
        return (random.randint(0,self.boundary_width), random.randint(0, self.boundary_height))
         
    def create_balls(self):
        self.ball_list = []
        for i in range(self.amount): 
            (x, y) = self.generate_random_coordinates()
            # print 'Coordinates for Ball %s: %s'%(i, (x,y))
            self.ball_list.append(Ball(x,y,1,self.start_velocity, i))
        # print "Created balls."
        
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
            if ball.boundary.left < 0:
                ball.velocity[0] = abs(ball.velocity[0])
            if ball.boundary.right > b_width:
                if ball.velocity[0] > 0: 
                    ball.velocity[0] = -1 * ball.velocity[0]
            if ball.boundary.top < 0: 
                ball.velocity[1] = abs(ball.velocity[1]) 
            if ball.boundary.bottom > b_height:
                if ball.velocity > 0: 
                    ball.velocity[1] = -1 * ball.velocity[1]
    
    def _detect_ball_collision(self):
        for i in range(len(self.ball_list)):
            for j in range (i+1,len(self.ball_list)):
                if self.ball_list[i].boundary.colliderect(self.ball_list[j].boundary):
                    # reverse direction
                    self._resolve_collision(self.ball_list[i], self.ball_list[j])
                    
    def _resolve_collision(self, ball, ball2):
        print "Collision between ball %s and %s!"%(ball.id, ball2.id)
        ball.reverse()
        ball2.reverse()
        
    def _detect_line_collision(self, lines):
        for ball in self.ball_list:
            for line in lines:
                pass
    
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
