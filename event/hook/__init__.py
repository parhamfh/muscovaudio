from abc import ABCMeta

class EventHook(object):
    __meta__ = ABCMeta
    
    def __init__(self):
        self.handlers = []
    
    @classmethod
    def class_name(cls):
        return cls.__name__
    
    @staticmethod
    def fire_blank(resound, *args, **keywargs):
        """
            WARNING! CONFUSING STATIC FUNCTION!
            Use this function to try the event hooks fire function. It simply
            echoes the arguments
            
            Usage:
                    event_hook_instance += EventHook.fire_blank 
        """ 
        print resound
        
    def __iadd__(self, handler):
        self.handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self

    def __len__(self):
        return len(self.handlers)
    
    def fire(self, *args, **keywargs):
        for handler in self.handlers:
            if handler is not None:
                handler(*args, **keywargs)
