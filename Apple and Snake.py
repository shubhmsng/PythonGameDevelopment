__author__ = 'shubham singh'
import  pygame
import random
from time import sleep
pygame.init()
gameDisplay = pygame.display.set_mode((900, 600))
pygame.display.set_caption("snake and apple")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
BLUE = (100,100 , 250)
BLACK = (0, 0, 0)
RED = (250, 10, 10)
GREEN = (53, 214, 147)
YELLOW = (245, 255, 60)
init_x = 430
init_y = 280
font = pygame.font.SysFont("comicsansms", 45)
clock = pygame.time.Clock()
snake_head = pygame.image.load("head.png")
direction = "up"

def snake (snakelist , block_size):
    if direction == "right":
        for XnY in snakelist[:-1]:
            pygame.draw.rect(gameDisplay, BLUE, (XnY[0], XnY[1], block_size, block_size))
        head = pygame.transform.rotate(snake_head, 270)
        gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]-3))

    if direction == "left":
        for XnY in snakelist[:-1]:
            pygame.draw.rect(gameDisplay, BLUE, (XnY[0], XnY[1], block_size, block_size))
        head = pygame.transform.rotate(snake_head, 90)
        gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]-2))

    if direction == "up":
        for XnY in snakelist[:-1]:
            pygame.draw.rect(gameDisplay, BLUE, (XnY[0], XnY[1], block_size, block_size))
        head = snake_head
        gameDisplay.blit(head,(snakelist[-1][0]-2, snakelist[-1][1]))

    if direction == "down":
        for XnY in snakelist[:-1]:
            pygame.draw.rect(gameDisplay, BLUE, (XnY[0], XnY[1], block_size, block_size))
        head = pygame.transform.rotate(snake_head, 180)
        gameDisplay.blit(head,(snakelist[-1][0]-2, snakelist[-1][1]))


def score (score):
    text = font.render("Score: "+str(score), True, BLACK)
    gameDisplay.blit(text, (10, 10))

def ur_score(score):
    text = font.render("Your Score: "+str(score), True, RED)
    gameDisplay.blit(text, (310, 310))

def g_level(level):
    text = font.render("Level: "+ str(level), True, RED)
    gameDisplay.blit(text, (10, 60))

snakelen = 15
score_ = 0
level = 1
gameover = False
i = False
speed = 50
while not gameover:
    global direction
    gameExit = False
    lead_x = 0
    lead_y = 0
    snakelist = []
    rand_x = random.randrange(0, 900-30)
    rand_y = random.randrange(0, 600-30)
    while not gameExit:
        gameDisplay.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if init_x > 0:
                        lead_x -= 5
                    lead_y = 0
                    direction = "left"
                if event.key == pygame.K_RIGHT:
                    if init_x < 880:
                        lead_x += 5
                    direction = "right"
                    lead_y = 0
                if event.key == pygame.K_UP:
                    if init_y > 0:
                        lead_y -= 5
                    lead_x = 0
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    if init_y < 580:
                        lead_y += 5
                    lead_x = 0
                    direction = "down"
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()


        if ( init_x >= 0 and init_x <= 880 ):
                init_x += lead_x
        else:
            gameExit = True
            gameover = True
            i = True
            break
        if ( init_y >= 0 and init_y <= 580 ):
            init_y += lead_y
        else:
            gameExit = True
            gameover = True
            i = True
            break
        if init_x == 0 or init_y ==0:
            gameExit = True
            gameover = True
            i = True
            break

        if rand_x >= init_x :
            if rand_y >= init_y:
                if rand_y - init_y < 25 and rand_x - init_x < 25:
                    gameExit = True
                    score_ +=10
                    speed +=5

                    if level <=20:
                        level += 1
            if init_y > rand_y:
                if init_y - rand_y < 40 and rand_x - init_x < 40:
                    gameExit = True
                    speed += 5
                    score_ += 10
                    if level <=20:
                        level += 1
        if rand_x < init_x :
            if rand_y >= init_y:
                if rand_y - init_y < 40 and init_x - rand_x < 40:
                    gameExit = True
                    speed += 5
                    score_ += 10

                    if level <=20:
                        level += 1
            if init_y > rand_y:
                if init_y - rand_y < 40 and init_x - rand_x < 40:
                    gameExit = True
                    speed += 5
                    score_ += 10

                    if level <=20:
                        level += 1
        snakehead = []
        snakehead.append(init_x)
        snakehead.append(init_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelen:
            del snakelist[0]


        snake(snakelist, 15)
        img = pygame.image.load("apple.png")
        gameDisplay.blit(img, (rand_x, rand_y))
        score(score_)
        g_level(level)
        pygame.display.update()
        clock.tick(speed)
if i:
    gameDisplay.fill(GREEN)
    ur_score(score_)

    if score_ >= 150 and score_ <200:
        img1 = pygame.image.load("medal3.jpg")
        gameDisplay.blit(img1, (310,10))
        text = font.render("Congratulation You got << BRONZE >> ", True, RED)
        text2 = font.render("!!!Go For gold!!!", True, BLUE)
        gameDisplay.blit(text, (110, 450))
        gameDisplay.blit(text2, (170, 520))

    elif score_ >= 200 and score_ <250:
        img2 = pygame.image.load("medal2.jpg")
        gameDisplay.blit(img2, (310,10))
        text = font.render("Congratulation You got << SILVER >>", True, RED)
        text2 = font.render("!!! Go for Gold !!!", True, BLUE)
        gameDisplay.blit(text, (110, 450))
        gameDisplay.blit(text2, (170, 520))
    elif score_ >= 250:
        img3 = pygame.image.load("medal1.jpg")
        gameDisplay.blit(img3, (310,10))
        text = font.render("Congratulation You got << GOLDEN >>", True, RED)
        text2 = font.render("!!!!!!!You make a World Record !!!!!!", True, YELLOW)
        gameDisplay.blit(text, (110, 450))
        gameDisplay.blit(text2, (130, 520))
    else:
        text = font.render("You did'n got any Badge ", True, RED)
        gameDisplay.blit(text, (210, 450))
    soundObj4 = pygame.mixer.Sound('match20.wav')
    soundObj4.play()


    pygame.display.update()
    sleep(3)

pygame.quit()
quit()
