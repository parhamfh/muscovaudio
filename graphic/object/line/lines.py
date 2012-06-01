'''
Created on May 31, 2012

@author: parhamfh
'''
#from pygame import Surface

from graphic.object.line import Line
from graphic.colour import Colour

# TODO make inherit from list
class Lines(object):
    def __init__(self, line_color, colorkey, super_canvas):
        # Amount = number of balls on canvas 
        # Ball boundaries 
        self.lines = []
        self.line_color = line_color
        self.colorkey = colorkey
        self.super_canvas = super_canvas

    def draw_line(self, x0, y0, x1, y1):
        line = Line(x0,y0,x1,y1, self.line_color, self.colorkey)
        line.draw()
        self.super_canvas.blit(line.line_surface, line.rect)
        self.lines.append(line)

    def __iter__(self):
        return iter(self.lines)

    def redraw(self):
        self.super_canvas.fill(self.colorkey)

        for line in self.lines:
            self.super_canvas.blit(line.redraw(), line.rect)
            line.redraw()
