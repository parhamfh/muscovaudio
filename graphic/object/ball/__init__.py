import pygame 

class Ball(object):

    def __init__(self, x_init, y_init, r, velocity):
        self.x = x_init
        self.y = y_init
        self.radius = r 
        self.velocity = []
        self.velocity.extend(velocity)
        self.ball_image = pygame.image.load('../../../ball.png').convert_alpha()
        self.ball_boundary = self.ball_image.get_rect(center=(x_init,y_init))

