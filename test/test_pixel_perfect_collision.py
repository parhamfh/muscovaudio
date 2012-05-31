'''
Created on May 30, 2012

@author: parhamfh
'''

import pygame, time
from pygame.locals import RLEACCEL
import graphic.collision.pixelperfect as pp 
import graphic.collision as c

def load_image(name, colorkey=None, alpha=False):
    """loads an image into memory"""
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if alpha:image = image.convert_alpha()
    else:image=image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
 
class my_object(object):
    def __init__(self, image,colorkey=None,alpha=None):
        self.image, self._collision_rect=load_image(image,colorkey=colorkey, alpha=alpha)
        if colorkey and alpha:
            self._collision_hitmask=c.get_colorkey_and_alpha_hitmask(self.image, self._collision_rect,
                                                        colorkey, alpha)
        elif colorkey:
            self._collision_hitmask=c.get_colorkey_hitmask(self.image, self._collision_rect,
                                              colorkey)
        elif alpha:
            self._collision_hitmask=c.get_alpha_hitmask(self.image, self._collision_rect,
                                           alpha)
        else:
            self._collision_hitmask=c.get_full_hitmask(self.image, self._collision_rect)
 
pygame.init()
screen = pygame.display.set_mode([200,200])
screen.fill([255,255,255])
 
 
a=my_object('../resources/img/ball.png',-1,None)
a._collision_rect.center=(25,25)
 
b=my_object('../resources/img/ball.png',None,True)
b._collision_rect.center=(50,50)
 
screen.blit(a.image, a._collision_rect)
screen.blit(b.image, b._collision_rect)
pygame.display.flip()
 
def main():
    av=0
    for i in xrange(20000):
        st_time=time.clock()
        pp.check_collision(a, b)
        av+=time.clock()-st_time
 
    print "time:", av, pp.check_collision(a, b)
 
main()