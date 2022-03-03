import pygame
from boardGame.variables import RED, WHITE, BLUE, SQUARE_SIZE
from boardGame.board import Board
from MiniMax.minimaxAlgorithm import minimax
class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.x = 2
        self.y = 2

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col, self.board)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col,board):

        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            board.moveCount = board.moveCount +1
            print("move Count: ", board.moveCount)
            if self.board.white_left >= 2:
                self.x = self.x-1
            else:
                self.x = self.x-2
            if self.x == 0:
                self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
            self.x = 2
            self.y = 2

        elif self.turn == WHITE:
            self.turn = RED
            self.x = 2
            self.y = 2


    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        board.moveCount = board.moveCount +1
        print("move Count: ", board.moveCount)
        if self.board.white_left >= 2:
            self.y = self.y - 1
        elif self.board.white_left < 2:
            self.y = self.y - 2
        if self.y==0:
            self.change_turn()