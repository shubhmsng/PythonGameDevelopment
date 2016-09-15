__author__ = 'shubham singh'
import pygame
from pygame import gfxdraw
from time import sleep

def sign(m):
    if m < 0:
        return 1
    if m > 0:
        return 1
    if m == 0:
        return 0

GREEN = (0, 250, 10)
RED = (250, 0, 0)
WHITE = (255, 255, 255)
print("enter the value of x1,y1,x2,y2");
x1,y1,x2,y2 = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
dx = x2 - x1
dy = y2 - y1

display = pygame.display.set_mode((1200,900))
if abs(dx) >= abs(dy):
    m = abs(dx)
else:
    m = abs(dy)
delx = int(dx/m)
dely = int(dy/m)
x = x1 + 0.5*sign(delx)
y = y1 + 0.5*sign(dely)
gfxdraw.pixel(display,int(x),int(y),RED)
for i in range(0,m):
    x = x + delx
    y = y + dely
    gfxdraw.pixel(display,int(x),int(y),WHITE)


pygame.display.update()
WindowExit = True
while WindowExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WindowExit = False
pygame.quit()
exit()
