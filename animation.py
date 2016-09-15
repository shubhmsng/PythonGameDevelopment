__author__ = 'shubham singh'
import pygame,sys
from time import *
pygame.init()

BLUE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((600, 600))


catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'
pygame.display.update()
gameExit = False
while not gameExit:
    DISPLAYSURF.fill(BLUE)
    if direction == 'right':
        catx += 5
        if catx == 480:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 480:
             direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.display.update()
    sleep(.05)

pygame.quit()
exit()