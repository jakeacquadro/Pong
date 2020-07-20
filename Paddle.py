import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, paddle_width, paddle_height, init_x, init_y):
        # create surface
        self.surf = pygame.Surface((paddle_width,paddle_height))
        self.surf.fill((255,255,255))
        # get rectangle
        self.rect = self.surf.get_rect(center = (init_x, init_y))
