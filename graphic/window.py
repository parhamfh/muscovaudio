'''
Created on May 26, 2012

@author: pfh
'''
import pygame

from colour import Colour
from canvas import Canvas

class Window(object):
    
    def __init__(self, boundary_width=800, boundary_height=600, bkg_color=Colour.BLACK, canvas=None):
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        self.background_color = bkg_color
        self.window = None
        self.canvas = canvas if canvas else Canvas() 
        self.set_canvas_postion()
        
    def add_canvas(self, canvas, canvas_x=100, canvas_y=100):
        self.canvas = canvas
        self.set_canvas_position(canvas_x, canvas_y)
        self.canvas.set_global_position(canvas_x, canvas_y)
    
    def set_canvas_postion(self, canvas_x=100, canvas_y=100):
        self.canvas_x = canvas_x
        self.canvas_y = canvas_y
        self.canvas.set_global_position(canvas_x, canvas_y)
        
    def get_canvas(self):
        return self.canvas
        
    def draw(self):
        self.canvas.draw_balls()
        self.canvas.draw_content()
        self.window.blit(self.canvas, (self.canvas_x,self.canvas_y))
        pygame.display.update()
        
    def init_window(self):
        self.window = pygame.display.set_mode((self.boundary_width,self.boundary_height))
        self.window.fill(self.background_color)
        
        # Create Balls
        self.canvas.create_balls()
        
    def change_background_color(self, color):
        self.window.fill(color)
    
    def blit(self, canvas, pos):
        self.window.blit(canvas, pos)