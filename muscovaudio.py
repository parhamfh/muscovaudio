#!/usr/local/bin/python

import sys
from __init__ import add_lib_to_path
add_lib_to_path()

import pygame
print "Using pygame from: %s"%pygame.__file__
from pygame.locals import KEYDOWN, K_ESCAPE

from graphic.window import Window
from handler.mouse import MouseHandler
from handler.keyboard import KeyboardHandler
from handler.sound import SoundHandler 
from audio.osc.player import OSCPlayer
from event.manager import EventManager
from event.hook.keyboard import KeyPressed
from event.hook.mouse import ButtonPressed


class Muscovaudio(object):
    def __init__(self):
        print "init"
            
    def run(self):
        print "running"
        # Initialize pygame
        pygame.init()
        
        # Pygame.display stuff
        pygame.display.set_caption('MUSCOVAUDIO')
        
        # Create & init application Window 
        self.window = Window()
        self.window.init_window()
        
        # Create OSCPlayer
        self.osc_player = OSCPlayer('127.0.0.1', 9001, "/muscovaudio")
        # Connect OSCPlayer
        self.osc_player.open_connection()
        
        # Init MouseHandler against the mouse
        self.mh = MouseHandler(self.window.get_canvas(), self.osc_player)
        self.kh = KeyboardHandler(self.window.get_canvas())
        self.sh = SoundHandler(self.osc_player)

        
        # Update the pygame display
        self.window.draw()
        
        # Send start signal
        self.osc_player.send_message(440, '/start')
        
        # Create Event Manager
        self.em = EventManager()
        
        
        for hook in self.em:
            print hook
        try:
            while True:
                    # Check events
                    events = pygame.event.get()
                    for e in events:
                        self.em[ButtonPressed].fire(e)
                        if e.type == pygame.QUIT:
                        # Enables user to close the program using the mouse 
                            raise KeyboardInterrupt
                        elif e.type == KEYDOWN:
                            # Check if user has aborted
                            if e.key == K_ESCAPE:
                                raise KeyboardInterrupt
                            else:
                                self.em[KeyPressed].fire(e)
                    # Update the pygame display
                    self.window.draw()
                    
        except KeyboardInterrupt:
            print "Closing Muscovaudio"
            # Do closing stuff here
            pygame.quit()
            self.osc_player.close_connection()
            print "Done"    
            sys.exit(0)


if __name__ == "__main__":
    muscovaudio = Muscovaudio()
    muscovaudio.run()
    

