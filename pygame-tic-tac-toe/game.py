import math
import pygame as pg
import sys

# SCREEN
SCREEN_SIZE = 900
SQR_SIZE = SCREEN_SIZE / 3
SCREEN_TITLE = "Tic-Tac-Toe :D"


# COLORS
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)
GRID_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)


class TicTacToe:
    def __init__(self):
        self.grid = [
            ["X", "", ""],
            ["", "O", ""],
            ["", "", "X"],
        ]
        self.turn = "X"

    def play(self):
        self.screen = pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pg.display.set_caption(SCREEN_TITLE)

        while True:
            pg.init()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self._get_input()
            self._draw_grid()
            pg.display.update()

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    def _get_input(self):
        # ! TODO: Crashes for the indices being out of bounds sometimes
        if pg.mouse.get_pressed()[0]:
            x, y = pg.mouse.get_pos()
            row, col = math.floor(x / SQR_SIZE), math.floor(y / SQR_SIZE)
            if not (row in range(3) or col in range(3)):
                return
            if not self.grid[row][col]:
                self.grid[row][col] = self.turn
                self.switch_turn()

    def _draw_grid(self):
        self.screen.fill(BG_COLOR)

        for row in range(3):
            for col in range(3):
                sqr_rect = pg.Rect(col * SQR_SIZE, row * SQR_SIZE, SQR_SIZE, SQR_SIZE)
                sqr_value = self.grid[row][col]

                if sqr_value:
                    sqr_color = X_COLOR if sqr_value == "X" else O_COLOR
                    pg.draw.rect(self.screen, sqr_color, sqr_rect)

                pg.draw.rect(self.screen, GRID_COLOR, sqr_rect, width=3)


"""
OPTIONS:
    1. Draw the grid and its squares all in one function.
    2. Use one function to draw squares and another to draw grid lines.
"""
