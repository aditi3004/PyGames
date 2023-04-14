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
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1060, 720))
clock = pygame.time.Clock()
speed = [2, 2]
black = 0, 0, 0
size = width, height = 1060, 720
running = True


window = pygame.display.set_mode((width, height))
i = 0

font = pygame.font.SysFont('freesansbold', 40)

objects = []


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#964B00',
            'hover': '#C4A484',
            'pressed': '#964B01',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (50, 50, 50))

        self.alreadyPressed = False
        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
    apt = pygame.image.load("apt.jpg")
    running = True
    while running:
        # display_surface.fill(white)
        # display_surface.blit(text, textRect)
        window.blit(apt, (i, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for object in objects:
            object.process()

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


customButton = Button(370, 550, 300, 100, 'START GAME', myFunction)


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

        for object in objects:
            object.process()

        pygame.display.update()
        pygame.display.flip()


homepg()
pygame.quit()
