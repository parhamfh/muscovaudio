import random
from collections import MutableMapping

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
class EventManager(MutableMapping):
    """
        NOT SUPPORTED:
        event_manager[ButtonPressed] = 'a' (must use __name__)
        
        SUPPORTED:
        event_manager[ButtonPressed] (returns list of handlers registered on
                                     ButtonPressed)
        
        USAGE:
        event_manager[ButtonPressed] += handler.event_handler # Add handler
        event_manager[ButtonPressed].fire('Bang!')            # Notify handlers 
        event_manager[ButtonPressed} -= handler.event_handler # Remove handler
        
        The EventManager is basically a wrapper of the dictionary that 
        allows for fancy class name keys to be used to index the underlying
        dict.
        
        TODO: Should I implement __contains__() ?
        
    """
    def __init__(self):
        # make singleton
        self.id = random.randint(0,1001)
        self._event_to_handler_map = dict()
        
    @property
    def event_to_handler_map(self):
        return self._event_to_handler_map
    
    def __getitem__(self, event_hook):
        
        # If it is a string it might be the name of an EventHook class
        if isinstance(event_hook, str):
            return self.event_to_handler_map[event_hook]
        
        # Else try using the class_name() function
        if not self.event_to_handler_map.has_key(event_hook.class_name()):
            print "Event Hook '%s' did not exist. Creating..."%event_hook.class_name()
            self.event_to_handler_map[event_hook.class_name()] = event_hook()

        return self.event_to_handler_map[event_hook.class_name()]
        
    def __setitem__(self, event_hook, value):
        if isinstance(event_hook, str):
            # See if its an EventHook class name string
            self.event_to_handler_map[event_hook] = value
        else:
            # Assume it is an EventHook Class
            self.event_to_handler_map[event_hook.class_name()] = value

    def __delitem__(self, event_hook):
        del self.event_to_handler_map[event_hook.class_name()]

    def __iter__(self):
        return iter(self.event_to_handler_map)

    def __len__(self):
        return len(self.event_to_handler_map)
