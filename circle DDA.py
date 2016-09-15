__author__ = 'shubham singh'
import pygame
from pygame import gfxdraw
from time import sleep
WHITE = (255, 255, 255)
RED = (250, 200, 122)
BLUE = (10, 20, 211)
GREEN = (10,234,100)
def circle(x, y, r):
    d = 3-2*r
    x1 = 0
    y1 = r
    while(x1 < y1):
        gfxdraw.pixel(display, x+x1, y+y1, WHITE)
        gfxdraw.pixel(display, y+y1, x+x1, RED)
        gfxdraw.pixel(display, y+y1, x-x1, BLUE)
        gfxdraw.pixel(display, x+x1, y-y1, GREEN)
        gfxdraw.pixel(display, x-x1, y-y1, WHITE)
        gfxdraw.pixel(display, y-y1, x-x1, RED)
        gfxdraw.pixel(display, y-y1, x+x1, GREEN)
        gfxdraw.pixel(display, x-x1, y+y1, BLUE)
        if(d<=0):
            d = d+4*x1+6
        else:
            d = d+4*(x1-y1)+10
            y1 -= 1
        x1 += 1
        sleep(.15)
        pygame.display.update()


print("enter the value of x,y,r, and x must equal to y(x = y)")
x, y, r = input().split()

display = pygame.display.set_mode((800,500))

circle(int(x), int(y), int(r))
pygame.display.update()
Exit = False
while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
pygame.quit()
exit()