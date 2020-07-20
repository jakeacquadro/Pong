import pygame
import pygame_menu
from Paddle import Paddle
from Human import Human
from Ball import Ball
from Computer import Computer

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_a,
    K_z
)
class Game:

    # constructor (runs game)
    def __init__(self):
        # initialize variables
        self.gamemode = 1
        self.difficulty = 1

        self.screen_width = 700
        self.screen_height = 400

        # initialize the display module
        pygame.init()
        pygame.display.set_caption('Pong')

        # screen is a Surface object
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])

        # create menu
        menu = pygame_menu.Menu(self.screen_height - 100, self.screen_width - 100, 'Pong',\
            theme=pygame_menu.themes.THEME_DARK)
        menu.add_selector('Difficulty:', [('Beginner', 1), ('Intermediate', 2), ('Expert', 3)], onchange= self.set_difficulty)
        menu.add_selector('Gamemode:', [('Player vs Player', 1), ('Computer vs Player', 2)], onchange= self.set_gamemode)
        menu.add_button('Play', self.game_loop)
        menu.add_button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

        pygame.display.quit()
        pygame.quit()
        sys.exit()



    # sets self.difficulty
    def set_difficulty(self,value,diff):
        self.difficulty = diff

    # sets self.gamemode where 1 is Player vs Player, 2 is Computer vs Player
    def set_gamemode(self,value,mode):
        self.gamemode = mode

    def game_loop(self):
        if self.difficulty == 1:
            speed = 5
            distance = 30
        elif self.difficulty == 2:
            speed = 6
            distance = 40
        elif self.difficulty == 3:
            speed = 8
            distance = 40

        # fill screen with black
        self.screen.fill((0,0,0))

        # add scoreboard
        font = pygame.font.Font('freesansbold.ttf', 32)

        score1 = 0
        score1_text = font.render(str(score1), True, (255,255,255))
        score1_rect = score1_text.get_rect()

        score2 = 0
        score2_text = font.render(str(score2), True, (255,255,255))
        score2_rect = score2_text.get_rect()

        score1_rect.center = (self.screen_width/2 - 50, 20)
        score2_rect.center = (self.screen_width/2 + 50, 20)

        # add two paddles
        paddle_width = 20
        paddle_height = 110

        # paddle starting coordinates
        init_x_1 = 5*self.screen_width/6 - paddle_width/2
        init_y_1 = self.screen_height/2 - paddle_height/2

        init_x_2 = self.screen_width/6 - paddle_width/2
        init_y_2 = self.screen_height/2- paddle_height/2

        # create paddles
        right_paddle = Paddle(paddle_width, paddle_height, init_x_1, init_y_1)
        left_paddle = Paddle(paddle_width, paddle_height, init_x_2, init_y_2)


        # create first paddle
        right_paddle.rect.x = init_x_1 # update position of paddle
        right_paddle.rect.y = init_y_1
        self.screen.blit(right_paddle.surf, (init_x_1, init_y_1)) # put paddle on screen

        # create second paddle
        left_paddle.rect.x = init_x_2 # update position of paddle
        left_paddle.rect.y = init_y_2
        self.screen.blit(left_paddle.surf, (init_x_2, init_y_2))

        # create human characters
        human_1 = Human(right_paddle, self.screen_height, K_UP, K_DOWN)
        # create second human if necessary
        if self.gamemode == 1:
            human_2 = Human(left_paddle, self.screen_height, K_a, K_z)
        # create computer if necessary
        elif self.gamemode == 2:
            computer = Computer(left_paddle, self.screen_height, distance)

        # create ball
        ball_len = 10
        init_x_ball = self.screen_width/2
        init_y_ball = self.screen_height/2
        ball = Ball(ball_len, init_x_ball, init_y_ball, speed, self.screen_height, self.screen_width)
        self.screen.blit(ball.surf, (init_x_ball, init_y_ball)) # put ball on screen


        # keep game running until closed by user
        on = True

        # as long as this while loop is running (and by extension, the program),
        # the window stays open
        while on:

            # check for quit by user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on = False

            # update background before showing other objects
            self.screen.fill((0,0,0))


            # check for key press
            pressed_keys = pygame.key.get_pressed()

            # if key pressed, move paddle
            human_1.update(pressed_keys)
            if self.gamemode == 1:
                human_2.update(pressed_keys)
            elif self.gamemode == 2:
                computer.update(ball.rect.x, ball.rect.y)

            # check for collision
            if pygame.sprite.collide_rect(ball, right_paddle):
                ball.reverse()
            elif pygame.sprite.collide_rect(ball, left_paddle):
                ball.reverse()

            if ball.rect.right <= 0:
                ball.reset()
                ball.x_speed = ball.init_speed
                score2 += 1
                score2_text = font.render(str(score2), True, (255,255,255))
            if ball.rect.left >= ball.screen_width:
                ball.reset()
                ball.x_speed = -ball.init_speed
                score1 += 1
                score1_text = font.render(str(score1), True, (255,255,255))

            # update ball position
            ball.update()

            # update graphics
            self.screen.blit(right_paddle.surf, right_paddle.rect)
            self.screen.blit(left_paddle.surf, left_paddle.rect)
            self.screen.blit(ball.surf, ball.rect)
            self.screen.blit(score1_text, score1_rect)
            self.screen.blit(score2_text, score2_rect)

            # flip (refresh) the screen
            pygame.display.flip()
        pygame.display.quit()
        pygame.quit()
        sys.exit()
