from .. import EventHook 

class BallCollision(EventHook):
    pass

# If handler should only accept two balls: 

#    def fire(self, ball, ball2):
#        for handler in self.handlers:
#            if handler is not None:
#                handler(ball, ball2)  
