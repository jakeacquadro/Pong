import pygame
import Paddle

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_a,
    K_z
)

class Human:

    def __init__(self, pad, screen_height, key_1, key_2):
        self.paddle = pad
        self.screen_height = screen_height
        self.key_1 = key_1
        self.key_2 = key_2

    def update(self, pressed_keys):
        if pressed_keys[self.key_1]:
            self.paddle.rect.move_ip(0, -5)
        if pressed_keys[self.key_2]:
            self.paddle.rect.move_ip(0, 5)

        if self.paddle.rect.top <= 0:
            self.paddle.rect.top = 0
        if self.paddle.rect.bottom >= self.screen_height:
            self.paddle.rect.bottom = self.screen_height
