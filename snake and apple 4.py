__author__ = 'shubham singh'
import  pygame
import random
from time import sleep
pygame.init()
gameDisplay = pygame.display.set_mode((900, 600))
pygame.display.set_caption("snake and apple")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
BLUE = (10, 0, 250)
BLACK = (0, 0, 0)
RED = (250, 10, 10)
GREEN = (53, 214, 147)
init_x = 430
init_y = 280
font = pygame.font.SysFont("comicsansms", 45)
clock = pygame.time.Clock()
snake_head = pygame.image.load("head.png")
direction = "up"

def snake (snakelist , block_size):
    if direction == "right":
        head = pygame.transform.rotate(snake_head, 270)
    if direction == "left":
        head = pygame.transform.rotate(snake_head, 90)
    if direction == "up":
        head = snake_head
    if direction == "down":
        head = pygame.transform.rotate(snake_head, 180)

    gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, BLUE, (XnY[0]+3.6, XnY[1]+3.6, block_size, block_size))

def score (score):
    text = font.render("Score: "+str(score), True, BLACK)
    gameDisplay.blit(text, (10, 10))

def ur_score(score):
    text = font.render("Your Score: "+str(score), True, RED)
    gameDisplay.blit(text, (310, 210))

snakelen = 15
score_ = 0
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

        if rand_x > init_x :
            if rand_y > init_y:
                if rand_y - init_y < 25 and rand_x - init_x < 25:
                    gameExit = True
                    score_ +=10
                    speed +=5
            if init_y > rand_y:
                if init_y - rand_y < 40 and rand_x - init_x < 40:
                    gameExit = True
                    speed += 5
                    score_ += 10
        if rand_x < init_x :
            if rand_y > init_y:
                if rand_y - init_y < 40 and init_x - rand_x < 40:
                    gameExit = True
                    speed += 5
                    score_ += 10
            if init_y > rand_y:
                if init_y - rand_y < 40 and init_x - rand_x < 40:
                    gameExit = True
                    speed += 5
                    score_ += 10

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
        pygame.display.update()
        clock.tick(speed)
if i:
    gameDisplay.fill(GREEN)
    ur_score(score_)
    soundObj4 = pygame.mixer.Sound('match20.wav')
    soundObj4.play()
    pygame.display.update()
    sleep(3.5)


pygame.quit()
quit()