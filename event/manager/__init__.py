import random


def singleton(cls):
    '''
        Standard implementation of Singleton pattern
        using @singleton decoration according to PEP-318
    '''
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class EventManager(object):

    def __init__(self):
        print self
        # make singleton
        self.handlers = []
        self.id = random.randint(0,1001)
    
    def register(self):
        pass
    
    def __iadd__(self, handler):
        self.handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self
#
#    def fire(self, *args, **kwargs):
#        for handler in self.handlers:
#            handler(*args, **kwargs)
#
#    def clearObjectHandlers(self, inObject):
#        for handler in self.handlers:
#            if handler.im_self == inObject:
#                self -= handler


