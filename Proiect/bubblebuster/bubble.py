import random

import pygame
import main


class Bubble(pygame.sprite.Sprite):

    def __init__(self, color, row=0, column=0):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.centerx = main.START_X
        self.rect.centery = main.START_Y
        self.speed = 10
        self.color = color
        self.radius = main.BUBBLE_RADIUS
        self.angle = 0
        self.row = row
        self.column = column

    def draw(self):
        pygame.gfxdraw.filled_circle(main.DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(main.DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, main.BLACK)


def set_bubbles(array, game_color_list):
    for row in range(main.BUBBLE_LAYERS):
        for column in range(len(array[row])):
            random.shuffle(game_color_list)
            new_bubble = Bubble(game_color_list[0], row, column)
            array[row][column] = new_bubble

    set_array_pos(array)


def draw_bubble_array(array):
    for row in range(main.ARRAY_HEIGHT):
        for column in range(len(array[row])):
            if array[row][column] != main.BLANK:
                array[row][column].draw()


def set_array_pos(array):
    for row in range(main.ARRAY_HEIGHT):
        for column in range(len(array[row])):
            if array[row][column] != main.BLANK:
                array[row][column].rect.x = (main.BUBBLE_WIDTH * column) + 5
                array[row][column].rect.y = (main.BUBBLE_WIDTH * row) + 5

    for row in range(1, main.ARRAY_HEIGHT, 2):
        for column in range(len(array[row])):
            if array[row][column] != main.BLANK:
                array[row][column].rect.x += main.BUBBLE_RADIUS

    for row in range(1, main.ARRAY_HEIGHT):
        for column in range(len(array[row])):
            if array[row][column] != main.BLANK:
                array[row][column].rect.y -= (main.BUBBLE_Y_ADJUST * row)