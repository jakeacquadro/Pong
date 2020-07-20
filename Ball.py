import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, ball_len, init_x, init_y, speed, screen_height, screen_width):
        self.surf = pygame.Surface((ball_len,ball_len))
        self.surf.fill((255,255,255))
        # get rectangle
        self.rect = self.surf.get_rect(center = (init_x, init_y))
        self.init_speed = speed
        self.x_speed = speed
        self.y_speed = 2*speed/3
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.init_x = init_x
        self.init_y = init_y

    def update(self):

        self.rect.move_ip(self.x_speed, self.y_speed)

        # make ball bounce off of walls
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y_speed = -self.y_speed # reverse speed when hitting wall
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
            self.y_speed = -self.y_speed
        

    def reverse(self):
        self.x_speed = -self.x_speed

    def reset(self):
        self.rect.x = self.init_x
        self.rect.y = self.init_y
        self.reverse()
