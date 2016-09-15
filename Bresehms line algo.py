__author__ = 'shubham singh'
import pygame
from pygame import gfxdraw

WHITE = (255, 255, 255)
def line(x1,y1,x2,y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    e = 2*dy - dx
    two_dy = 2 * dy
    two_dydx = 2 * (dy - dx)
    if x1 > x2:
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    gfxdraw.pixel(display, x, y, WHITE)
    if dx != 0:
        while x < xend :
            x += 1
            if e < 0:
                e += two_dy
            else:
                y += 1
                e += two_dydx
            gfxdraw.pixel(display, x, y, WHITE)
    if dx == 0:
         for i in range(0, dy):
            gfxdraw.pixel(display, int(x), int(y+i), WHITE)

print("enter the value of x1,y1,x2,y2")
x1, y1, x2, y2 = input().split()

display = pygame.display.set_mode((800,500))

line(int(x1), int(y1), int(x2), int(y2))
pygame.display.update()
Exit = False
while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
pygame.quit()
exit()