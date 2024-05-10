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
        pg.init()
        self.grid = ["" for _ in range(9)]
        self.turn = "X"

    def play(self):
        self.screen = pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pg.display.set_caption(SCREEN_TITLE)
        self.draw_grid()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            # This part sucks
            grid_index = self.get_mouse_input()
            if grid_index:
                if not self.grid[grid_index]:
                    self.grid[grid_index] = self.turn
                    win = self.check_win()
                    self.switch_turn()
                    self.draw_grid()
                    if win:
                        print(f"{self.turn} WINS!")
            pg.display.update()

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    def check_win(self):
        # https://www.reddit.com/r/learnpython/comments/v8bscr/comment/ibs9e6y/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
        return any(
            self.turn == self.grid[a] == self.grid[b] == self.grid[c]
            for a, b, c in [
                (0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6),
            ]
        )

    def get_mouse_input(self) -> int | None:
        """
        Gets the square number clicked by the user.

        Returns:
            int | None: Index of the clicked square in the grid array.
                None if a click does not happen inside the grid.
        """
        if pg.mouse.get_pressed()[0]:
            x, y = pg.mouse.get_pos()
            col, row = math.floor(x / SQR_SIZE), math.floor(y / SQR_SIZE)
            i = row * 3 + col
            if i in range(9):
                return i

    def draw_grid(self):
        self.screen.fill(BG_COLOR)

        for row in range(3):
            for col in range(3):
                sqr_rect = pg.Rect(col * SQR_SIZE, row * SQR_SIZE, SQR_SIZE, SQR_SIZE)
                sqr_value = self.grid[row * 3 + col]

                if sqr_value:
                    sqr_color = X_COLOR if sqr_value == "X" else O_COLOR
                    pg.draw.rect(self.screen, sqr_color, sqr_rect)

                pg.draw.rect(self.screen, GRID_COLOR, sqr_rect, width=3)


"""
OPTIONS:
    1. Draw the grid and its squares all in one function.
    2. Use one function to draw squares and another to draw grid lines.
"""
