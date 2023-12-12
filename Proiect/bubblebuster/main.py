import copy
import random
import bubble
import pygame
import sys
import pygame.gfxdraw
from pygame.locals import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 850
TEXT_HEIGHT = 20

BUBBLE_RADIUS = 27
BUBBLE_WIDTH = BUBBLE_RADIUS * 2
BUBBLE_LAYERS = 5
BUBBLE_Y_ADJUST = 5
START_X = WINDOW_WIDTH / 2
START_Y = WINDOW_HEIGHT - 75
ARRAY_WIDTH = 12
ARRAY_HEIGHT = 21

BLANK = '.'

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


def make_blank_board():
    array = []
    for row in range(ARRAY_HEIGHT):
        column = []
        for i in range(ARRAY_WIDTH):
            column.append(BLANK)
        array.append(column)

    return array


def make_display():
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY_RECT = DISPLAY_SURF.get_rect()
    DISPLAY_SURF.fill(BACKGROUND_COLOR)

    return DISPLAY_SURF, DISPLAY_RECT


def terminate():
    pygame.quit()
    sys.exit()


def run():
    game_color_list = copy.deepcopy(COLOR_LIST)
    bubble_array = make_blank_board()
    bubble.set_bubbles(bubble_array, game_color_list)
    while True:
        DISPLAY_SURF.fill(BACKGROUND_COLOR)
        bubble.draw_bubble_array(bubble_array)

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
