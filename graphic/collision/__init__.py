from abc import ABCMeta, abstractproperty

class Collidable(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.colorkey = None
        self.alpha = None
        self._hitmask = None
    @abstractproperty
    def rect(self):
        pass
    
    @abstractproperty
    def hitmask(self):
        pass