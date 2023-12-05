import pygame
import sys
import pygame.gfxdraw
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
TEXTHEIGHT = 20


GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COMBLUE = (233, 232, 255)

BGCOLOR = COMBLUE
COLORLIST = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]



def main():
    global DISPLAYSURF, DISPLAYRECT, MAINFONT
    pygame.init()
    pygame.display.set_caption('Bubble Buster')
    MAINFONT = pygame.font.SysFont('Helvetica', TEXTHEIGHT)
    DISPLAYSURF, DISPLAYRECT = makeDisplay()

    while True:
        run()


def run():
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()


def makeDisplay():
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYRECT = DISPLAYSURF.get_rect()
    DISPLAYSURF.fill(BGCOLOR)
    #DISPLAYSURF.convert()
    pygame.display.update()

    return DISPLAYSURF, DISPLAYRECT


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
