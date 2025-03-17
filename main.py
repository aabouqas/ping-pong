import pygame
from pygame import *
from Player import Player
from Ball import Ball
from Utils import *

pygame.init()

pygame.display.set_caption("Ping Pong")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

colors = [pygame.Color('red'), pygame.Color('blue'), pygame.Color('pink'), pygame.Color('yellow')]
i = 0

ball = Ball(WIDTH / 2, HEIGHT / 2)

player1 = Player(WIDTH // 2 - (PADDLE_WIDTH // 2), HEIGHT - PADDLE_HEIGHT)
player2 = Player(WIDTH // 2 - (PADDLE_WIDTH // 2), 0)

FONTSIZE = 40


def putTextToWindow(text: str, x, y):
    font_ = pygame.font.Font(None, FONTSIZE)
    text_surface = font_.render(text, True, pygame.Color("white"))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

play = True
scoore = 0

while running:
    if not play:
        screen.fill(Color("black"))
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                running = False
                break
            elif envent.type == pygame.KEYDOWN:
                keyPressed = envent.key
                if envent.key == pygame.K_ESCAPE:
                    running = False
                elif envent.key == pygame.K_SPACE:
                    play = True
        putTextToWindow(f"Max score : {scoore} / {player1.score}", WIDTH // 2, HEIGHT // 2)
        putTextToWindow("Press space to continue", WIDTH // 2, (HEIGHT // 2) + 46)
        pygame.display.set_caption("Ping Pong")
        pygame.display.flip()
        continue
    screen.fill(Color("black"))
    pygame.display.set_caption(f"Max score : {scoore} /  {player1.score}")
    if i % ball.speed == 0:
        ball.moveForward(player1)

    if ball.y == W_BOTTOM - OFFSET - BALL_SIZE:
        if (ball.x < player1.x - BALL_SIZE) or (ball.x > player1.x + PADDLE_WIDTH + BALL_SIZE):
            scoore = 0
            ball.reset()
            player1.increaseScore(scoore)
            play = False
            # running = False
        # if  ball.x > player1.x + PADDLE_WIDTH + BALL_SIZE:
        #     player2.score += 1

            # running = False

        if player1.x < ball.x < (player1.x + PADDLE_WIDTH):
            relative_impact = ((ball.x - player1.x) / PADDLE_WIDTH) * 2 - 1
            ball.directionX = relative_impact
            scoore += 1
            print (scoore)
        ball.directionY *= -1
        # ball.speed -= 1
    else:
        ball.speed = 1

    pygame.draw.circle(screen, pygame.Color("red"), ball.getCourdinates(), BALL_SIZE)
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(player1.x, player1.y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(player2.x, player2.y, PADDLE_WIDTH, PADDLE_HEIGHT))

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
    player2.followBall(ball)
    pygame.display.flip()
    i += 1
    if i == 1000:
        i = 0

pygame.quit()