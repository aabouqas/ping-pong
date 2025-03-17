from Utils import W_BOTTOM, W_RIGHT, BALL_SIZE

class Ball:
    x = 0
    y = 0
    speed = 1
    directionX = 0
    directionY = 1
    def __init__(self, x, y, speed = 0):
        self.x = x
        self.y = y
    def moveForward(self):
        self.x += self.directionX
        self.y += self.directionY
        if self.y >= W_BOTTOM or self.y < BALL_SIZE:
            self.directionY *= -1

        if self.x >= W_RIGHT or self.x <= BALL_SIZE:
            self.directionX *= -1

        if self.y == W_BOTTOM and self.directionX == 0:
            self.directionX = 1
    def getCourdinates(self):
        return [self.x, self.y]