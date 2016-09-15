__author__ = 'shubham singh'
import pygame
from time import sleep
import random
pygame.init()
gameDisplay = pygame.display.set_mode((1000,700))
pygame.display.set_caption("snake and apple")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
RED = (250, 30, 0)
GREEN = (0, 250, 50)
BLUE = (10, 30, 200)
BLACK = (0, 0, 0)
SKY = (0, 150, 250)
gameScore = 0
speed = 50
font = pygame.font.SysFont("comicsansms", 72)
def message_to_screen(msg, color, place, place1):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (4*place, 100*place1))

def snake(snakelist, block_size):
    for xny in snakelist:
        pygame.draw.rect(gameDisplay, BLUE, (xny[0], xny[1], block_size, block_size))

apple = pygame.image.load("squirrel.png")
gameDisplay.fill(GREEN)
message_to_screen("This game is Developed ",BLACK, 2, 1)
message_to_screen("By Shubham Singh",BLACK, 2, 2)
message_to_screen("CSE(4th Sem) Student",BLACK, 2, 3)
message_to_screen("At IERT Allahabad",BLACK, 2, 4)
pygame.display.update()
sleep(5)
gameOver = False
while not gameOver:
    clock = pygame.time.Clock()
    lead_x = 500
    lead_y = 350
    lead_change_x = 0
    lead_change_y = 0
    i = False
    l = False
    speed += 20

    snakelist = []
    snakelen = 20
    rand_x = random.randrange(0, 500-30)
    rand_y = random.randrange(0, 350-30)
    gameExit = False
    gameScore_gain = 4000
    while not gameExit:
        gameScore_gain -= 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
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
        if lead_x >=0 and lead_x <= 980:
            lead_x += lead_change_x
        else:
            gameExit = True
            i = True
            l = True
            gameScore = 0
        if lead_y >=0 and lead_y <=680:
            lead_y += lead_change_y
        else:
            gameExit = True
            i = True
            l = True
            gameScore = 0
        if lead_x == 0:
            gameExit = True
            i = True
            l = True
            gameScore = 0
        if lead_y == 0:
            gameExit = True
            i = True
            l = True
            gameScore = 0

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelen:
            del snakelist[0]

        gameDisplay.fill(GREEN)
        gameDisplay.blit(apple, (rand_x, rand_y))
        snake(snakelist, 15)

        if lead_x > rand_x and lead_y > rand_y :
            if lead_x-rand_x < 15 and lead_y-rand_y < 15 :
                gameExit = True
                gameScore += gameScore+gameScore_gain
                soundObj4 = pygame.mixer.Sound('match20.wav')
                soundObj4.play()
                pygame.display.update()
                gameDisplay.fill(GREEN)
                score = pygame.image.load('Score.png')
                message_to_screen("WELCOME to Next Level",SKY , 10, 1)
                gameDisplay.blit(score, (100,200))
                message_to_screen(str(gameScore),RED, 100, 2.5)
                pygame.display.update()
                sleep(2)

        if rand_x > lead_x and rand_y > lead_y :
            if rand_x-lead_x < 35 and rand_y-lead_y < 35:
                gameExit = True
                gameScore += gameScore+gameScore_gain
                soundObj4 = pygame.mixer.Sound('match20.wav')
                soundObj4.play()
                pygame.display.update()
                gameDisplay.fill(GREEN)
                message_to_screen(("Welcome to Next Level"),SKY, 10, 1)
                score = pygame.image.load('Score.png')
                gameDisplay.blit(score, (100,200))
                message_to_screen(str(gameScore),RED, 100, 2.5)
                pygame.display.update()
                sleep(2)

        clock.tick(speed)
        pygame.display.update()

    if i:
        soundObj4 = pygame.mixer.Sound('match21.wav')
        soundObj4.play()
        speed = 50
        gameDisplay.fill(GREEN)
        looser = pygame.image.load('looser.jpg')
        gameDisplay.blit(looser, (300,200))
        pygame.display.update()
        sleep(1)
    if speed >=150:
        gameDisplay.fill(GREEN)
        winner = pygame.image.load('winner.jpg')
        score = pygame.image.load('Score.png')
        gameDisplay.blit(score, (100,50))
        message_to_screen(str(gameScore),RED, 100, 1)
        gameDisplay.blit(winner, (300,200))
        message_to_screen("PRESS q to Quit", RED, 2, 4)
        pygame.display.update()
        for i in range (2):
            soundObj4 = pygame.mixer.Sound('match20.wav')
            soundObj4.play()
            sleep(1)
        pygame.display.update()
    if l:
        gameDisplay.fill(GREEN)
        ins = pygame.image.load('quit.jpg')
        gameDisplay.blit(ins, (300,200))
        pygame.display.update()
        sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameOver = True

pygame.quit()
quit()
