'''
Created on May 30, 2012

@author: parhamfh
'''

import pygame 
import graphic.collision as collision

from graphic.colour import Colour 

class Ball(collision.Collidable):

    def __init__(self, x_init, y_init, r, velocity, i, colorkey = None, 
                 alpha = None):
        super(Ball, self).__init__()
        self.x = x_init
        self.y = y_init
        self.radius = r 
        self.velocity = []
        self.velocity.extend(velocity)
        self.id = i
        # TODO: fix correct path 
        self.image = pygame.image.load('resources/img/ball.png')
        # Collidable attributes
        self._rect = self.image.get_rect(center=(x_init,y_init))
        self.colorkey = colorkey
        self.alpha = alpha
        self._hitmask = pygame.surfarray.array2d(self.image)
#        print 'Ball: printing the\nRect: %s\nSurface: %s\n'%(self.rect, self.image)

        
    def reverse(self):
        self.image = pygame.image.load('resources/img/ball_touched.png')
        self.velocity[0] = -1 * self.velocity[0]
        self.velocity[1] = -1 * self.velocity[1]
    
    @property 
    def rect(self):
        return self._rect
    
    @property
    def hitmask(self):
        return self._hitmask
    
    @property
    def boundary(self):
        return self._rect
    
    def set_boundary(self, moved_boundary):
        self._rect = moved_boundary
#        print 'Ball: printing the\nRect: %s\nSurface: %s\n'%(self.rect, self.image)
        
# Imports into package
from balls import Balls