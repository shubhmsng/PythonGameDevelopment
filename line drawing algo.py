__author__ = 'shubham singh'
import pygame
from pygame import gfxdraw

def draw_line(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx != 0 and dy != 0:
        m = (dy / dx)
        x = x1
        y = m * (x - x1) + y1
        for x in range(x1, dx):
            y = m * (x - x1) + y1
            gfxdraw.pixel(display, int(x), int(y), WHITE)

        if dy != 0:
            y = y1
            x = ((y - y1) / m) + x1
            for y in range(y1, dy):
                x = ((y - y1) / m) + x1
                gfxdraw.pixel(display, int(x), int(y), WHITE)
            pygame.display.update()
    elif dx == 0:
        y = y1
        for i in range(0, dy):
            gfxdraw.pixel(display, int(x1), int(y + i), WHITE)
        pygame.display.update()
    else:
        x = x1
        for i in range(0, dx):
            gfxdraw.pixel(display, int(x + i), int(y1), WHITE)
        pygame.display.update()


GREEN = (0, 250, 10)
RED = (250, 0, 0)
WHITE = (255, 255, 255)
print("enter the value of x1,y1,x2,y2")
x1, y1, x2, y2 = input().split()
display = pygame.display.set_mode((1200, 900))

draw_line(x1, y1, x2, y2)
WindowExit = False
while not WindowExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WindowExit = True
pygame.quit()
exit()
