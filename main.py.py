import pygame
from random import randint
from os import system

system('cls')

pygame.init()

win = pygame.display.set_mode((600, 500))
hold = True

#--------------platform-----------------------#
platform = pygame.image.load("background.png")
def draw_platform():
    win.blit(platform, (0,0))

#---------------imposter---------------------#
ball = pygame.image.load("ball_1.png")
def draw_ball():
    win.blit(ball, (300,250))


#--------------------------#--------------------------#--------------------------#--------------------------#
while hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hold = False

    win.fill((0, 0, 0))
    draw_platform()
    draw_ball()

    #--------------------------#--------------------------#--------------------------#--------------------------#
    pygame.display.update()