import copy
import random
import pygame
import sys
import pygame.gfxdraw
from pygame.locals import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 850
TEXT_HEIGHT = 20

RIGHT = 'right'
LEFT = 'left'

BUBBLE_RADIUS = 27
BUBBLE_WIDTH = BUBBLE_RADIUS * 2
BUBBLE_LAYERS = 5
START_X = WINDOW_WIDTH / 2
START_Y = WINDOW_HEIGHT - 75
ARRAY_WIDTH = 12
ARRAY_HEIGHT = 21

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


class Arrow(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.angle = 90
        arrow_image = pygame.image.load('arrow.png')
        arrow_rect = arrow_image.get_rect()
        new_width = int(arrow_rect.width / 2.5)
        new_height = int(arrow_rect.height / 2.5)
        self.image = pygame.transform.scale(arrow_image, (new_width, new_height))

        self.transformImage = self.image
        self.rect = arrow_rect
        self.rect.centerx = START_X
        self.rect.centery = START_Y

    def update(self, direction):

        if direction == LEFT and self.angle < 180:
            self.angle += 1
        elif direction == RIGHT and self.angle > 0:
            self.angle -= 1

        self.transformImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.transformImage.get_rect()
        self.rect.centerx = START_X
        self.rect.centery = START_Y

    def draw(self):
        DISPLAY_SURF.blit(self.transformImage, self.rect)


class Bubble(pygame.sprite.Sprite):

    def __init__(self, color, row=0, column=0):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.centerx = START_X
        self.rect.centery = START_Y
        self.color = color
        self.radius = BUBBLE_RADIUS
        self.angle = 0
        self.row = row
        self.column = column

    def draw(self):
        pygame.gfxdraw.filled_circle(DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, BLACK)


def set_bubbles(array, game_color_list):
    for row in range(BUBBLE_LAYERS):
        for column in range(len(array[row])):
            random.shuffle(game_color_list)
            new_bubble = Bubble(game_color_list[0], row, column)
            array[row][column] = new_bubble

    set_array_pos(array)


def draw_bubble_array(array):
    for row in range(ARRAY_HEIGHT):
        for column in range(len(array[row])):
            if array[row][column] is not None:
                array[row][column].draw()


def set_array_pos(array):
    for row in range(ARRAY_HEIGHT):
        for column in range(len(array[row])):
            if array[row][column] is not None:
                array[row][column].rect.x = (BUBBLE_WIDTH * column) + 5
                array[row][column].rect.y = (BUBBLE_WIDTH * row) + 5

    for row in range(1, ARRAY_HEIGHT, 2):
        for column in range(len(array[row])):
            if array[row][column] is not None:
                array[row][column].rect.x += BUBBLE_RADIUS

    for row in range(1, ARRAY_HEIGHT):
        for column in range(len(array[row])):
            if array[row][column] is not None:
                array[row][column].rect.y -= (5 * row)


def make_blank_board():
    array = []
    for row in range(ARRAY_HEIGHT):
        column = []
        for i in range(ARRAY_WIDTH):
            column.append(None)
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
    set_bubbles(bubble_array, game_color_list)
    arrow = Arrow()
    clock = pygame.time.Clock()

    while True:
        DISPLAY_SURF.fill(BACKGROUND_COLOR)
        draw_bubble_array(bubble_array)

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            direction = LEFT
        elif keys[K_RIGHT]:
            direction = RIGHT
        else:
            direction = None

        arrow.update(direction)
        arrow.draw()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        pygame.display.update()
        clock.tick(120)


def main():
    global DISPLAY_SURF, DISPLAY_RECT
    pygame.init()
    pygame.display.set_caption('Bubble Buster')
    pygame.font.SysFont('Helvetica', TEXT_HEIGHT)
    DISPLAY_SURF, DISPLAY_RECT = make_display()
    while True:
        run()


if __name__ == "__main__":
    main()
