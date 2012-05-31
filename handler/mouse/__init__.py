'''
Created on May 27, 2012

@author: parhamfh
'''
import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from event.manager import EventManager
from event.hook.mouse import ButtonPressed
from mouse import Mouse

class MouseHandler(object):
    
    def __init__(self, canvas, osc_player):
        
        self.canvas = canvas    
        self.mouse = Mouse()
        self.osc_player = osc_player
        self.em = EventManager()
        self.em[ButtonPressed] += self.handle_event
       
        # Mouse action 
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.drag_end_x = 0
        self.drag_end_y = 0
        
    def handle_event(self, event):
        # Get mouse position
        (self.mouse_x, self.mouse_y) = pygame.mouse.get_pos()
        
        # TODO: find better programmatical solution for addition
        # Now you can also draw lines from outside canvas
        self.mouse_x= self.mouse_x-self.canvas.global_x
        self.mouse_y= self.mouse_y-self.canvas.global_y
        
        
        # Check if the event is mouse-related
        if event.type == MOUSEBUTTONDOWN:
            self.mouse.mouse_pressed()
            self.mouse.set_button_pressed(event.button)
                
        elif event.type == MOUSEBUTTONUP:
            self.mouse.mouse_released()
            self.mouse.set_button_pressed(event.button)
        
        self.measure_line()
        # Write out mouse info
        self.write_mouse_info()
    
    def measure_line(self):
        if not self.mouse.dragging and self.mouse.mouse_down and self.mouse.left_button_pressed:
            self.drag_start_x = self.mouse_x
            self.drag_start_y = self.mouse_y
            self.drag_end_x = self.mouse_x
            self.drag_end_y = self.mouse_y
            self.mouse.set_dragging(True)
            
        elif self.mouse.dragging and self.mouse.mouse_down and self.mouse.left_button_pressed:
            self.drag_end_x = self.mouse_x
            self.drag_end_y = self.mouse_y 
            self.canvas.draw_measuring_line((self.drag_start_x,self.drag_start_y),(self.drag_end_x, self.drag_end_y))
            
            # Send x and y dragging values to PD
            # TODO: restrict to canvas borders
            self.osc_player.send_message(self.drag_end_x, "/mouse/x")
            self.osc_player.send_message(self.drag_end_y, "/mouse/y")
            
        elif self.mouse.dragging and not self.mouse.mouse_down and self.mouse.left_button_pressed:
            self.mouse.set_dragging(False)
            self.canvas.draw_line((self.drag_start_x,self.drag_start_y),(self.drag_end_x, self.drag_end_y))

    def write_mouse_info(self):
        
        # Build string
        message = "x = %s "\
                  "y = %s"%(self.mouse_x, self.mouse_y)
        
        # If key pressed add that info
        if self.mouse.mouse_down:
            message = message + " %s"%self.mouse.button_pressed

        # Draw Mouse info on canvas
        self.canvas.draw_mouse_info(message,self.mouse.dragging)        
