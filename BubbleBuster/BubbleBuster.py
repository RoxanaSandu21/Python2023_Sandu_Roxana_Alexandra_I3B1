import copy
import random
import math
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
        self.speed = 10
        self.color = color
        self.radius = BUBBLE_RADIUS
        self.angle = 0
        self.row = row
        self.column = column

    def update(self):

        if self.angle == 90:
            x_move = 0
            y_move = self.speed * -1
        elif self.angle < 90:
            x_move = self.x_calculate(self.angle)
            y_move = self.y_calculate(self.angle)
        elif self.angle > 90:
            x_move = self.x_calculate(180 - self.angle) * -1
            y_move = self.y_calculate(180 - self.angle)

        self.rect.x += x_move
        self.rect.y += y_move

    def draw(self):
        pygame.gfxdraw.filled_circle(DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, BLACK)

    def x_calculate(self, angle):
        radians = math.radians(angle)
        x_move = math.cos(radians) * (self.speed)
        return x_move

    def y_calculate(self, angle):
        radians = math.radians(angle)
        y_move = math.sin(radians) * (self.speed) * -1
        return y_move


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


def update_color_list(bubble_array):
    new_color_list = []

    for row in range(len(bubble_array)):
        for column in range(len(bubble_array[0])):
            if bubble_array[row][column] is not None:
                new_color_list.append(bubble_array[row][column].color)

    color_set = set(new_color_list)

    if len(color_set) < 1:
        color_list = []
        color_list.append(WHITE)
        return color_list

    else:

        return list(color_set)


def stop_bubble(bubble_array, new_bubble, launch_bubble):
    for row in range(len(bubble_array)):
        for column in range(len(bubble_array[row])):
            if bubble_array[row][column] is not None and new_bubble is not None:
                if (pygame.sprite.collide_rect(new_bubble, bubble_array[row][column])) or new_bubble.rect.top < 0:
                    if new_bubble.rect.centery >= bubble_array[row][column].rect.centery:
                        if new_bubble.rect.centerx >= bubble_array[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                new_row = row + 1
                                new_column = column
                                if new_row < len(bubble_array) and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row - 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                    launch_bubble = False
                    new_bubble = None

    return launch_bubble, new_bubble


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

    bubble_array = make_blank_board()
    set_bubbles(bubble_array, game_color_list)
    launch_bubble = False
    new_bubble = None

    next_bubble = Bubble(game_color_list[0])
    next_bubble.rect.right = WINDOW_WIDTH - 5
    next_bubble.rect.bottom = WINDOW_HEIGHT - 5

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

            elif event.type == KEYUP:
                direction = None
                if event.key == K_SPACE:
                    launch_bubble = True

        if launch_bubble:
            if new_bubble is None:
                new_bubble = Bubble(next_bubble.color)
                new_bubble.angle = arrow.angle

            new_bubble.update()
            new_bubble.draw()

            if new_bubble.rect.right >= WINDOW_WIDTH - 5:
                new_bubble.angle = 180 - new_bubble.angle
            elif new_bubble.rect.left <= 5:
                new_bubble.angle = 180 - new_bubble.angle

            launch_bubble, new_bubble = stop_bubble(bubble_array, new_bubble, launch_bubble)

            final_bubble_list = []
            for row in range(len(bubble_array)):
                for column in range(len(bubble_array[0])):
                    if bubble_array[row][column] is not None:
                        final_bubble_list.append(bubble_array[row][column])

            game_color_list = update_color_list(bubble_array)
            random.shuffle(game_color_list)

            if not launch_bubble:
                next_bubble = Bubble(game_color_list[0])
                next_bubble.rect.right = WINDOW_WIDTH - 5
                next_bubble.rect.bottom = WINDOW_HEIGHT - 5

        next_bubble.draw()
        arrow.update(direction)
        arrow.draw()

        set_array_pos(bubble_array)
        draw_bubble_array(bubble_array)

        pygame.display.update()
        clock.tick(100)


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
