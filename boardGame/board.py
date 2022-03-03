import pygame
from .variables import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .pieces import Pieces

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 4
        self.red_destroyed = self.white_destroyed = 0
        self.create_board()
        self.moveCount = 0

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def maxEval(self) :
        return self.red_left - self.white_left + self.white_destroyed * 0.5 - self.red_destroyed * 0.5

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

        piece.move(row, col)

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c]
                if turn != 0:
                    if turn.color == RED:
                        if c == 0:  ##en sol duvar üçgen için
                            if r == 0:
                                if self.board[r + 1][c] != 0:
                                    if self.board[r + 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0: #ikili yok etme sol üst aşağı doğru
                                    if self.board[r + 1][c].color == RED and self.board[r + 2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r+1][c])
                                        self.red_destroyed = self.red_destroyed + 2
                                if self.board[r][c+1] != 0:
                                    if self.board[r][c+1] == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r][c+1] != 0 and self.board[r][c+2] != 0: #ikili yok etme sol üst sağa doğru
                                    if self.board[r][c+1].color == RED and self.board[r][c + 2].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c + 1])
                                        self.red_destroyed = self.red_destroyed + 2
                            if r == 6:
                                if self.board[r - 1][c] != 0:
                                    if self.board[r - 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r - 1][c] != 0 and self.board[r - 2][c] != 0: #ikili yok etme sol alt yukarı doğru
                                    if self.board[r - 1][c].color == RED and self.board[r-2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r-1][c])
                                        self.red_destroyed = self.red_destroyed + 2

                                if self.board[r][c+1] != 0:
                                    if self.board[r][c+1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r][c+1] != 0 and self.board[r][c+2] != 0: #ikili yok etme sol alt sağa doğru
                                    if self.board[r][c+1].color == RED and self.board[r][c+2].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c+1])
                                        self.red_destroyed = self.red_destroyed + 2

                            elif 1 <= r <= 5:
                                if self.board[r][c+1] != 0:
                                    if self.board[r][c + 1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r][c + 1] != 0 and self.board[r][c + 2] != 0:  # ikili yok etme c=0 en sol column 1-5 arası row
                                    if self.board[r][c + 1].color == RED and self.board[r][c + 2].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c+1])
                                        self.red_destroyed = self.red_destroyed + 2
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0:
                                    if self.board[r - 1][c].color == WHITE and self.board[r + 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1


                        elif c == 6:  ##en sağ duvar üçgen için
                            if r == 0:
                                if self.board[r + 1][c] != 0:
                                    if self.board[r + 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r + 1][c] != 0 and self.board[r+2][c] != 0: #ikili yok etme sağ üst aşağı doğru
                                    if self.board[r + 1][c].color == RED and self.board[r+2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r+1][c])
                                        self.red_destroyed = self.red_destroyed + 2
                                if self.board[r][c-1] != 0:
                                    if self.board[r][c-1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r][c-1] != 0 and self.board[r][c-2] != 0: #ikili yok etme sağ üst aşağı doğru
                                    if self.board[r][c - 1].color == RED and self.board[r][c-2].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c-1])
                                        self.red_destroyed = self.red_destroyed + 2

                            if r == 6:
                                if self.board[r-1][c] != 0:
                                    if self.board[r - 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r-1][c] != 0 and self.board[r-2][c] != 0: #ikili yok etme sağ alt yukarı doğru
                                    if self.board[r-1][c].color == RED and self.board[r-2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r-1][c])
                                        self.red_destroyed = self.red_destroyed + 2

                                if self.board[r][c-1] != 0:
                                    if self.board[r][c-1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r][c-1] != 0 and self.board[r][c-2] != 0: #ikili yok etme sağ alt sola doğru
                                    if self.board[r][c-1].color == RED and  self.board[r][c-2].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c-1])
                                        self.red_destroyed = self.red_destroyed + 2
                            elif 1 <= r <= 5:
                                if self.board[r ][c-1] != 0:
                                    if self.board[r][c - 1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r ][c-1] != 0 and self.board[r ][c-2] != 0:#ikili yok etme sağ column sola doğru
                                    if self.board[r][c - 1].color == RED and self.board[r][c - 2].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c-1])
                                        self.red_destroyed = self.red_destroyed + 2
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0:
                                    if self.board[r - 1][c].color == WHITE and self.board[r + 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1


                        elif r == 0:  ##en üst duvar red için
                            if 1 <= c <= 5:
                                if self.board[r + 1][c] != 0:
                                    if self.board[r + 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0: #ikili yok etme üst row aşağı doğru
                                    if self.board[r + 1][c].color == RED and self.board[r + 2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r+1][c])
                                        self.red_destroyed = self.red_destroyed + 2
                                if self.board[r][c+1] != 0 and self.board[r][c-1] != 0:
                                    if self.board[r][c + 1].color == WHITE and self.board[r][c - 1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1

                        elif r == 6:  ##en alt duvar red için
                            if 1 <= c <= 5:
                                if self.board[r - 1][c] != 0:
                                    if self.board[r - 1][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1
                                if self.board[r - 1][c] != 0 and self.board[r - 2][c] != 0:#ikili yok etme alt row yukarı doğru
                                    if self.board[r - 1][c].color == RED and self.board[r - 2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r - 1][c])
                                        self.red_destroyed = self.red_destroyed + 2
                                if self.board[r][c-1] != 0 and self.board[r][c+1] != 0:
                                    if self.board[r][c+1].color == WHITE and self.board[r][c-1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.red_destroyed = self.red_destroyed + 1


                        elif 0 < r < 6 and 0 < c < 6:  ##ortadaki red için
                            if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0:
                                if self.board[r - 1][c].color == WHITE and self.board[r + 1][c].color == WHITE:
                                    self.remove(self.board[r][c])
                                    self.red_destroyed = self.red_destroyed + 1
                            if 0 < r <= 4:
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0: #ikili yok etme ortada rowlar ile
                                    if self.board[r - 1][c].color == WHITE and self.board[r + 1][c].color == RED and self.board[r + 2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r+1][c])
                                        self.red_destroyed = self.red_destroyed + 2
                            if 1 < r <=5:
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0 and self.board[r - 2][c] != 0: #ikili yok etme ortada rowlar ile
                                    if self.board[r - 1][c].color == RED and self.board[r + 1][c].color == WHITE and self.board[r - 2][c].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r - 1][c])
                                        self.red_destroyed = self.red_destroyed + 2
                            if self.board[r ][c-1] != 0 and self.board[r][c+1] != 0:
                                if self.board[r][c - 1].color == WHITE and self.board[r][c + 1].color == WHITE:
                                    self.remove(self.board[r][c])
                                    self.red_destroyed = self.red_destroyed + 1
                            if 0 < c <= 4:
                                if self.board[r ][c-1] != 0 and self.board[r][c+1] != 0 and self.board[r ][c+2] != 0:#ikili yok etme ortada collar ile
                                    if self.board[r][c - 1].color == WHITE and self.board[r][c + 2].color == WHITE and self.board[r][c + 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c+1])
                                        self.red_destroyed = self.red_destroyed + 2
                            if 1 < c <= 5:
                                if self.board[r ][c-1] != 0 and self.board[r][c+1] != 0 and self.board[r ][c-2] != 0:#ikili yok etme ortada collar ile
                                    if self.board[r][c - 1].color == RED and self.board[r][c - 2].color == WHITE and self.board[r][c + 1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c-1])
                                        self.red_destroyed = self.red_destroyed + 2

                    elif turn.color == WHITE:
                        if c == 0:  ##en sol duvar beyaz için
                            if r == 0:
                                if self.board[r + 1][c] != 0:
                                    if self.board[r + 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0: #ikili yok etme sol üst aşağı doğru
                                    if self.board[r + 1][c].color == WHITE and self.board[r + 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r+1][c])
                                        self.white_destroyed = self.white_destroyed + 2
                                if self.board[r ][c+1] != 0:
                                    if self.board[r][c + 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r][c + 1] != 0 and self.board[r][c + 2] != 0:  # ikili yok etme sol üst sağa doğru
                                    if self.board[r][c + 1].color == WHITE and self.board[r][c + 2].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c + 1])
                                        self.white_destroyed = self.white_destroyed + 2
                            if r == 6:
                                if self.board[r - 1][c] != 0:
                                    if self.board[r - 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r - 1][c] != 0 and self.board[r - 2][c] != 0:  # ikili yok etme sol alt yukarı doğru
                                    if self.board[r - 1][c].color == WHITE and self.board[r - 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r - 1][c])
                                        self.white_destroyed = self.white_destroyed + 2

                                if self.board[r][c+1] != 0:
                                    if self.board[r][c + 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r][c + 1] != 0 and self.board[r][c + 2] != 0:  # ikili yok etme sol alt sağa doğru
                                    if self.board[r][c + 1].color == WHITE and self.board[r][c + 2].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c + 1])
                                        self.white_destroyed = self.white_destroyed + 2

                            elif 1 <= r <= 5:
                                if self.board[r][c+1] != 0:
                                    if self.board[r][c + 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r][c + 1] != 0 and self.board[r][c + 2] != 0:  # ikili yok etme c=0 en sol column 1-5 arası row
                                    if self.board[r][c + 1].color == WHITE and self.board[r][c + 2].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c + 1])
                                        self.white_destroyed = self.white_destroyed + 2
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0:
                                    if self.board[r - 1][c].color == RED and self.board[r + 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1


                        elif c == 6:  ##en sağ duvar beyaz için
                            if r == 0:
                                if self.board[r + 1][c] != 0:
                                    if self.board[r + 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0:  # ikili yok etme sağ üst aşağı doğru
                                    if self.board[r + 1][c].color == WHITE and self.board[r + 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r + 1][c])
                                        self.white_destroyed = self.white_destroyed + 2
                                if self.board[r][c-1] != 0:
                                    if self.board[r][c - 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r][c - 1] != 0 and self.board[r][c - 2] != 0:  # ikili yok etme sağ üst aşağı doğru
                                    if self.board[r][c - 1].color == WHITE and self.board[r][c - 2].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c - 1])
                                        self.white_destroyed = self.white_destroyed + 2
                            if r == 6:
                                if self.board[r - 1][c] != 0:
                                    if self.board[r - 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r - 1][c] != 0 and self.board[r - 2][c] != 0:  # ikili yok etme sağ alt yukarı doğru
                                    if self.board[r - 1][c].color == WHITE and self.board[r - 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r - 1][c])
                                        self.white_destroyed = self.white_destroyed + 2

                                if self.board[r][c-1] != 0:
                                    if self.board[r][c - 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r][c - 1] != 0 and self.board[r][c - 2] != 0:  # ikili yok etme sağ alt sola doğru
                                    if self.board[r][c - 1].color == WHITE and self.board[r][c - 2].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c - 1])
                                        self.white_destroyed = self.white_destroyed + 2
                            elif 1 <= r <= 5:
                                if self.board[r][c-1] != 0:
                                    if self.board[r][c - 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r][c - 1] != 0 and self.board[r][c - 2] != 0:  # ikili yok etme sağ column sola doğru
                                    if self.board[r][c - 1].color == WHITE and self.board[r][c - 2].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c - 1])
                                        self.white_destroyed = self.white_destroyed + 2
                                if self.board[r -1][c] != 0 and self.board[r + 1][c] != 0:
                                    if self.board[r - 1][c].color == RED and self.board[r + 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1


                        elif r == 0:  ##en üst duvar beyaz için
                            if 1 <= c <= 5:
                                if self.board[r + 1][c] != 0:
                                    if self.board[r + 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0:  # ikili yok etme üst row aşağı doğru
                                    if self.board[r + 1][c].color == WHITE and self.board[r + 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r + 1][c])
                                        self.white_destroyed = self.white_destroyed + 2
                                if self.board[r ][c +1] != 0 and self.board[r][c -1 ] != 0:
                                    if self.board[r][c + 1].color == RED and self.board[r][c - 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1

                        elif r == 6:  ##en alt duvar beyaz için
                            if 1 <= c <= 5:
                                if self.board[r - 1][c] != 0:
                                    if self.board[r - 1][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1
                                if self.board[r - 1][c] != 0 and self.board[r - 2][c] != 0:  # ikili yok etme alt row yukarı doğru
                                    if self.board[r - 1][c].color == WHITE and self.board[r - 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r - 1][c])
                                        self.white_destroyed = self.white_destroyed + 2
                                if self.board[r][c+1] != 0 and self.board[r][c-1] != 0:
                                    if self.board[r][c + 1].color == RED and self.board[r][c - 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.white_destroyed = self.white_destroyed + 1


                        elif 0 < r < 6 and 0 < c < 6:  ##ortadaki beyaz için
                            if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0:
                                if self.board[r - 1][c].color == RED and self.board[r + 1][c].color == RED:
                                    self.remove(self.board[r][c])
                                    self.white_destroyed = self.white_destroyed + 1
                            if 0 < r <= 4:
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0 and self.board[r + 2][c] != 0:  # ikili yok etme ortada rowlar ile
                                    if self.board[r - 1][c].color == RED and self.board[r + 1][c].color == WHITE and self.board[r + 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r + 1][c])
                                        self.white_destroyed = self.white_destroyed + 2
                            if 1 < r <= 5:
                                if self.board[r - 1][c] != 0 and self.board[r + 1][c] != 0 and self.board[r - 2][c] != 0:  # ikili yok etme ortada rowlar ile
                                    if self.board[r - 1][c].color == WHITE and self.board[r + 1][c].color == RED and self.board[r - 2][c].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r - 1][c])
                                        self.white_destroyed = self.white_destroyed + 2
                            if self.board[r][c-1] != 0 and self.board[r ][c+1] != 0:
                                if self.board[r][c-1].color == RED and self.board[r][c+1].color == RED:
                                    self.remove(self.board[r][c])
                                    self.white_destroyed = self.white_destroyed + 1
                            if 0 < c <= 4:
                                if self.board[r][c - 1] != 0 and self.board[r][c + 1] != 0 and self.board[r][c + 2] != 0:  # ikili yok etme ortada collar ile
                                    if self.board[r][c - 1].color == RED and self.board[r][c + 2].color == RED and self.board[r][c + 1].color == WHITE:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c + 1])
                                        self.white_destroyed = self.white_destroyed + 2

                            if 1 < c <= 5:
                                if self.board[r][c - 1] != 0 and self.board[r][c + 1] != 0 and self.board[r][c - 2] != 0:  # ikili yok etme ortada collar ile
                                    if self.board[r][c - 1].color == WHITE and self.board[r][c - 2].color == RED and self.board[r][c + 1].color == RED:
                                        self.remove(self.board[r][c])
                                        self.remove(self.board[r][c - 1])
                                        self.white_destroyed = self.white_destroyed + 2

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col == 0:
                    if row == 0 or row == 2:
                        self.board[row].append(Pieces(row, col, WHITE,moved=False))
                    elif row == 4 or row == 6:
                        self.board[row].append(Pieces(row, col, RED,moved=False))
                    else:
                        self.board[row].append(0)
                elif col == 6:
                    if row == 0 or row == 2 :
                        self.board[row].append(Pieces(row, col, RED,moved=False))
                    elif row == 6 or row == 4:
                        self.board[row].append(Pieces(row, col, WHITE,moved=False))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
            self.board[pieces.row][pieces.col] = 0
            if pieces != 0:
                if pieces.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            for i in range(4):
                print("WHITE WINS ")
                return WHITE
        elif self.white_left <= 0:
            for i in range(4):
                print("RED WINS ")
                return RED
        elif self.moveCount == 50:
            if self.red_left == self.white_left:
                print("DRAW")
                return True
            elif self.red_left > self.white_left:
                print("RED WINS ")
                return RED
            elif self.red_left < self.white_left:
                print("WHITE WINS ")
                return WHITE
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        up = piece.row-1
        down = piece.row+1
        col = piece.col
        if piece.color == RED and piece.moved == False:
            moves.update(self.go_left(row, row+1 , piece.color, left))
            moves.update(self.go_right(row , row+1, piece.color, right))
            moves.update(self.go_up(col,col+1,piece.color,up))
            moves.update(self.go_down(col,col+1,piece.color,down))
        if piece.color == WHITE and piece.moved == False:
            moves.update(self.go_left(row,row+1, piece.color, left))
            moves.update(self.go_right(row, row+1, piece.color, right))
            moves.update(self.go_up(col, col + 1, piece.color, up))
            moves.update(self.go_down(col, col + 1, piece.color, down))

        return moves

    def go_left(self, start,stop,color, left):
        moves = {}
        last = []
        for r in range(start, stop):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                moves[(r, left)] = last
        return moves



    def go_up(self, start,stop,color, up):
        moves = {}
        last = []
        for c in range(start, stop):
            if up < 0:
                break

            current = self.board[up][c]
            if current == 0:
                moves[(up, c)] = last
        return moves

    def go_down(self, start,stop,color, down,destroyed=[]):
        moves = {}
        last = []
        for c in range(start, stop):
            if down >= ROWS:
                break

            current = self.board[down][c]
            downeksi = self.board[down-1][c]
            if current == 0:
                moves[(down, c)] = last

        return moves

    def go_right(self, start, stop, color, right):
        moves = {}
        last = []
        for r in range(start, stop):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                moves[(r, right)] = last
        return moves