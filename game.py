'''
FINDING PY
ADITI SHARMA
ANANYA BHAT
BHAVINI MATHUR
RHUCHA SANT
'''

import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1060, 720))
clock = pygame.time.Clock()
speed = [2, 2]
black = 0, 0, 0
size = width, height = 1060, 720
running = True


window = pygame.display.set_mode((width, height))
i = 0


def homepg():

    bg = pygame.image.load("homebg2.png")
    mixer.music.load('bgm.mp3')
    mixer.music.play(-1)
    running = True
    while running:
        # display_surface.fill(white)
        # display_surface.blit(text, textRect)
        window.blit(bg, (i, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        pygame.display.flip()


homepg()
pygame.quit()
