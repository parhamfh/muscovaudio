'''
Created on May 26, 2012

@author: pfh
'''

import pygame
from pygame import Surface
from pygame.font import Font

from colour import Colour

class Canvas(Surface):
    
    def __init__(self, width = 630, height = 470, color = Colour.GOLFGREEN):
        super(Canvas, self).__init__((width, height))
        
        # Canvas color
        self.color = color
        
        # Canvas for temporary lines
        self.work_canvas = Surface((width, height)) 
        self.work_canvas.set_colorkey(color)
        
        # Canvas for drawn lines 
        self.line_canvas = Surface((width, height))
        self.line_canvas.fill(self.color)


        # List of lines
        self.lines = []
        
        # Mouse info text position on Canvas
        self.mouse_info_x = 0
        self.mouse_info_y = 0
        self.mouse_info_canvas = Surface ((200,100))
        self.mouse_info_canvas.set_colorkey(color)
        
        # Fill the auxilliary canvases so that they become transparent
        self.work_canvas.fill(self.color)
        self.mouse_info_canvas.fill(self.color)
    
    def set_global_position(self, x, y):
        '''
        The Canvas position in the containing Window
        '''
        self.global_x = x
        self.global_y = y
    def draw_measuring_line(self,start,end):
        # Erase old measuring line
        self.work_canvas.fill(self.color)
        # Draw new measuring line
        pygame.draw.line(self.work_canvas, Colour.AQUAMARINE, start, end)
    
    def draw_line(self,start,end):
        # Draw an actual, permanent line and erase measuring line
        self.work_canvas.fill(self.color)
#        self.mouse_info_canvas.fill(self .color)
        pygame.draw.line(self.line_canvas, Colour.TURQUOISE, start, end, 5)
    
    def draw_mouse_info(self, message, drawing=False):
        # Empty mouse canvas
        self.mouse_info_canvas.fill(self.color)
        # Create font and blit onto canvas
        font = Font(None, 22)
        mouse_info = font.render(message, 1, Colour.WHITE, Colour.BLUE)
        self.mouse_info_canvas.blit(mouse_info, (self.mouse_info_x, self.mouse_info_y))
        
        # If Mouse is dragging, notify
        if drawing:
            ti = Font(None, 30).render("DRAWING",1,Colour.CHOCOLATE, Colour.WHITE)
            self.mouse_info_canvas.blit(ti, (self.mouse_info_x, self.mouse_info_y+20))
    
    def draw_content(self):
        # Draw the stuff on the canvas 
        self.blit(self.line_canvas,(0,0))
        self.blit(self.work_canvas,(0,0))
        self.blit(self.mouse_info_canvas,(self.get_width()-240,self.get_height()-80))
