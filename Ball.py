from wsgiref.validate import bad_header_value_re

import Player
from Utils import *


class Ball:
    x = 0
    y = 0
    speed = 1
    directionX = 0
    directionY = 1
    i = 1
    def __init__(self, x, y, speed = 0):
        self.x = x
        self.y = y
    def moveForward(self, player : Player):
        self.i += 1

        if self.i % 2 == 0:
            return
        self.x += self.directionX
        self.y += self.directionY
        # if self.y >= W_BOTTOM - OFFSET or self.y < BALL_SIZE + OFFSET and self.x in range(player.x, player.x + PADDLE_WIDTH):
        #     self.directionY *= -1


        # if self.y >= W_BOTTOM - BALL_SIZE - OFFSET  and self.x in range(player.x, player.x + PADDLE_WIDTH):
        #     self.directionY *= -1

        # if player is player1:

        if self.x >= WIDTH - BALL_SIZE or self.x <= 0:
            self.directionX *= -1
            paddle_sound_wall.play()

        if (self.y == HEIGHT - ball.get_height() - paddle.get_height() or self.y == paddle.get_height()) and player.x < self.x < (player.x + paddle.get_width()):
            self.directionY *= -1
            paddle_sound.play()
            return
        if self.y == HEIGHT - ball.get_height() - paddle.get_height() or self.y <= 0:
            self.directionY *= -1
            paddle_sound.play()
            return

        # if self.y >= W_BOTTOM - BALL_SIZE - OFFSET or self.y < BALL_SIZE + OFFSET:
        #     self.directionY *= -1

        # print(self.x, WIDTH)

        # if self.y == W_BOTTOM  and self.directionX == 0:
        #     self.directionX = 1
    def getCourdinates(self):
        return [self.x, self.y]
    def reset(self):
        self.x =  WIDTH // 2 - BALL_SIZE // 2
        self.y = HEIGHT // 2
        self.speed = 0.5
