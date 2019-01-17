import pygame
import random
import shapes

from grid import Grid
from piece import Piece
from window import Window

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (surface.get_width()/2 - label.get_width()/2, surface.get_height()/2 - label.get_height()/2))

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
    fall_speed = 0.50

    score = 0
    lines = 0
    level = 1

    grid = Grid(10, 20)
    window = Window(surface, play_width, play_height)

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
            if grid.check_game_over() == True:
                run = False

            completed_lines = grid.check_completed_lines()
            lines += completed_lines
            score += level * completed_lines * completed_lines * 20
            if score > level * 100 and fall_speed > 0.05:
                level += 1
                fall_time -= 0.05

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
                    new_positions = current_piece.rotateRight()
                    if not(grid.check_position(new_positions)):
                        current_piece.rotateLeft()

                    grid.update(current_piece.get_positions(), current_piece.color)

        window.draw()
        window.draw_grid(grid)
        window.draw_score(score, lines, level)
        window.draw_next_piece(next_piece)
        pygame.display.update()

    draw_text_middle("Game Over", 40, (255,255,255), surface)
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