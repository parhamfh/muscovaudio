'''
Created on May 29, 2012

@author: pfh
'''
class Line(object):
    
    def __init__(self, start, end, colour):
        self.start = start
        self.end = end
        self.colour = colour
        
    def move(self, (x,y)):
        self.start = (self.start[0] + x, self.start[1]+ y)
        self.end = (self.end[0] + x, self.end[1] + y)