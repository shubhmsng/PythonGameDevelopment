__author__ = 'shubham singh'
import pygame
import sys
pygame.init()
pygame.display.set_mode((400,400))
pygame.display.set_caption("My second window")
gameExit=False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if(event.type == pygame.QUIT):
            gameExit=True

pygame.quit()
exit()