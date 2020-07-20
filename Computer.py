import pygame
import Paddle


class Computer:

    def __init__(self, paddle, screen_height, distance):
        self.paddle = paddle
        self.screen_height = screen_height
        # use a variable distance which is how many pixels away the ball must be
        # before the paddle adjusts to hit it
        self.distance = distance

    def update(self, ball_x, ball_y):
        if self.paddle.rect.x - ball_x < self.distance:
            if self.paddle.rect.y > ball_y:
                self.paddle.rect.move_ip(0, -5)
            elif self.paddle.rect.y < ball_y:
                self.paddle.rect.move_ip(0, 5)

        if self.paddle.rect.top <= 0:
            self.paddle.rect.top = 0
        if self.paddle.rect.bottom >= self.screen_height:
            self.paddle.rect.bottom = self.screen_height
