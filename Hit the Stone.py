__author__ = 'shubham singh'
import pygame
from time import sleep
pygame.init()

gammeDisplay = pygame.display.set_mode((600,600))
pygame.display.set_caption("Hit The Stone")
icon = pygame.image.load("gem2.png")
pygame.display.set_icon(icon)

RED = (250,0,0)
BLACK = (0,0,0)
BLUE = (0,120,250)
GREEN = (0,200,100)
stone_pos_x = 0
tank_pos_x = 250
fire_pos_y = 530
stone = pygame.image.load("Rock.png")
tank = pygame.image.load("tank.png")
fire = pygame.image.load("fire.png")
font = pygame.font.SysFont("comicsansms", 28)

def score_update(score):
    text = font.render("Score: "+str(score), True, BLACK )
    gammeDisplay.blit(text, (380, 380))

def time_update(time):
    text = font.render("Time Remaining:"+str(time), True, RED)
    gammeDisplay.blit(text, (280, 480))

def high_score(score):
    text = font.render("Your Score: "+str(score), True, BLUE)
    gammeDisplay.blit(text, (200, 250))

gameOver = False
while not gameOver:
    gameExit = True
    i = False
    fire_pos_x = 0
    score = 0
    time = 500
    speed =20
    m = 0
    level = 1

    while gameExit:
        gammeDisplay.fill(GREEN)
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False
                gameOver = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if tank_pos_x <550 and tank_pos_x > 0 :
                        tank_pos_x += 10
                if event.key == pygame.K_LEFT:
                    if tank_pos_x < 550 and tank_pos_x > 0 :
                        tank_pos_x -= 10
                if event.key == pygame.K_UP:
                    i = True
                    soundObj4 = pygame.mixer.Sound('match0.wav')
                    soundObj4.play()
                    fire_pos_x = tank_pos_x
                    m = event.key
        stone_pos_x += 5

        if stone_pos_x > 590:
            stone_pos_x = 0
        if i and fire_pos_y > 0:
            fire_pos_y -= 10
            gammeDisplay.blit(fire, (fire_pos_x-10, fire_pos_y-10))
        else:
            i = False
            fire_pos_y = 530
        fire_x = fire_pos_x-10
        fire_y = fire_pos_y-10
        if fire_x > stone_pos_x:
            if fire_x-stone_pos_x < 30 and fire_y < 25:
                score += 10
                stone_pos_x = 0
                time += 100
                if speed < 180:
                    speed += 10
                    level +=1
                soundObj4 = pygame.mixer.Sound('match1.wav')
                soundObj4.play()
        elif fire_x < stone_pos_x:
            if stone_pos_x-fire_x < 30 and fire_y < 25:
                score += 10
                stone_pos_x = 0
                time += 500
                if speed < 180:
                    speed += 10
                    level += 1
                soundObj4 = pygame.mixer.Sound('match1.wav')
                soundObj4.play()
        else:
            time -= 5

        score_update(score)
        time_update(time)
        txt = font.render("Level:"+str(level),True, BLUE )
        gammeDisplay.blit(txt, (380, 430))
        gammeDisplay.blit(stone, (stone_pos_x, 10))
        gammeDisplay.blit(tank, (tank_pos_x, 550))
        pygame.display.update()
        clock.tick(speed)
        time -= 1
        m =0
        if time == 0:
            gameExit = False
            gammeDisplay.fill(GREEN)
            high_score(score)
            soundObj4 = pygame.mixer.Sound('match20.wav')
            soundObj4.play()
            pygame.display.update()
            sleep(3)
            gammeDisplay.fill(GREEN)
            img = pygame.image.load("quit.jpg")
            gammeDisplay.blit(img, (150, 150))
            pygame.display.update()
            sleep(2)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        pygame.quit()
                    else:
                        gameOver = False
pygame.quit()
quit()