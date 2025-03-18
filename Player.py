from pygame import K_LEFT, K_RIGHT

import Utils
from Ball import Ball
from Utils import *
class Player:
    x = 0
    y = 0
    speed: float = 2
    score = 0
    ball : Ball
    def __init__(self, x, y, ball):
        self.x = x
        if y == 0:
            pass
            self.y = 0
            # self.y = OFFSET
        else:
            self.y = y - OFFSET
        # self.speed = speed
        self.ball = ball
    def getCourdinates(self):
        return [self.x, self.y]
    def move(self, keyPressed):
        if (keyPressed == K_LEFT and self.x <= 0) or (keyPressed == K_RIGHT and (self.x + paddle.get_width()) >= WIDTH):
            return
        if keyPressed == K_LEFT:
            self.x -= self.speed
        if keyPressed == K_RIGHT:
            self.x += self.speed

    def followBall(self, ball : Ball):
        # print(ball.x)
        # print(ball.x - paddle.get_width() // 2)
        if ball.x - paddle.get_width() // 2 <= 0 or ball.x + paddle.get_width() // 2 >= WIDTH:
            return
        if ball.x - paddle.get_width() // 2 > self.x:
            self.x += 0.1
        else:
            self.x -= 0.1
        # self.x = ball.x - (paddle.get_width() // 2) - self.speed
    def isLose(self):
        halfball = BALL_SIZE // 2
        if (self.ball.x < self.x - halfball) or (self.ball.x > (self.x + paddle.get_width() + halfball)):
            self.ball.reset()
            self.score += 1
            return True
        return False
