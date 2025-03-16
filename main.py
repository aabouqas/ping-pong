#!.venv/bin/python3
import random

import pygame
from pygame import *

pygame.init

WIDTH = 620
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING PONG")

running = True

colors = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('pink'), pygame.Color('yellow')]
# WIDTH / 2, HEIGHT - 11
i = 0



PADDLE_WIDTH = 100
PADDLE_HEIGHT = 25
# player = [[WIDTH / 2, HEIGHT], [WIDTH / 2, HEIGHT - 10], ]


LEFT = 1
RIGHT = 2
BALL_SIZE = 20
playerMovmentSpeed = 0.5

class Player:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getCourdinates(self):
        return [self.x, self.y]
    def move(self):
        if (keyPressed == K_LEFT and player1.x == 0) or (keyPressed == K_RIGHT and (player1.x + PADDLE_WIDTH) == WIDTH):
            return
        if keyPressed == K_LEFT:
            self.x -= playerMovmentSpeed
        if keyPressed == K_RIGHT:
            self.x += playerMovmentSpeed
class Ball:
    x = 0
    y = 0
    speed = 1
    directionX = 0
    directionY = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def increace(self):
        self.x += self.directionX
        self.y += self.directionY
    def getCourdinates(self):
        return [self.x, self.y]

player1 = Player(WIDTH // 2 - (PADDLE_WIDTH // 2), HEIGHT - (PADDLE_HEIGHT // 2))
# player2 = Player(WIDTH // 2 - (PADDLE_WIDTH // 2), -15)
ball = Ball(WIDTH / 2, HEIGHT / 2)

def movePlayer():
    if (keyPressed == K_LEFT and player1.x == 0) or (keyPressed == K_RIGHT and (player1.x + PADDLE_WIDTH) == WIDTH):
        return
    if keyPressed == K_LEFT:
        player1.x -= playerMovmentSpeed
    if keyPressed == K_RIGHT:
        player1.x += playerMovmentSpeed

key_hold = True
keyPressed = 0

gravity = 0.1

W_BOTTOM = HEIGHT - PADDLE_HEIGHT
W_RIGHT = WIDTH - BALL_SIZE

while running:
    screen.fill(Color("black"))
    if i % ball.speed == 0:

        ball.increace()

        if ball.y >= W_BOTTOM or ball.y < BALL_SIZE:
            ball.directionY *= -1

        if ball.x >= W_RIGHT or ball.x <= BALL_SIZE:
            ball.directionX *= -1

        if ball.y == W_BOTTOM and ball.directionX == 0:
            ball.directionX = 1

    if ball.y == W_BOTTOM:
        if ball.x < player1.x:
            running = False
        if  ball.x > player1.x + 100:
            running = False

        if player1.x < ball.x < (player1.x + PADDLE_WIDTH):
            relative_impact = ((ball.x - player1.x) / PADDLE_WIDTH) * 2 - 1
            ball.directionX = relative_impact
        ball.directionY *= -1
        ball.speed -= 1
    else:
        ball.speed = 2

    pygame.draw.circle(screen, pygame.Color("red"), ball.getCourdinates(), BALL_SIZE)
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(player1.x, player1.y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(player2.x, player2.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            running = False
            break
        elif envent.type == pygame.KEYDOWN:
            key_hold = True
            keyPressed = envent.key
            if envent.key == pygame.K_ESCAPE:
                running = False
        elif envent.type == pygame.KEYUP:
            key_hold = False

    if key_hold:
        if keyPressed == K_RIGHT or keyPressed == K_LEFT:
            player1.move()

    pygame.display.flip()
    i += 1
    if i == 1000:
        i = 0

print("End")
pygame.quit()