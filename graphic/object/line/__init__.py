'''
Created on May 29, 2012

@author: parhamfh
'''
import math

import pygame
from pygame import Surface, Rect

import graphic.collision as gc
from graphic.collision import Collidable
from graphic.colour import Colour

class Line(Collidable):
    def __init__(self, x0, y0, x1, y1, line_color, colorkey):
        super(Line, self).__init__()
        self.line_width = 1
        # Super canvas position top left corner
        self.super_canvas_start = (x0, y0)
        self.super_canvas_end = (x1, y1)
        
        # Transformation vector and position of left top corner
        self.t = (min(x0,x1), min(y0,y1))

        self.start = (x0-self.t[0], y0-self.t[1])
        self.end = (x1-self.t[0], y1-self.t[1])
        
        # Color stuff
        self.line_color = line_color
        self.colorkey = colorkey
        
        # Offset of coordinates based on line width
        self.offset = self.line_width * 4
        # Collision stuff
        self.line_surface = Surface( (self.offset+abs(x1-x0), 
                                      self.offset+abs(y1-y0)) )
        self.line_surface.set_colorkey(self.colorkey)

    @property
    def image(self):
        return self.line_surface
    
    @property 
    def rect(self):
        return self._rect
        
    def move(self, (x,y)):
        self.super_canvas_start = (self.super_canvas_start[0] + x, self.super_canvas_start[1]+ y)
        self.super_canvas_end = (self.super_canvas_end[0] + x, self.super_canvas_end[1] + y)
        
    @property
    def hitmask(self):
        if self._hitmask is None:
            self._hitmask = pygame.surfarray.array_colorkey(self.image)
        return self._hitmask 

    def _adjust_rect(self, rect, x0, y0, x1, y1):
        """
            This version is in place.
        """
        dx = abs(x0-x1)
        dy = abs(y0-y1)
        rect.move_ip((x0,y0))
        # Move to correct position
        # If x and y are growing
        if x0 < x1 and y0 < y1:
#            print "x ->, y ->"
            return
        # If x is growing and y is NOT
        elif x0 < x1 and y0 > y1:
#            print "x ->, y <-"
            return rect.move_ip(0, -dy)
        # If x is unchanged and y growing
        elif x0 == x1 and y0 < y1:
#            print "y ->"
            return rect.move_ip(-int((self.offset+dx)/2), 0)
        # If x is growing and y is unchanged
        elif x0 < x1 and y0 == y1:
#            print "x ->"
            return rect.move_ip(0, -int((self.offset+dy)/2))
        # If x is NOT growing and y is
        elif x0 > x1 and y0 < y1:
#            print "x <-, y ->"
            rect.move_ip(-dx, 0)
        # If x and y both are NOT growing
        elif x0 == x1 and y0 > y1:
#            print "y <-"
            return rect.move_ip(-int((self.offset+dx)/2), -int((self.offset+dy)/2))
        # If x is NOT growing and y is unchanged  
        elif x0 > x1 and y0 == y1:
#            print "x <-"
            return rect.move_ip(-dx, -int((self.offset+dy)/2))
        # If both x and y are growing
        elif x0 > x1 and y0 > y1:
            print "x <-, y <-"
            rect.move_ip(-dx, -dy)
        return rect
    
    def draw(self):
        print "Drawing line on %s"%self.line_surface
        return self.redraw()
    
    def redraw(self):
        # Reset canvas
        self.line_surface.fill(self.colorkey)
        # Redraw line        
        self._rect = pygame.draw.line(self.line_surface, self.line_color, 
                                      self.start, self.end, self.line_width)
        # Adjust the Rect that appears
        self._adjust_rect(self.rect, self.super_canvas_start[0],
                                     self.super_canvas_start[1],
                                     self.super_canvas_end[0],
                                     self.super_canvas_end[1])
#        print 'Line\nRect: %s\nSurface: %s\n'%(self.rect, self.image)
        return self.line_surface
    
# Imports into package
from lines import Lines
    