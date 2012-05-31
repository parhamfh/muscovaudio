from abc import ABCMeta, abstractproperty

class Collidable(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.colorkey = None
        self.alpha = None
        self._hitmask = None
    @abstractproperty
    def _collision_rect(self):
        pass
    
    @abstractproperty
    def _collision_hitmask(self):
        pass

    def _calculate_hitmask(self):
        # TODO: This might be dangerous if class has None as 
        # self.colorkey or self.alpha since value None has implications 
        # on collisions detection.
        if self.colorkey and self.alpha:
            self._hitmask=get_colorkey_and_alpha_hitmask(
                                    self.image, self.rect, 
                                    self.colorkey, self.alpha)
        elif self.colorkey:
            self._hitmask=get_colorkey_hitmask(
                                    self.image, self.rect, self.colorkey)
        elif self.alpha:
            self._hitmask=get_alpha_hitmask(
                                    self.image, self.rect, self.alpha)
        else:
            self._hitmask=get_full_hitmask(self.image, self.rect)

def get_colorkey_hitmask(image, rect, colorkey=None):
    """returns a hitmask using an image's colorkey.
       image->pygame Surface,
       rect->pygame Rect that fits image,
       key->an over-ride color, if not None will be used instead of the image's colorkey"""
    if colorkey is None:
        colorkey=image.get_colorkey()
    
    mask=[]
    for x in range(rect.width):
        mask.append([])
        for y in range(rect.height):
            mask[x].append(not image.get_at((x,y)) == colorkey)
    return mask
 
def get_alpha_hitmask(image, rect, alpha=0):
    """returns a hitmask using an image's alpha.
       image->pygame Surface,
       rect->pygame Rect that fits image,
       alpha->the alpha amount that is invisible in collisions"""
    mask=[]
    for x in range(rect.width):
        mask.append([])
        for y in range(rect.height):
            mask[x].append(not image.get_at((x,y))[3]==alpha)
    return mask
 
def get_colorkey_and_alpha_hitmask(image, rect, colorkey=None, alpha=0):
    """returns a hitmask using an image's colorkey and alpha."""
    if colorkey is None:
        colorkey=image.get_colorkey()
    mask=[]
    for x in range(rect.width):
        mask.append([])
        for y in range(rect.height):
            mask[x].append(not (image.get_at((x,y))[3]==alpha or\
                                image.get_at((x,y))==colorkey))
    return mask
 
def get_full_hitmask(image, rect):
    """returns a completely full hitmask that fits the image,
       without referencing the images colorkey or alpha."""
    mask=[]
    for x in range(rect.width):
        mask.append([])
        for y in range(rect.height):
            mask[x].append(True)
    return mask