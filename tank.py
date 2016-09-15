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


def fire (x, y, angle, rand_x, rand_y):
    Fire = True
    i=0

    while Fire:
        display.blit(img,(x-10,y-10))
        pygame.display.update()
        sleep(.03)
        if angle ==0:
            x -= 2*i
            y -= i
        elif angle ==15:
            x -= 2*i
            y -= int(1.5*i)
        elif angle ==30:
            x -= 2*i
            y -= 2*i
        elif angle == 45:
            x -= 2*i
            y -=int(2.5*i)
        elif angle == 60:
            x -=int(1.5*i)
            y -= 3*i
        elif angle == 75:
            x -= int(.5*i)
            y -= int(1.25*i)
        elif angle == 90:
            x -= int (1.15*i)
            y -= int(2.75*i)
        if  x <= rand_x+50:
            Fire = False
        i +=1

    if y < rand_y:
        i=1
        x = x-20
        Fire1 =True
        while Fire1:
            display.blit(img,(x-5,y-5))
            pygame.display.update()
            sleep(.05)
            if angle == 0:
                x -= int(1.5*i)
                y += 2*i
            else:
                x -= int(.5*i)
                y += int(1.25*i)
            if y >=550:
                Fire1 = False
            i +=2

def stone(rand_x):
    rand_y = 500
    stone = pygame.image.load("Rock.png")
    display.blit(stone, (rand_x, rand_y))
    pygame.display.update()

def loop():
    tannk1_x = 800
    ln_x = 0
    ln_y = 0
    level = 0
    angle = 0
    Gexit = True
    rand_x = random.randint(250, 600)
    rand_y = random.randint( 150,400)
    randstone_x = random.randint(50, rand_x-100)
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
                    if angle <=75:
                        angle +=15
                elif event.key == pygame.K_DOWN:
                    if ln_x > 0 and tannk1_x <= 880 and tannk1_x > rand_x+50:
                        ln_x -= 3
                        ln_y += 3
                    if angle >=15:
                        angle -= 15
                elif event.key == pygame.K_SPACE:
                    fire(tannk1_x+ln_x-5, 520+ln_y, angle, rand_x, rand_y)
                    randstone_x = random.randint(50, rand_x - 100)
                elif event.key == pygame.K_w:
                    if level <= 95:
                        level += 5
                elif event.key == pygame.K_s:
                    if level >=5:
                        level -= 5


        display.fill(SKY_BLUE)
        draw_tank(tannk1_x, ln_x, ln_y)
        barrier(rand_x, rand_y)
        ground()
        stone(randstone_x)
        pygame.display.update()
        clock.tick(60)
        stone_pos = False

def main():
    loop()
    pygame.quit()
    quit()
main()