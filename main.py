import pygame
import random
import shapes

from grid import Grid
from piece import Piece

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

def draw_text_middle(text, size, color, surface: pygame.Surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), s_height/2 - label.get_height()/2))

def draw_window(grid: Grid, surface: pygame.Surface):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(grid.row):
        for j in range(grid.column):
            pygame.draw.rect(surface, grid.grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)

    # draw grid and border
    draw_grid(grid, surface)

def draw_grid(grid: Grid, surface: pygame.Surface):
    sx = top_left_x
    sy = top_left_y
    for i in range(grid.row):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i * 30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(grid.column):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

def get_piece():
    shape = random.choice(shapes.list)
    color = shapes.colors[shapes.list.index(shape)]

    return Piece(5, 0, shape, color)

def main(surface: pygame.Surface):

    run = True
    change_piece = False
    current_piece = get_piece()
    next_piece = get_piece()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    score = 0

    grid = Grid(10, 20)

    while run:
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0

            grid.update(current_piece.get_positions(), (0,0,0))

            new_positions = current_piece.moveDown()

            if not(grid.check_position(new_positions)) and current_piece.y > 0:
                current_piece.moveUp()
                change_piece = True
                    

            grid.update(current_piece.get_positions(), current_piece.color)

        if change_piece == True:
            if grid.check_lost() == True:
                run = False

            completed_lines = grid.check_completed_lines()
            score += completed_lines * completed_lines * 20
            print(score)

            current_piece = next_piece
            next_piece = get_piece()
            change_piece = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    grid.update(current_piece.get_positions(), (0,0,0))
                    new_positions = current_piece.moveLeft()
                    if not(grid.check_position(new_positions)):
                        current_piece.moveRight()

                    grid.update(current_piece.get_positions(), current_piece.color)

                if event.key == pygame.K_RIGHT:
                    grid.update(current_piece.get_positions(), (0,0,0))
                    new_positions = current_piece.moveRight()
                    if not(grid.check_position(new_positions)):
                        current_piece.moveLeft()

                    grid.update(current_piece.get_positions(), current_piece.color)

                if event.key == pygame.K_DOWN:
                    grid.update(current_piece.get_positions(), (0,0,0))
                    new_positions = current_piece.moveDown()
                    if not(grid.check_position(new_positions)):
                        current_piece.moveUp()
                    
                    grid.update(current_piece.get_positions(), current_piece.color)

                if event.key == pygame.K_UP:
                    grid.update(current_piece.get_positions(), (0,0,0))
                    new_positions = current_piece.rotate()
                    grid.update(current_piece.get_positions(), current_piece.color)

        draw_window(grid, surface)
        pygame.display.update()

    draw_text_middle("You Lost", 40, (255,255,255), surface)
    pygame.display.update()
    pygame.time.delay(2000)

    

def main_menu():
    surface = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')

    run = True
    while run:
        surface.fill((0,0,0))
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main(surface)
    pygame.quit()
 

main_menu()  # start game