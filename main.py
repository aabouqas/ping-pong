import pygame
from pygame import *

import Utils
from Player import Player
from Ball import Ball
from Utils import *

pygame.init()

pygame.display.set_caption("Ping Pong")
icon = pygame.image.load("res/icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

colors = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('pink'), pygame.Color('yellow')]

ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2)

player1 = Player(WIDTH // 2 - (paddle.get_width() // 2), HEIGHT, ball)
player2 = Player(WIDTH // 2 - (paddle.get_width() // 2), 0, ball)

FONTSIZE = 40


def putTextToWindow(text: str, x, y):
    font_ = pygame.font.Font(None, FONTSIZE)
    text_surface = font_.render(text, True, pygame.Color("white"))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

clock = pygame.time.Clock()
i = 0
while running:
    if not Utils.play:
        # screen.fill(background)
        # screen.fill(Color("black"))
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                running = False
                break
            elif envent.type == pygame.KEYDOWN:
                keyPressed = envent.key
                if envent.key == pygame.K_ESCAPE:
                    running = False
                elif envent.key == pygame.K_SPACE:
                    Utils.play = True
        pygame.display.set_caption(f"P1: {int(player2.score)} -  P2: {int(player1.score)}")
        putTextToWindow("Press space to continue", WIDTH // 2, (HEIGHT // 2) + 46)
        pygame.display.set_caption("Ping Pong")
        pygame.display.flip()
        continue
    screen.fill(Color("black"))
    pygame.display.set_caption(f"P1: {int(player2.score)} -  P2: {int(player1.score)}")
    if ball.y < HEIGHT // 2:
        ball.moveForward(player2)
    else:
        ball.moveForward(player1)
    # ball.moveForward(player2)

    # print (ball.y >= W_BOTTOM - OFFSET - BALL_SIZE)

    if ball.y == 0:
        if player2.isLose():
            Utils.play = False

    if ball.y == W_BOTTOM - BALL_SIZE - paddle.get_height():
        if player1.isLose():
            Utils.play = False

        if player1.x < (ball.x + BALL_SIZE) < (player1.x + paddle.get_width()):
            relative_impact = ((ball.x - player1.x) / paddle.get_width()) * 2 - 1
            ball.directionX = relative_impact


    # pygame.draw.circle(screen, pygame.Color("red"), ball.getCourdinates(), BALL_SIZE)
    # pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(player1.x, player1.y, paddle_get_width(, PADDLE_HEIGHT))
    # pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(player2.x, player2.y, paddle_get_width(, PADDLE_HEIGHT))
    screen.blit(Utils.ball, ball.getCourdinates())
    screen.blit(paddle, (player1.x, player1.y - paddle.get_height() // 2))
    screen.blit(paddle, (player2.x, player2.y))
    # print(player1.x)

    # - paddle.get_height())
    # + paddle.get_height())

    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            running = False
            break
        elif envent.type == pygame.KEYDOWN:
            key_hold = True
            Utils.keyPressed = envent.key
            if envent.key == pygame.K_ESCAPE:
                running = False
        elif envent.type == pygame.KEYUP:
            key_hold = False

    if key_hold:
        if Utils.keyPressed == K_RIGHT or Utils.keyPressed == K_LEFT:
            player1.move(Utils.keyPressed)
    player2.followBall(ball)
    pygame.display.flip()
    # clock.tick(90)
    i += 0.5

pygame.quit()