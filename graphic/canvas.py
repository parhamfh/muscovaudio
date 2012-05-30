'''
Created on May 26, 2012

@author: pfh
'''

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

from graphic.colour import Colour
from graphic.object.line import Line
from graphic.object.ball import Balls

class Canvas(Surface):
    
    def __init__(self, boundary_width = 630, boundary_height = 470, color = Colour.WHITE):
        super(Canvas, self).__init__((boundary_width, boundary_height))
        
        # Canvas color
        self.color = color
        
        # Canvas for temporary lines
        self.work_canvas = Surface((boundary_width, boundary_height)) 
        self.work_canvas.set_colorkey(color)
        
        # Canvas for drawn lines 
        self.line_canvas = Surface((boundary_width, boundary_height))
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
        
        # Create empty Ball Canvas
        self.ball_canvas = None
        
    def set_global_position(self, x, y):
        '''
        The Canvas position in the containing Window
        '''
        self.global_x = x
        self.global_y = y
        
    def create_balls(self):
        self.balls = Balls(3,[3,3],300, 300)
        self.ball_canvas = Surface((self.get_width(),self.get_height()))
        self.ball_canvas.set_colorkey(self.color)
        
    def draw_measuring_line(self,start,end):
        # Erase old measuring line
        self.work_canvas.fill(self.color)
        # Draw new measuring line
        pygame.draw.line(self.work_canvas, Colour.GOLFGREEN, start, end)
    
    def draw_line(self,start,end):
        # Draw an actual, permanent line and erase measuring line
        self.work_canvas.fill(self.color)
#        self.mouse_info_canvas.fill(self .color)
        pygame.draw.line(self.line_canvas, Colour.BLUE, start, end, 5)
        self.lines.append(Line(start,end, Colour.BLUE))
    
    def draw_mouse_info(self, message, drawing=False):
        # Empty mouse canvas
        self.mouse_info_canvas.fill(self.color)
        # Create font and blit onto canvas
        font = Font(None, 22)
        mouse_info = font.render(message, 1, Colour.CHOCOLATE, Colour.BLACK)
        self.mouse_info_canvas.blit(mouse_info, (self.mouse_info_x, self.mouse_info_y))
        
        # If Mouse is dragging, notify
        if drawing:
            ti = Font(None, 30).render("DRAWING",1,Colour.CHOCOLATE, Colour.BLACK)
            self.mouse_info_canvas.blit(ti, (self.mouse_info_x, self.mouse_info_y+20))
    
    def draw_balls(self):
        self.ball_canvas.fill(self.color)
        # Do all kinds of checkings
        self.balls.detect_collisions(self.lines,
                                     self.get_width(),self.get_height())
        self.balls.move_balls()
        self.balls.blit_balls(self.ball_canvas)
        
    def move_lines(self, direction):
        if direction == K_RIGHT:
            (x, y) = (3, 0)
            print "moving lines to the right with vector (%s,%s)"%(x,y)
        elif direction == K_LEFT:
            (x, y) = (-3, 0)
            print "moving lines to the left with vector (%s,%s)"%(x,y)
        elif direction == K_UP:
            (x, y) = (0, -3)
            print "moving lines up with vector (%s,%s)"%(x,y)
        elif direction == K_DOWN:
            (x, y) = (0, 3)
            print "moving lines down with vector (%s,%s)"%(x,y)

        for line in self.lines:
            line.move((x, y))
    
    def update_content(self):
        # Clear out line_canvas and read
        self.line_canvas.fill(self.color)
        for line in self.lines:
            pygame.draw.line(self.line_canvas, line.colour, line.start, line.end, 5)
            
    def draw_content(self):
        self.update_content()
        # Draw the stuff on the canvas 
        self.blit(self.line_canvas,(0,0))
        self.blit(self.work_canvas,(0,0))
        self.blit(self.mouse_info_canvas,(self.get_width()-240,self.get_height()-80))
        
        if self.ball_canvas is not None:
            self.blit(self.ball_canvas, (0,0))
