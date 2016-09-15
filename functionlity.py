__author__ = 'shubham singh'
import pygame,sys
from time import sleep
import random
pygame.init()
gameDisplay = pygame.display.set_mode((1000,700))
pygame.display.set_caption("moving rect3")
RED = (250, 30, 0)
GREEN = (0, 250, 50)
BLUE = (10, 30, 200)

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (500,350))

gameOver = False
while not gameOver:
    clock = pygame.time.Clock()
    lead_x = 500
    lead_y = 350
    lead_change_x = 0
    lead_change_y = 0
    rand_x = random.randrange(0, 500-30)
    rand_y = random.randrange(0, 350-30)
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
        pygame.draw.rect(gameDisplay,BLUE,(rand_x, rand_y, 20, 20))
        pygame.draw.rect(gameDisplay, RED, (lead_x, lead_y, 20, 20))
        clock.tick(100)
        pygame.display.update()

    soundObj4 = pygame.mixer.Sound('match2.wav')
    soundObj4.play()
    message_to_screen("You lose", BLUE)
    pygame.display.update()
    sleep(1)
    gameDisplay.fill(GREEN)
    message_to_screen("PRESS c to Play again or Q to QUIT or wait 3 sec.", BLUE)
    pygame.display.update()
    sleep(3)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                gameOver = False
            else:
                gameOver = True

pygame.quit()
quit()
