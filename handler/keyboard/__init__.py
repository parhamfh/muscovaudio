
from keyboard import Keyboard

from pygame.locals import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN
class KeyboardHandler(object):
    
    def __init__(self, canvas):
        self.keyboard = Keyboard()
        self.canvas = canvas
    
    def handle_event(self, event):
        
        # If not a Keyboard event, return
        if event.type != KEYDOWN: #and event.type != KEYUP:
            return
        
        # It is a key press
        if event.key == K_RIGHT:
            self.canvas.move_lines(K_RIGHT)
        elif event.key == K_LEFT:
            self.canvas.move_lines(K_LEFT)
        elif event.key == K_UP:
            self.canvas.move_lines(K_UP)
        elif event.key == K_DOWN:
            self.canvas.move_lines(K_DOWN)