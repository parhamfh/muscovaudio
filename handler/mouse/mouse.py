'''
Created on May 27, 2012

@author: parhamfh
'''
class Mouse(object):
    
    BUTTONS = {1:"Left Button", 3:"Right Button", 4: "Up", 5: "Down"}
    
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