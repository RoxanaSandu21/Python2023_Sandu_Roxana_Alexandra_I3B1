import pygame
import sys
import pygame.gfxdraw
from pygame.locals import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 850
TEXT_HEIGHT = 20

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
BACKGROUND_COLOR = (233, 232, 255)

COLOR_LIST = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]


def make_display():
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY_RECT = DISPLAY_SURF.get_rect()
    DISPLAY_SURF.fill(BACKGROUND_COLOR)

    return DISPLAY_SURF, DISPLAY_RECT


def terminate():
    pygame.quit()
    sys.exit()


def run():
    while True:
        DISPLAY_SURF.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        pygame.display.update()


def main():
    pygame.init()
    pygame.display.set_caption('Bubble Buster')
    pygame.font.SysFont('Helvetica', TEXT_HEIGHT)
    while True:
        run()


DISPLAY_SURF, DISPLAY_RECT = make_display()

if __name__ == "__main__":
    main()
