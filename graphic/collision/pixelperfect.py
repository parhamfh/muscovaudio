'''
Created on May 30, 2012

@author: parhamfh
'''

def check_collision(obj1,obj2):
    """checks if two objects have collided, using hitmasks"""
    try:
        rect1 = obj1.rect
        rect2 = obj2.rect
        hitmask1 = obj1.hitmask
        hitmask2 = obj2.hitmask
    except AttributeError, ae:
        print ae
        raise
    
    rect=rect1.clip(rect2)
    
    if rect.width==0 or rect.height==0:
        return False
    
    x1 = rect.x-rect1.x
    y1 = rect.y-rect1.y
    x2 = rect.x-rect2.x
    y2 = rect.y-rect2.y
    
    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
            else:
                continue
    return False