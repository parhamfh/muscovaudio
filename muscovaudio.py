#!/usr/local/bin/python

import sys

import OSC
import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import KEYDOWN, K_ESCAPE

class Colour(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    AQUAMARINE = (127 ,255, 212)
    CHOCOLATE = (255, 127, 36)
    TURQUOISE = (0, 245, 255)
    GOLFGREEN = (0,100,27)
    
class Muscovaudio(object):
    def __init__(self):
        print "init"
            
    def run(self):
        print "running"
        # Initialize pygame
        pygame.init()
            
        # Pygame.display stuff
        pygame.display.set_caption('MUSCOVAUDIO')
        
        # Create canvas
        self.canvas = Canvas()
        
        # Create mouse canvas
        
        # Create & init application Window 
        self.window = Window()
        self.window.init_window()
        
        # Add our canvas to the window
        self.window.add_canvas(self.canvas)
        
        # Create OSCPlayer
        self.osc_player = OSCPlayer('127.0.0.1', 9000, "/muscovaudio")
        # Connect OSCPlayer
        self.osc_player.open_connection()
        
        # Init MouseHandler against our mouse
        self.mouse = Mouse()
        self.mh = MouseHandler(self.mouse, self.canvas, self.osc_player)
        
        # Update the pygame display
        self.window.draw()
        pygame.display.update()    
            
            
# Test sound
        self.osc_player.send_message(440, '/play')
        try:
            while True:
                    # Check events
                    events = pygame.event.get()
                    for e in events:
                        self.mh.handle_event(e) 
                        if e.type == pygame.QUIT:
                        # Enables user to close the program using the mouse 
                            sys.exit(0)
                        if e.type == KEYDOWN:
                            # Check if user has aborted
                            if e.key == K_ESCAPE:
                                raise KeyboardInterrupt
                    # Update the pygame display
                    self.window.draw()
                    pygame.display.update()


        except KeyboardInterrupt:
            print "Closing Muscovaudio"
            # Do closing stuff here
            pygame.quit()
            self.osc_player.close_connection()                    
            print "Done"    
            sys.exit(0)
            
class Canvas(Surface):
    
    def __init__(self, width = 630, height = 470, color = Colour.BLACK):
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
        
class Window(object):
    
    def __init__(self, width=800, height=600, bkg_color=Colour.WHITE):
        self.width = width
        self.height = height
        self.background_color = bkg_color
        self.window = None
        self.init_window()
        self.canvas = None
        
    def add_canvas(self, canvas, canvas_x=100, canvas_y=100):
        self.canvas = canvas
        self.canvas_x = canvas_x
        self.canvas_y = canvas_y
        self.canvas.set_global_position(canvas_x, canvas_y)
        
    def draw(self):
        self.canvas.draw_content()
        self.window.blit(self.canvas, (self.canvas_x,self.canvas_y))
        
    def init_window(self):
        self.window = pygame.display.set_mode((self.width,self.height))
        self.window.fill(self.background_color)
        
    def change_background_color(self, color):
        self.window.fill(color)
    
    def blit(self, canvas, pos):
        self.window.blit(canvas, pos)

class MouseHandler(object):
    
    def __init__(self, mouse, canvas, osc_player):
        
        self.canvas = canvas    
        self.mouse = mouse
        self.osc_player = osc_player
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse.mouse_pressed()
            self.mouse.set_button_pressed(event.button)  
                
        elif event.type == pygame.MOUSEBUTTONUP:
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

    
class Mouse(object):
    
    BUTTONS = {1:"Left Button", 3:"Right Button"}
    
    def __init__(self):
        self.mouse_down = False
        self.button_pressed = "None"
        self.swiping = False
        
    def mouse_pressed(self):
        self.mouse_down = True
    
    def mouse_released(self):
        self.mouse_down = False
    
    @property
    def dragging(self):
        return self.swiping
        
    def set_dragging(self, sw):
        self.swiping = sw
        
    @property
    def left_button_pressed(self):
        return self.button_pressed == "Left Button"
    
    def set_button_pressed(self, button):
        self.button_pressed = self.BUTTONS[button]

class OSCPlayer(object):
    def __init__(self, ip_address, port, osc_address):
        self.ip_address = ip_address
        self.port = port
        self.base_osc_address = osc_address
        self.client = OSC.OSCClient()

    def open_connection(self):
        try:
            self.client.connect((self.ip_address,self.port))
        except OSC.OSCClientError, o:
            print o
    
    def close_connection(self):
        self.send_message(0, '/stop')
        self.client.close()
    
    def send_message(self, message, osc_address):
        
        osc_message = OSC.OSCMessage("{0}{1}".format(self.base_osc_address, osc_address))
        osc_message.append(message)
        try:
            self.client.send(osc_message, 3)
        except OSC.OSCClientError, o:
            print o
        
    def send_bundle(self, bundle):
        raise NotImplementedError
    
    def set_address(self, address):
        self.osc_address = address

class Ball(object):

    def __init__(self, x_init, y_init, r, vel=0):
        self.x = x_init
        self.y = y_init
        self.radius = r
        self.velocity = vel

if __name__ == "__main__":
    muscovaudio = Muscovaudio()
    muscovaudio.run()