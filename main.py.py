import pygame
from random import randint
from os import system

system('cls')

pygame.init()

win = pygame.display.set_mode((600, 500))
hold = True

platform = pygame.image.load("platform_1.png")
def draw_platform():
    win.blit(platform, (1,20))


#--------------------------#--------------------------#--------------------------#--------------------------#
while hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hold = False

    win.fill((0, 0, 0))
    draw_platform()

    #--------------------------#--------------------------#--------------------------#--------------------------#
    pygame.display.update()