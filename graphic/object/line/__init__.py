'''
Created on May 29, 2012

@author: parhamfh
'''
import pygame

from graphic.collision import Collidable
from graphic.colour import Colour

class Line(Collidable):
    def __init__(self, start, end, colour, rect):
        super(Line, self).__init__()
        self.start = start
        self.end = end
        self.colour = colour
        self.color_key = Colour.WHITE
        self._rect = rect
#        self._hitmask = pygame.surfarray.array2d(self.image)
    
    @property
    def image(self):
        return self.line_surface
    
    @property 
    def rect(self):
        return self._rect
        
    def move(self, (x,y)):
        self.start = (self.start[0] + x, self.start[1]+ y)
        self.end = (self.end[0] + x, self.end[1] + y)
        
    @property
    def hitmask(self):
        if self._hitmask is None:
            self._hitmask = pygame.surfarray.array_colorkey(self.image)
        return self._hitmask 
    
# Imports into package
#from lines import Lines
    