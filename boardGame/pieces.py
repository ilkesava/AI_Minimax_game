from .variables import RED, WHITE, SQUARE_SIZE, GREY
import pygame

class Pieces:
    DOLGU = 15
    OUTLINE = 2

    def __init__(self, row, col, color, moved):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calculate_position()
        self.moved = False

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.DOLGU
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):

        self.row = row
        self.col = col
        self.calculate_position()