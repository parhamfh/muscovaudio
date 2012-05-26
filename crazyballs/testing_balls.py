import pygame
import random
import sys

class Ball:
    def __init__(self,X,Y):
        self.velocity = [3,3] # hypotenusan
        self.ball_image = pygame.image.load ('ball.png'). convert_alpha() # alpha : transparency background
        self.ball_boundary = self.ball_image.get_rect (center=(X,Y))
        self.sound = pygame.mixer.Sound ('Thump.wav')

if __name__ =='__main__':
    width = 700
    height = 500
    background_colour = 250,250,250
    pygame.init()
    frame = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BALLS!!!")
    num_balls = 3
    ball_list = []
    for i in range(num_balls):
        # add ball-object with random coordinates for every item in num_balls to ball_list
        ball_list.append( Ball(random.randint(0, width),random.randint(0, height)) )
        # coordinates? 

    while True:
        for event in pygame.event.get():
                #print event 
                if event.type == pygame.QUIT: 
                        sys.exit(0)
        frame.fill (background_colour)

        for ball in ball_list:
                if ball.ball_boundary.left < 0 or ball.ball_boundary.right > width:
                        ball.velocity[0] = -1 * ball.velocity[0]
                if ball.ball_boundary.top < 0 or ball.ball_boundary.bottom > height:
                        ball.velocity[1] = -1 * ball.velocity[1]

                ball.ball_boundary = ball.ball_boundary.move (ball.velocity)
                frame.blit (ball.ball_image, ball.ball_boundary)
        pygame.display.flip()