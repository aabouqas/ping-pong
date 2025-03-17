from pygame import K_LEFT, K_RIGHT
from Utils import *
class Player:
    x = 0
    y = 0
    speed = 0
    def __init__(self, x, y, speed = 2):
        self.x = x
        self.y = y
        self.speed = speed
    def getCourdinates(self):
        return [self.x, self.y]
    def move(self, keyPressed):
        if (keyPressed == K_LEFT and self.x == 0) or (keyPressed == K_RIGHT and (self.x + PADDLE_WIDTH) == WIDTH):
            return
        if keyPressed == K_LEFT:
            self.x -= self.speed
        if keyPressed == K_RIGHT:
            self.x += self.speed