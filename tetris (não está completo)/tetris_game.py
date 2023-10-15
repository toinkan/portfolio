import pygame
from tetris_pecas import *
from pygame.locals import *

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('tetris')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.update()
