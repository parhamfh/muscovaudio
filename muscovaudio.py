#!/usr/local/bin/python

import sys

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE

from graphic.window import Window
from handler.mouse import MouseHandler
from audio.osc.player import OSCPlayer

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
        self.osc_player = OSCPlayer('127.0.0.1', 9000, "/muscovaudio")
        # Connect OSCPlayer
        self.osc_player.open_connection()
        
        # Init MouseHandler against the mouse
        self.mh = MouseHandler(self.window.get_canvas(), self.osc_player)
        
        # Update the pygame display
        self.window.draw()
                
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
                            raise KeyboardInterrupt
                        elif e.type == KEYDOWN:
                            # Check if user has aborted
                            if e.key == K_ESCAPE:
                                raise KeyboardInterrupt
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