import pygame
from piece import Piece

class Grid:

    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.grid = [[(0,0,0) for x in range(column)] for x in range(row)]

    def update(self, piece_positions, color):
        for position in piece_positions:
            column, row = position
            if row > -1:
                self.grid[row][column] = color

    def updateLockedPositions(self, locked_positions):
        for column in range(self.column):
            for row in range(self.row):
                if (row, column) in locked_positions:
                    color = locked_positions[(row, column)]
                    self.grid[row][column] = color


    def draw(self, surface: pygame.Surface, top_left_x, top_left_y, play_width, play_height):
        sx = top_left_x
        sy = top_left_y
        for i in range(self.row):
            pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
            for j in range(self.column):
                pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines

    def check_position(self, piece_positions):
        accepted_positions = [[(j, i) for j in range(self.column) if self.grid[i][j] == (0,0,0)] for i in range(self.row)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        for position in piece_positions:
            if position not in accepted_positions:
                if position[1] > -1:
                    return False

        return True

    def check_lost(self):
        for column in range(self.column):
            if self.grid[0][column] != (0,0,0):
                return True

        return False
