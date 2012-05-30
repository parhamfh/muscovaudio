'''
Created on May 30, 2012

@author: pfh
'''
import pygame 

class Ball(object):

    def __init__(self, x_init, y_init, r, velocity, i):
        self.x = x_init
        self.y = y_init
        self.radius = r 
        self.velocity = []
        self.velocity.extend(velocity)
        self.id = i
        # TODO: fix correct path 
        self.image = pygame.image.load('resources/img/ball.png')
        self.boundary = self.image.get_rect(center=(x_init,y_init))
        
    def reverse(self):
        self.image = pygame.image.load('resources/img/ball_touched.png')
        self.velocity[0] = -1 * self.velocity[0]
        self.velocity[1] = -1 * self.velocity[1]
