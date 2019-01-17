import pygame
from grid import Grid
from piece import Piece

class Window:
    def __init__(self, surface: pygame.Surface, width, height):
        self.surface = surface
        self.width = width
        self.height = height
        self.block_size = width // 10
        self.top_left_x = 100
        self.top_left_y = surface.get_height() - height

    def draw(self):
        self.surface.fill((0,0,0))
        # Tetris Title
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('TETRIS', 1, (255,255,255))

        self.surface.blit(label, (self.top_left_x + self.width / 2 - (label.get_width() / 2), self.block_size))

    def draw_grid(self, grid: Grid):
       
        #pieces
        for i in range(grid.row):
            for j in range(grid.column):
                rect = (
                    self.top_left_x + j * self.block_size,
                    self.top_left_y + i * self.block_size,
                    self.block_size,
                    self.block_size
                )
                pygame.draw.rect(self.surface, grid.grid[i][j], rect, 0)

        #lines
        for i in range(grid.row):
            # horizontal lines
            pygame.draw.line(
                self.surface, (128,128,128),
                (self.top_left_x, self.top_left_y + i * self.block_size),
                (self.top_left_x + self.width, self.top_left_y + i * self.block_size)
            )
            for j in range(grid.column):
                # vertical lines
                pygame.draw.line(
                    self.surface, (128,128,128),
                    (self.top_left_x + j * self.block_size, self.top_left_y),
                    (self.top_left_x + j * self.block_size, self.top_left_y + self.height)
                )

        #border
        pygame.draw.rect(self.surface, (255, 0, 0), (self.top_left_x, self.top_left_y, self.width, self.height), 5)

    def draw_score(self, score, lines, level):
        font = pygame.font.SysFont('comicsans', 60)
        label_score = font.render("Score "+str(score), 1, (255,255,255))
        label_line = font.render("Lines "+str(lines), 1, (255,255,255))
        label_level = font.render("Level "+str(level), 1, (255,255,255))

        self.surface.blit(label_score, (self.top_left_x*2 + self.width, self.top_left_y))
        self.surface.blit(label_line, (self.top_left_x*2 + self.width, self.top_left_y + 50))
        self.surface.blit(label_level, (self.top_left_x*2 + self.width, self.top_left_y + 100))

    def draw_next_piece(self, next_piece: Piece):
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render("Next Piece", 1, (255,255,255))
        self.surface.blit(label, (self.top_left_x*2 + self.width, self.top_left_y + 200))

        format = next_piece.shape[0]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    color = next_piece.color
                else:
                    color = (0,0,0)

                rect = (
                    self.top_left_x*2 + self.width + 30 + j * self.block_size,
                    self.top_left_y + 250 + i * self.block_size,
                    self.block_size,
                    self.block_size
                )
                pygame.draw.rect(self.surface, color, rect, 0)
