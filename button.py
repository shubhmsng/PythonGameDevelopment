import pygame
gdisplay = pygame.display.set_mode((500,500))

pygame.display.set_caption("button")
BLUE = (10, 0, 250)
BLACK = (0, 0, 0)
RED = (250, 10, 10)
GREEN = (53, 214, 147)
LIGHT_GREEN =(0, 255, 0)
WHITE = (255, 255, 255)
mousex = 0
mousey = 0

clock = pygame.time.Clock()
mouseClicked = False
while True:
    gdisplay.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type ==pygame.MOUSEBUTTONUP:
            mouseClicked = True
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos

        if (100 < mousex and mousex < 200) and (300 < mousey and mousey < 350):
            pygame.draw.rect(gdisplay,BLACK, (100, 300, 150, 50))
            if mouseClicked:
                pygame.quit()
                pygame.display.update()
        else:
            pygame.draw.rect(gdisplay, GREEN, (100, 300, 150, 50))
            image = pygame.image.load("click.png")
        gdisplay.blit(image, (100,300))

    pygame.display.update()

quit()