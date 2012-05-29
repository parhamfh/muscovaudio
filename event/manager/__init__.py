import random

from ..hook.mouse import ButtonPressed

def singleton(cls):
    '''
        Standard implementation of @singleton decorator
        to allow use of Singleton pattern according to PEP-318
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
        # make singleton
        self.id = random.randint(0,1001)
        self._event_to_handler_map = EventHandlerMap()
    
    @property
    def event_to_handler_map(self):
        return self._event_to_handler_map
    
    def register(self):
        pass
    
    
    def __getitem__(self, key):
        return self.event_to_handler_map[key]

    def debug_test_event_handler_map(self):
        self.event_to_handler_map[ButtonPressed.__name__] = ButtonPressed()
        self.event_to_handler_map[ButtonPressed] += ButtonPressed.fire_blank
        self.event_to_handler_map[ButtonPressed].fire('BANG BANG SHOOT SHOOT')
    
class EventHandlerMap(dict):
    """
        NOT SUPPORTED:
        self.event_to_handler_map[ButtonPressed] = 'a' (must use __name__)
        
        SUPPORTED:
        self.event_to_handler_map[ButtonPressed] (returns list of handlers)
        
        USAGE:
        self.event_to_handler_map[ButtonPressed] += event_handler
    """
    def __getitem__(self, event_class, *args, **kwargs):
#        print event_class.class_name()
        if not self.has_key(event_class.class_name()):
            print "Event Hook %s did not exist. Creating..."%event_class.class_name()
            self[event_class.class_name()] = event_class()
        return dict.__getitem__(self, event_class.class_name(), *args, **kwargs)
