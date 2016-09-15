__author__ = 'shubham singh'
import pygame
from time import sleep

GREEN =(0, 250, 100)
RED = (250, 30, 0)
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Moving Rect")

gameExit = False
lead_x = 5
lead_y = 5
clock = pygame.time.Clock()
while not gameExit:
    for event in pygame.event.get():
        gameDisplay.fill(GREEN)
        pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20, 20))
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                while lead_x >= 10:
                    lead_x -= 10
                    gameDisplay.fill(GREEN)
                    pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20, 20))
                    pygame.display.update()
                    clock.tick(30)
                    soundObj = pygame.mixer.Sound('match3.wav')
                    soundObj.play()
            if event.key == pygame.K_RIGHT:
                while lead_x <= 760:
                    lead_x += 10
                    gameDisplay.fill(GREEN)
                    pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20, 20))
                    pygame.display.update()
                    clock.tick(30)
                    soundObj = pygame.mixer.Sound('match2.wav')
                    soundObj.play()
            if event.key == pygame.K_UP:
                while lead_y >= 10:
                    lead_y -= 10
                    gameDisplay.fill(GREEN)
                    pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20, 20))
                    pygame.display.update()
                    clock.tick(30)
                    soundObj = pygame.mixer.Sound('match1.wav')
                    soundObj.play()
            if event.key == pygame.K_DOWN:
                while lead_y <= 580:
                    lead_y += 10
                    gameDisplay.fill(GREEN)
                    pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20, 20))
                    pygame.display.update()
                    clock.tick(30)
                    soundObj = pygame.mixer.Sound('match0.wav')
                    soundObj.play()
        if event.type == pygame.QUIT:
            gameExit = True
pygame.quit()
quit()