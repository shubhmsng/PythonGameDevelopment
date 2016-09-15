__author__ = 'shubham singh'
import pygame
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
    if lead_x >=0 and lead_x <=950:
        lead_x += lead_change_x
    else:
        lead_x = 10
    if lead_y >=0 and lead_y <=650:
        lead_y += lead_change_y
    else:
        lead_y = 10
    if lead_x == 0:
        lead_x = 950
    if lead_y == 0:
        lead_change_y == 5
    gameDisplay.fill(GREEN)
    pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 50,5))
    clock.tick(30)
    pygame.display.update()
pygame.quit()
quit()