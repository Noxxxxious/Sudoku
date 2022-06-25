import pygame
import random
from Field import Field


class Sudoku:
    def __init__(self, window):
        self.h = 9
        self.w = 9
        self.board = [[Field(None, x, y, window.size / 9) for x in range(9)] for y in range(9)]
        self.window = window
        self.selected_field = self.board[4][4]

    def board_generator(self):
        for row in self.board:
            for field in row:
                field.set_digit(random.randint(1, 9))

    def draw(self):
        # drawing fields
        for row in self.board:
            for field in row:
                color = (40, 40, 40)
                if field == self.selected_field:
                    color = (70, 70, 70)
                elif field.get_x() == self.selected_field.get_x() or field.get_y() == self.selected_field.get_y():
                    color = (50, 50, 50)
                field.draw(self.window.surface, color)
        # drawing grid lines
        for i in range(8):
            x = y = (i + 1) * self.window.size / 9
            line_w = 2 if (i + 1) % 3 else 5
            pygame.draw.line(self.window.surface, (20, 20, 20), [x, 0], [x, self.window.size], line_w)
            pygame.draw.line(self.window.surface, (20, 20, 20), [0, y], [self.window.size, y], line_w)

    def click(self, mouse_pos):
        for row in self.board:
            for field in row:
                if field.get_x() < mouse_pos[0] < field.get_x() + field.get_size() and field.get_y() < mouse_pos[1] < field.get_y() + field.get_size():
                    self.selected_field = field

    def write(self, unicode):
        self.selected_field.set_digit(unicode)

    def remove(self):
        self.selected_field.set_digit(None)
