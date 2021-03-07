import os
import pygame
import random
import Import.Draw as Draw
import Import.Score as Score
import Import.Action as Act
import Import.Variable as Var
import Import.Validation as Val


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = Var.shape_colors[Var.shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                grid[i][j] = locked_pos[(j, i)]
    return grid


def get_shape():
    return Piece(5, 0, random.choice(Var.shapes))


def main(win):
    if not os.path.exists('scores.txt'):
        with open('scores.txt', 'w') as f:
            f.write('0')
    last_score = Score.max_score()
    locked_positions = {}
    # grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not Val.valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not Val.valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not Val.valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not Val.valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not Val.valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_pos = Act.convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += Act.clear_rows(grid, locked_positions) * 10

        Draw.draw_window(win, grid, score, last_score)
        Draw.draw_next_shape(next_piece, win)
        pygame.display.update()

        if Val.check_lost(locked_positions):
            Draw.draw_text_middle(win, 'YOU LOST!', 80, (255, 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            Score.update_score(score)


def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        Draw.draw_text_middle(win, 'Press Any Key To Play', 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()


def init():
    pygame.init()
    win = pygame.display.set_mode((Var.S_WIDTH, Var.S_HEIGHT))
    pygame.display.set_caption('Tetris')
    main_menu(win)
