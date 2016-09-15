__author__ = 'shubham singh'
#IMPORT FILES
import pygame
import random
from time import sleep

#PYGAME INITIALISATION
pygame.init()
display = pygame.display.set_mode((900, 600))  #SET SIZE OF SCREEN
pygame.display.set_caption("TANK")                   #SET TITLE OF GAME
#colors            R    G   B
RED             = (252, 23,  12)
BROWN           = (117,  0,   0)
LIGHT_RED       = (255, 117, 124)
GREEN           = (0,   255,  0)
LIGHT_GREEN     = (113, 255,113)
BLUE            = (0,   0,  255)
LIGHT_BLUE      = (70, 102, 255)
SKY_BLUE        = (73, 239, 243)
BLACK           = (0, 0, 0)
WHITE           = (255, 255, 255)
LIGHT_BLACK     = (143, 143, 143)
PINK            = (255, 0, 255)
NAVYBLUE        = ( 60, 60, 100)
YELLOW          = (255, 255, 0)
ORANGE          = (255, 128, 0)
CYAN            = ( 0, 255, 255)
#clock speed(Frame Per Second)
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 28)
img = pygame.image.load("fire2.png")

def draw_tank(tank_x, lead_x, lead_y):
    imag = pygame.image.load("tank2.png")
    display.blit(imag, (tank_x, 520))
    pygame.draw.line(display, BLACK, (tank_x + 20, 528),(tank_x+lead_x-5, 520+lead_y), 5)

def barrier(rand_x, rand_y):
    pygame.draw.rect(display, BROWN, (rand_x, rand_y, 50, 500))

def ground():
    pygame.draw.rect(display, GREEN, (0, 550, 900, 50))

def fire (x, y, angle, rand_x, rand_y, stone_x, stone_y):
    Fire = True
    diff_x = 0
    diff_y = 0
    score = 0
    x1 = x
    while Fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(img,(x-10,y-10))
        pygame.display.update()
        sleep(.03)
        x -= (12 - angle)*2
        y += int((((x - x1)*0.015)**2)-2*(angle+angle/(9-angle)))
        if y > 550:
            Fire = False
        if y > rand_y and x >= rand_x  and x <= rand_x+50:
            Fire = False
    if stone_x <= x:
        diff_x = x - stone_x
    if x < stone_x:
        diff_x = stone_x - x
    if stone_y <= y:
        diff_y = y- stone_y
    if stone_y > y:
        diff_y = stone_y - y
    if diff_y <= 45 and diff_x <=45:
        score = 50
    elif diff_x <= 50 and diff_y <= 50:
        score = 30
    elif diff_x <= 70 and diff_y <= 70:
        score = 20
    elif diff_x <=90 and diff_y <=90:
        score = 10
    print (score)
    return score
def stone(rand_x):
    rand_y = 500
    stone = pygame.image.load("Rock.png")
    display.blit(stone, (rand_x, rand_y))
    pygame.display.update()

def score_update(score):
    text = font.render("Score: "+str(score),True, BLUE)
    display.blit(text, (500, 10))

def loop():
    tannk1_x = 800
    ln_x = 0
    ln_y = 0
    level = 0
    angle = 0
    score = 0
    Gexit = True
    rand_x = random.randint(250, 600)
    rand_y = random.randint( 250,400)
    randstone_x = random.randint(50, rand_x-150)
    while Gexit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Gexit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if tannk1_x < 850:
                        lead1 = 10
                        tannk1_x += lead1

                elif event.key == pygame.K_LEFT:
                    if tannk1_x > rand_x+50:
                        lead1 = 10
                        tannk1_x -= lead1

                elif event.key == pygame.K_UP:
                    if ln_x <18 and tannk1_x <= 880 and tannk1_x > rand_x+50:
                        ln_x += 3
                        ln_y -= 3
                    if angle <=7:
                        angle +=1
                elif event.key == pygame.K_DOWN:
                    if ln_x > 0 and tannk1_x <= 880 and tannk1_x > rand_x+50:
                        ln_x -= 3
                        ln_y += 3
                    if angle >=1:
                        angle -= 1
                elif event.key == pygame.K_SPACE:
                    score += fire(tannk1_x+ln_x-5, 520+ln_y, angle, rand_x, rand_y, randstone_x, 500)
                    rand_x = random.randint(250, 600)
                    rand_y = random.randint( 250,400)
                    randstone_x = random.randint(50, rand_x - 200)


        display.fill(SKY_BLUE)
        draw_tank(tannk1_x, ln_x, ln_y)
        barrier(rand_x, rand_y)
        ground()
        score_update(score)
        stone(randstone_x)
        pygame.display.update()
        clock.tick(60)

def main():
    loop()
    pygame.quit()
    quit()
main()