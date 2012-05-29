import pygame 

class Ball(object):

    def __init__(self, x_init, y_init, r, velocity):
        self.x = x_init
        self.y = y_init
        self.radius = r 
        self.velocity = []
        self.velocity.extend(velocity)
        # TODO: fix correct path 
        self.image = pygame.image.load('resources/img/ball.png').convert_alpha()
        self.boundary = self.image.get_rect(center=(x_init,y_init))

