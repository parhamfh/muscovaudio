'''
Created on 30 maj 2012

@author: emser
'''

from event.manager import EventManager
from event.hook.ball import BallCollision
from event.hook.ball import LineCollision

class SoundHandler(object):
    """
        Handles Ball collision
    """
    def __init__(self, osc_player):
        self.osc_player = osc_player
        self.em = EventManager()
        self.em[BallCollision] += self.send_sound
        self.em[LineCollision] += self.send_linecollision 
        # self.em[WallCollision] += self.send_sound
        
    def send_sound(self,ball,ball2):
        # send x,y coordinates for both balls when colliding
        #print 'boundary ball 1', ball.boundary
        #print 'boundary ball 2', ball2.boundary
        x1 = ball.boundary[0]
        y1 = ball.boundary[1]
        x2 = ball2.boundary[0] 
        y2 = ball2.boundary[1]
        #print 'X1', x1, 'X2', y1
        #print 'Y1', x2, 'Y2', y2
        x = (x1+x2)/2
        y = (y1+y2)/2
        self.osc_player.send_message("%s %s"%(x,y),'/soundhandler/collision')
        
    
    def send_linecollision(self):
        # send 'bang' when ball collides with line 
        message = 'bang'
        self.osc_player.send_message(message,'/soundhandler/linecollision') 
        pass 
 
    
    def send_wallcollision(self):
        # TODO: fix 
        pass 
        #self.osc_player.send_message(1,'/soundhandler/collision/wall')
    

