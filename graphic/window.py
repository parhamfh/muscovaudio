'''
Created on May 26, 2012

@author: pfh
'''
import pygame

from colour import Colour
from canvas import Canvas

class Window(object):
    
    def __init__(self, width=800, height=600, bkg_color=Colour.WHITE, canvas=None):
        self.width = width
        self.height = height
        self.background_color = bkg_color
        self.window = None
        self.init_window()
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
        self.canvas.draw_content()
        self.window.blit(self.canvas, (self.canvas_x,self.canvas_y))
        pygame.display.update()
        
    def init_window(self):
        self.window = pygame.display.set_mode((self.width,self.height))
        self.window.fill(self.background_color)
        
    def change_background_color(self, color):
        self.window.fill(color)
    
    def blit(self, canvas, pos):
        self.window.blit(canvas, pos)