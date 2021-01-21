import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()

running = True
background = GRAY

start = (0, 0)
size = (0, 0)
drawing = False

screen = pygame.display.set_mode((640, 240))
pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
        screen.fill(GRAY)
        pygame.draw.rect(screen, RED, (start, size), 2)
        pygame.display.update()    

#     screen.fill(background)
#   
#     pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
#     pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
#     pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))
# 
#     pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
#     pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
#     pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)
#     pygame.display.update()
    
pygame.quit()