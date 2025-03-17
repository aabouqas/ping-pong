from pygame import K_LEFT, K_RIGHT

from Ball import Ball
from Utils import *
class Player:
    x = 0
    y = 0
    speed: float = 0
    score = 0
    def __init__(self, x, y, speed = 1):
        self.x = x
        if y == 0:
            self.y = OFFSET
        else:
            self.y = y - OFFSET
        self.speed = speed
    def getCourdinates(self):
        return [self.x, self.y]
    def move(self, keyPressed):
        if (keyPressed == K_LEFT and self.x <= 0) or (keyPressed == K_RIGHT and (self.x + PADDLE_WIDTH) >= WIDTH):
            return
        if keyPressed == K_LEFT:
            self.x -= self.speed
        if keyPressed == K_RIGHT:
            self.x += self.speed

    def followBall(self, ball : Ball):
        # print(ball.x)
        if ball.x - PADDLE_WIDTH // 2 <= 0 or ball.x + PADDLE_WIDTH // 2 >= WIDTH:
            return
        self.x = ball.x - (PADDLE_WIDTH // 2) - self.speed