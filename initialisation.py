__author__ = 'shubham singh'
import pygame

pygame.init()

pygame.display.set_mode((300,300))
pygame.display.set_caption("My first window")

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if(event.type ==pygame.QUIT):
            gameExit=True
pygame.quit()
exit()