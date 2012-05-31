'''
Created on May 31, 2012

@author: parhamfh
'''

from graphic.object.line import Line

# TODO make inherit from list
class Lines(object):

    def __init__(self, boundary_width, boundary_height):
        # Amount = number of balls on canvas 
        self.amount = amount 
        self.start_velocity = start_velocity 
        # Ball boundaries 
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        
        self.create_balls()