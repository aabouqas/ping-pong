import Player
from Utils import W_BOTTOM, W_RIGHT, BALL_SIZE, PADDLE_WIDTH, OFFSET, PADDLE_HEIGHT, HEIGHT, WIDTH


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

        if self.y >= W_BOTTOM - OFFSET - BALL_SIZE and player.x < self.x < (player.x + PADDLE_WIDTH):
            self.directionY *= -1
        elif self.y == W_BOTTOM or self.y < BALL_SIZE + OFFSET:
            self.directionY *= -1
        # if self.y >= W_BOTTOM - BALL_SIZE - OFFSET or self.y < BALL_SIZE + OFFSET:
        #     self.directionY *= -1

        if self.x >= W_RIGHT or self.x <= BALL_SIZE:
            self.directionX *= -1
        # if self.y == W_BOTTOM  and self.directionX == 0:
        #     self.directionX = 1
    def getCourdinates(self):
        return [self.x, self.y]
    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 0.5
