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

    def check_completed_lines(self):
        completed_line = 0

        for row in range(self.row):
            count_complete_column = 0
            for column in range(self.column):
                if self.grid[row][column] != (0,0,0):
                    count_complete_column += 1
            
            if count_complete_column == self.column:
                del self.grid[row]
                line = [(0,0,0) for x in range(self.column)]
                print(self.grid)
                self.grid.insert(0, line)
                print(self.grid)
                completed_line += 1

        return completed_line





