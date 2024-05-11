import math
import pygame as pg
from typing import Literal
import sys

pg.init()

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
    def __init__(self, starting_player: Literal["X", "O"] = "X") -> None:
        """
        Initializes tic-tac-toe game.
        """
        self.grid = ["" for _ in range(9)]
        self.player = starting_player

    def play(self) -> None:
        """
        Starts the game loop and plays the game.
        """
        # Screen is fixed size. Might add resizable window but it would require significant changes
        # to drawing code
        self.screen = pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pg.display.set_caption(SCREEN_TITLE)
        self.draw_grid()

        # GAME LOOP
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    sqr = self.get_clicked_square()
                    if sqr is not None and not self.grid[sqr]:
                        self.grid[sqr] = self.player
                        if self.check_win():
                            print(f"{self.player} WINS!")
                            return
                        elif self.check_draw():
                            print(f"IT'S A DRAW!")
                            return
                        self.switch_player()
            self.draw_grid()

    def get_clicked_square(self) -> int:
        """
        Gets the square number clicked by the user.

        Returns:
            int | None: Index of the clicked square in the grid array.
                None if a click does not happen inside the grid.
        """
        x, y = pg.mouse.get_pos()
        col, row = math.floor(x / SQR_SIZE), math.floor(y / SQR_SIZE)
        i = row * 3 + col
        if i in range(9):
            return i

    def switch_player(self) -> None:
        """
        Flips the turn of the game to the other player.
        """
        self.player = "O" if self.player == "X" else "X"

    def check_win(self) -> bool:
        """
        Determines if the current player has won.

        Returns:
            bool: True if the current player has one, false otherwise.
        """
        # https://www.reddit.com/r/learnpython/comments/v8bscr/comment/ibs9e6y/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
        return any(
            self.player == self.grid[a] == self.grid[b] == self.grid[c]
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

    def check_draw(self) -> bool:
        """
        Determines if the game has reached a draw.

        Returns:
            bool: True if it is draw (i.e. board is full). False otherwise.
        """
        return all(self.grid) and not self.check_win()

    def draw_grid(self) -> None:
        """
        Draws the tic-tac-toe grid to the screen.
        """
        self.screen.fill(BG_COLOR)

        for row in range(3):
            for col in range(3):
                sqr_rect = pg.Rect(col * SQR_SIZE, row * SQR_SIZE, SQR_SIZE, SQR_SIZE)
                sqr_value = self.grid[row * 3 + col]

                if sqr_value:
                    sqr_color = X_COLOR if sqr_value == "X" else O_COLOR
                    pg.draw.rect(self.screen, sqr_color, sqr_rect)

                pg.draw.rect(self.screen, GRID_COLOR, sqr_rect, width=3)
        pg.display.update()
