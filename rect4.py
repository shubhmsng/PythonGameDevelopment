__author__ = 'shubham singh'
import pygame
from time import sleep
pygame.init()
gameDisplay = pygame.display.set_mode((1000,700))
pygame.display.set_caption("moving rect3")
RED = (250, 30, 0)
GREEN = (0, 250, 50)

clock = pygame.time.Clock()
lead_x = 10
lead_y = 10
lead_change_x = 0
lead_change_y = 0
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_change_x -= 5
                lead_change_y = 0
            if event.key == pygame.K_RIGHT:
                lead_change_x += 5
                lead_change_y = 0
            if event.key == pygame.K_UP:
                lead_change_y -= 5
                lead_change_x = 0
            if event.key == pygame.K_DOWN:
                lead_change_y += 5
                lead_change_x = 0
    if lead_x >=0 and lead_x <=980:
        lead_x += lead_change_x
    else:
        gameExit = True
    if lead_y >=0 and lead_y <=680:
        lead_y += lead_change_y
    else:
        gameExit = True
    if lead_x == 0:
        gameExit = True
    if lead_y == 0:
        gameExit = True
    gameDisplay.fill(GREEN)
    pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20,20))
    clock.tick(30)
    pygame.display.update()
soundObj4 = pygame.mixer.Sound('match2.wav')
soundObj4.play()
sleep(.5)
pygame.quit()
quit()