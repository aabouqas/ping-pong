import pygame.mixer
WIDTH = 620
HEIGHT = 720

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10

LEFT = 1
RIGHT = 2
BALL_SIZE = 40
playerMovmentSpeed = 0

key_hold = True
keyPressed = 0

gravity = 0.1

OFFSET = 15
W_BOTTOM = HEIGHT
W_RIGHT = WIDTH - BALL_SIZE

play = True

pygame.mixer.init()
paddle_sound = pygame.mixer.Sound("audio/pingpongbat.wav")
paddle_sound_wall = pygame.mixer.Sound("audio/pingpongboard.wav")

paddle = pygame.image.load("res/fancy-paddle-grey.png")

paddle = pygame.transform.rotate(paddle, 90)

ball = pygame.image.load("res/Ball.png")

ball = pygame.transform.scale(ball, (BALL_SIZE, BALL_SIZE))

background = pygame.image.load("res/space1.png")