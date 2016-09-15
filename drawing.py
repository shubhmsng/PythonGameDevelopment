__author__ = 'shubham singh'
import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Drawing")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 250, 250)

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(BLUE)
    pygame.draw.polygon(gameDisplay, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    pygame.draw.rect(gameDisplay, WHITE, [100, 100, 100, 100])
    pygame.draw.circle(gameDisplay, RED, [300, 100], 70, 70)
    pygame.draw.line(gameDisplay, BLACK, (60, 120), (120, 120), 4)
    pygame.draw.ellipse(gameDisplay, RED, (360, 150, 80, 60), 4)
    pygame.display.update()

pygame.quit()
exit()