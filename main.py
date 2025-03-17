import pygame
from pygame import *
from Player import Player
from Ball import Ball
from Utils import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING PONG")

running = True

colors = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('pink'), pygame.Color('yellow')]
i = 0

ball = Ball(WIDTH / 2, HEIGHT / 2)

player1 = Player(WIDTH // 2 - (PADDLE_WIDTH // 2), HEIGHT - (PADDLE_HEIGHT // 2))
player2 = Player(WIDTH // 2 - (PADDLE_WIDTH // 2), -15)



while running:
    screen.fill(Color("black"))
    if i % ball.speed == 0:
        ball.moveForward()

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
            player1.move(keyPressed)

    pygame.display.flip()
    i += 1
    if i == 1000:
        i = 0

print("End")
pygame.quit()