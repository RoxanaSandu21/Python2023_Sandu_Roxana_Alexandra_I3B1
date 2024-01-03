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


class Score(object):
    def __init__(self):
        self.total = 0
        self.font = pygame.font.SysFont('comicsansms', 20)
        self.render = self.font.render('Score: ' + str(self.total), True, BLACK, WHITE)
        self.rect = self.render.get_rect()
        self.rect.left = 5
        self.rect.bottom = WINDOW_HEIGHT - 30

    def update(self, delete_list):
        self.total += ((len(delete_list)) * 10)
        self.render = self.font.render('Score: ' + str(self.total), True, BLACK, WHITE)

    def draw(self):
        DISPLAY_SURF.blit(self.render, self.rect)


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
        else:
            x_move = self.x_calculate(180 - self.angle) * -1
            y_move = self.y_calculate(180 - self.angle)

        self.rect.x += x_move
        self.rect.y += y_move

    def draw(self):
        pygame.gfxdraw.filled_circle(DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(DISPLAY_SURF, self.rect.centerx + 10, self.rect.centery, self.radius, BLACK)

    def x_calculate(self, angle):
        radians = math.radians(angle)
        x_move = math.cos(radians) * self.speed
        return x_move

    def y_calculate(self, angle):
        radians = math.radians(angle)
        y_move = math.sin(radians) * self.speed * -1
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
        color_list = [WHITE]
        return color_list

    else:

        return list(color_set)


def check_for_floaters(bubble_array):
    bubble_list = [column for column in range(len(bubble_array[0])) if bubble_array[0][column] is not None]
    new_bubble_list = []

    for i in range(len(bubble_list)):
        if i == 0:
            new_bubble_list.append(bubble_list[i])
        elif bubble_list[i] > bubble_list[i - 1] + 1:
            new_bubble_list.append(bubble_list[i])

    copy_of_board = copy.deepcopy(bubble_array)

    for row in range(len(bubble_array)):
        for column in range(len(bubble_array[0])):
            bubble_array[row][column] = None

    for column in new_bubble_list:
        pop_floaters(bubble_array, copy_of_board, column)


def pop_floaters(bubble_array, copy_of_board, column, row=0):
    if (row < 0 or row > (len(bubble_array) - 1)
            or column < 0 or column > (len(bubble_array[0]) - 1)):
        return

    elif copy_of_board[row][column] is None:
        return

    elif bubble_array[row][column] == copy_of_board[row][column]:
        return

    bubble_array[row][column] = copy_of_board[row][column]

    if row == 0:
        pop_floaters(bubble_array, copy_of_board, column + 1, row)
        pop_floaters(bubble_array, copy_of_board, column - 1, row)
        pop_floaters(bubble_array, copy_of_board, column, row + 1)
        pop_floaters(bubble_array, copy_of_board, column - 1, row + 1)

    elif row % 2 == 0:
        pop_floaters(bubble_array, copy_of_board, column + 1, row)
        pop_floaters(bubble_array, copy_of_board, column - 1, row)
        pop_floaters(bubble_array, copy_of_board, column, row + 1)
        pop_floaters(bubble_array, copy_of_board, column - 1, row + 1)
        pop_floaters(bubble_array, copy_of_board, column, row - 1)
        pop_floaters(bubble_array, copy_of_board, column - 1, row - 1)

    else:
        pop_floaters(bubble_array, copy_of_board, column + 1, row)
        pop_floaters(bubble_array, copy_of_board, column - 1, row)
        pop_floaters(bubble_array, copy_of_board, column, row + 1)
        pop_floaters(bubble_array, copy_of_board, column + 1, row + 1)
        pop_floaters(bubble_array, copy_of_board, column, row - 1)
        pop_floaters(bubble_array, copy_of_board, column + 1, row - 1)


def stop_bubble(bubble_array, new_bubble, launch_bubble, score, pop_sound):
    delete_list = []
    new_row = 0
    new_column = 0

    for row in range(len(bubble_array)):
        for column in range(len(bubble_array[row])):

            if bubble_array[row][column] is not None and new_bubble is not None:
                if (pygame.sprite.collide_rect(new_bubble, bubble_array[row][column])) or new_bubble.rect.top < 0:
                    if new_bubble.rect.top < 0:
                        new_row, new_column = add_bubble_to_top(bubble_array, new_bubble)

                    elif new_bubble.rect.centery >= bubble_array[row][column].rect.centery:

                        if new_bubble.rect.centerx >= bubble_array[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                new_row = row + 1
                                new_column = column
                                if new_row < len(bubble_array) and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row - 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                            else:
                                new_row = row + 1
                                new_column = column + 1
                                if new_row < len(bubble_array) and new_column < len(bubble_array[row]) and \
                                        bubble_array[new_row][new_column] is not None:
                                    new_row = new_row - 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                        elif new_bubble.rect.centerx < bubble_array[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                new_row = row + 1
                                new_column = column - 1
                                if new_column >= 0 and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row - 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column
                            else:
                                new_row = row + 1
                                new_column = column
                                if new_row < len(bubble_array) and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row - 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                    elif new_bubble.rect.centery < bubble_array[row][column].rect.centery:
                        if new_bubble.rect.centerx >= bubble_array[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                new_row = row - 1
                                new_column = column
                                if new_row >= 0 and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row + 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column
                            else:
                                new_row = row - 1
                                new_column = column + 1
                                if new_row >= 0 and new_column < len(bubble_array[row]) and \
                                        bubble_array[new_row][new_column] is not None:
                                    new_row = new_row + 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                        elif new_bubble.rect.centerx <= bubble_array[row][column].rect.centerx:
                            if row == 0 or row % 2 == 0:
                                new_row = row - 1
                                new_column = column - 1
                                if new_row >= 0 and new_column >= 0 and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row + 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                            else:
                                new_row = row - 1
                                new_column = column
                                if new_row >= 0 and bubble_array[new_row][new_column] is not None:
                                    new_row = new_row + 1
                                bubble_array[new_row][new_column] = copy.copy(new_bubble)
                                bubble_array[new_row][new_column].row = new_row
                                bubble_array[new_row][new_column].column = new_column

                    pop_bubbles(bubble_array, new_row, new_column, new_bubble.color, delete_list)

                    if len(delete_list) >= 3:
                        pop_sound.play()
                        for pos in delete_list:
                            row = pos[0]
                            column = pos[1]
                            if 0 <= row < len(bubble_array) and 0 <= column < len(bubble_array[row]):
                                bubble_array[row][column] = None
                        check_for_floaters(bubble_array)
                        score.update(delete_list)

                    launch_bubble = False
                    new_bubble = None

    return launch_bubble, new_bubble, score


def add_bubble_to_top(bubble_array, bubble):
    pos_x = bubble.rect.centerx
    left_side_x = pos_x - BUBBLE_RADIUS

    column_division = math.modf(float(left_side_x) / float(BUBBLE_WIDTH))
    column = int(column_division[1])

    if column_division[0] < 0.5:
        bubble_array[0][column] = copy.copy(bubble)
    else:
        column += 1
        bubble_array[0][column] = copy.copy(bubble)

    row = 0

    return row, column


def pop_bubbles(bubble_array, row, column, color, delete_list):
    if row < 0 or column < 0 or row > (len(bubble_array) - 1) or column > (len(bubble_array[0]) - 1):
        return

    elif bubble_array[row][column] is None:
        return

    elif bubble_array[row][column].color != color:
        return

    for bubble in delete_list:
        if bubble_array[bubble[0]][bubble[1]] == bubble_array[row][column]:
            return

    delete_list.append((row, column))

    if row == 0:
        pop_bubbles(bubble_array, row, column - 1, color, delete_list)
        pop_bubbles(bubble_array, row, column + 1, color, delete_list)
        pop_bubbles(bubble_array, row + 1, column, color, delete_list)
        pop_bubbles(bubble_array, row + 1, column - 1, color, delete_list)

    elif row % 2 == 0:

        pop_bubbles(bubble_array, row + 1, column, color, delete_list)
        pop_bubbles(bubble_array, row + 1, column - 1, color, delete_list)
        pop_bubbles(bubble_array, row - 1, column, color, delete_list)
        pop_bubbles(bubble_array, row - 1, column - 1, color, delete_list)
        pop_bubbles(bubble_array, row, column + 1, color, delete_list)
        pop_bubbles(bubble_array, row, column - 1, color, delete_list)

    else:
        pop_bubbles(bubble_array, row - 1, column, color, delete_list)
        pop_bubbles(bubble_array, row - 1, column + 1, color, delete_list)
        pop_bubbles(bubble_array, row + 1, column, color, delete_list)
        pop_bubbles(bubble_array, row + 1, column + 1, color, delete_list)
        pop_bubbles(bubble_array, row, column + 1, color, delete_list)
        pop_bubbles(bubble_array, row, column - 1, color, delete_list)


def cover_next_bubble():
    white_rect = pygame.Rect(0, 0, BUBBLE_WIDTH, BUBBLE_WIDTH)
    white_rect.bottom = WINDOW_HEIGHT
    white_rect.right = WINDOW_WIDTH
    pygame.draw.rect(DISPLAY_SURF, BACKGROUND_COLOR, white_rect)


def move_bubbles_down(move_counter, bubble_array, game_color_list):
    if move_counter >= 5:
        for row in range(len(bubble_array) - 1, 0, -1):
            for column in range(len(bubble_array[row])):
                bubble_array[row][column] = bubble_array[row - 2][column]

        for column in range(len(bubble_array[0])):
            random.shuffle(game_color_list)
            bubble_array[0][column] = Bubble(game_color_list[0])
        for column in range(len(bubble_array[1])):
            random.shuffle(game_color_list)
            bubble_array[1][column] = Bubble(game_color_list[1])

        move_counter = 0

    return move_counter, bubble_array


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


def run(difficulty):
    game_color_list = copy.deepcopy(COLOR_LIST)
    bubble_array = make_blank_board()
    set_bubbles(bubble_array, game_color_list)
    arrow = Arrow()
    score = Score()
    clock = pygame.time.Clock()
    move_counter = 0

    bubble_array = make_blank_board()
    set_bubbles(bubble_array, game_color_list)
    launch_bubble = False
    new_bubble = None

    next_bubble = Bubble(game_color_list[0])
    next_bubble.rect.right = WINDOW_WIDTH - 5
    next_bubble.rect.bottom = WINDOW_HEIGHT - 5

    font = pygame.font.SysFont('comicsansms', 20)
    difficulty_text = font.render(f'Difficulty: {difficulty.capitalize()}', True, BLACK, WHITE)
    text_rect = difficulty_text.get_rect(left=5, top=WINDOW_HEIGHT - 29)

    pygame.mixer.init()
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)

    launch_sound = pygame.mixer.Sound('launch.mp3')
    pop_sound = pygame.mixer.Sound('pop.wav')

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
                    launch_sound.play()

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

            launch_bubble, new_bubble, score = stop_bubble(bubble_array, new_bubble, launch_bubble, score, pop_sound)

            final_bubble_list = []
            for row in range(len(bubble_array)):
                for column in range(len(bubble_array[0])):
                    if bubble_array[row][column] is not None:
                        final_bubble_list.append(bubble_array[row][column])
                        if bubble_array[row][column].rect.bottom > (WINDOW_HEIGHT - arrow.rect.height - 10):
                            end('lose', score.total)
                            return

            if len(final_bubble_list) == 0:
                end('win', score.total)
                return

            game_color_list = update_color_list(bubble_array)
            random.shuffle(game_color_list)

            if not launch_bubble:
                move_counter += 1
                next_bubble = Bubble(game_color_list[0])
                next_bubble.rect.right = WINDOW_WIDTH - 5
                next_bubble.rect.bottom = WINDOW_HEIGHT - 5

            if difficulty == 'hard':
                move_counter, bubble_array = move_bubbles_down(move_counter, bubble_array, game_color_list)

        next_bubble.draw()
        if launch_bubble:
            cover_next_bubble()

        arrow.update(direction)
        arrow.draw()
        score.draw()
        DISPLAY_SURF.blit(difficulty_text, text_rect)

        set_array_pos(bubble_array)
        draw_bubble_array(bubble_array)

        pygame.display.update()
        clock.tick(100)


def difficulty_selection():
    pygame.init()

    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.init()
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play(-1)

    while True:
        DISPLAY_SURF.blit(background_image, (0, 0))

        font = pygame.font.SysFont('comicsansms', 40)
        text = font.render('Choose Difficulty:', True, BLACK)
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3 + 50))
        DISPLAY_SURF.blit(text, text_rect)

        button_font = pygame.font.SysFont('comicsansms', 30)
        easy_button = button_font.render('Easy', True, BLACK)
        easy_rect = easy_button.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50))

        hard_button = button_font.render('Hard', True, BLACK)
        hard_rect = hard_button.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.5 + 50))

        DISPLAY_SURF.blit(easy_button, easy_rect)
        DISPLAY_SURF.blit(hard_button, hard_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(mouse_pos):
                    return 'easy'
                elif hard_rect.collidepoint(mouse_pos):
                    return 'hard'


def end(status, score):
    pygame.init()

    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.init()
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play(-1)

    while True:
        DISPLAY_SURF.blit(background_image, (0, 0))

        font = pygame.font.SysFont('comicsansms', 40)
        if status == 'lose':
            text1 = font.render(f'You lost :(. Score: {score}.', True, BLACK)
        else:
            text1 = font.render(f'You won!!! Score: {score}.', True, BLACK)
        text1_rect = text1.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3 + 90))
        DISPLAY_SURF.blit(text1, text1_rect)

        text2 = font.render('Do you want to play again?', True, BLACK)
        text2_rect = text2.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        DISPLAY_SURF.blit(text2, text2_rect)

        button_font = pygame.font.SysFont('comicsansms', 30)
        play_again = button_font.render('PLAY', True, BLACK)
        play_rect = play_again.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100))

        DISPLAY_SURF.blit(play_again, play_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    pygame.mixer.music.stop()
                    main()
                    return


def main():
    global DISPLAY_SURF, DISPLAY_RECT
    pygame.init()
    pygame.display.set_caption('Bubble Buster')
    pygame.font.SysFont('Helvetica', TEXT_HEIGHT)
    DISPLAY_SURF, DISPLAY_RECT = make_display()
    chosen_difficulty = difficulty_selection()
    pygame.mixer.music.stop()

    while True:
        run(chosen_difficulty)


if __name__ == "__main__":
    main()
