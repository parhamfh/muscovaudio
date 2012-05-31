'''
Created on 30 maj 2012

@author: emser
'''

from event.manager import EventManager
from event.hook.ball import BallCollision

class SoundHandler(object):
    """
        Handles Ball collision
    """
    def __init__(self, osc_player):
        self.osc_player = osc_player
        self.em = EventManager()
        self.em[BallCollision] += self.send_sound
        # self.em[LineCollision] += self.send_sound
        # self.em[WallCollision] += self.send_sound
        
    def send_sound(self, ball, ball2):
    
        # print ball
        # print ball2
        self.osc_player.send_message(67, '/soundhandler/collision')
