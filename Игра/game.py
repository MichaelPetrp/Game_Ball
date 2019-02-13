import pygame
import random
import time

pygame.init()
win = pygame.display.set_mode((400, 500))

pygame.display.set_caption('Ball')

WHITE = pygame.Color('white')  # Color of wall
ball = pygame.image.load('ball.png')
rock = pygame.image.load('rock.png')
GameOver = pygame.image.load('GameOver.jpg')
fone = pygame.image.load('fone.jpg')
music = pygame.mixer.Sound("music_2.wav")

RUN = True
x = 250
speed = 10
win.fill(WHITE)
rock_y = 0
count = 1
rock_x, rock_x2 = random.randint(0, 386), random.randint(0, 386)
fone_y = -500
ball_y = 250
music.play()
while RUN:
    pygame.time.delay(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x - speed >= -10:
            x -= speed
    elif keys[pygame.K_RIGHT]:
        if x + speed <= 330:
            x += speed

    if fone_y != 0:
        if int(count) == 0:
            fone_y += 1
            count = 1
        else:
            count -= 0.2
    else:
        ball_y -= speed

    win.blit(fone, (0, fone_y))

    if rock_y <= 500:
        win.blit(rock, (rock_x, rock_y))
        win.blit(rock, (rock_x2, rock_y))
        rock_y += 20
    else:
        rock_x, rock_x2 = random.randint(0, 386), random.randint(0, 386)
        rock_y = 0

    win.blit(ball, (x, ball_y))

    if 330 >= rock_y >= 250 and x <= rock_x <= x + 80:
        win.blit(GameOver, (0, 0))
        RUN = False
    elif 330 >= rock_y >= 250 and x <= rock_x2 <= x + 80:
        win.blit(GameOver, (0, 0))
        RUN = False

    pygame.display.flip()
time.sleep(3)
pygame.quit()
