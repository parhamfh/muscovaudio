'''
Created on May 28, 2012

@author: parhamfh
'''

class Keyboard(object):
    '''
    A class representing the computers keyboard.
    '''

    KEYS = []
    
    def __init__(self):
        '''
        Constructor
        '''
        self.buttons_pressed = []