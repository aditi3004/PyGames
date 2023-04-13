'''
FINDING PY
ADITI SHARMA
ANANYA BHAT
BHAVINI MATHUR
RHUCHA SANT
'''

import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
speed = [2, 2]
black = 0, 0, 0
size = width, height = 640, 360
running = True
bg = pygame.image.load("dungeon_pre.png")
bg = pygame.transform.scale(bg, (width, height))

window = pygame.display.set_mode((width, height))
i = 0


def homepg():
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    display_surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('FINDING PY')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('FINDING PY', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)
    running = True
    bg = pygame.image.load("homebg.jpg")
    bg = pygame.transform.scale(bg, (width, height))
    while running:
        display_surface.fill(white)
        display_surface.blit(text, textRect)
        window.blit(bg, (i, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        pygame.display.flip()


homepg()
pygame.quit()
