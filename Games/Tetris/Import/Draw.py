import pygame
import Import.Variable as Var


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (Var.TOP_LEFT_X + Var.PLAY_WIDTH / 2 - (label.get_width() / 2),
                         Var.TOP_LEFT_Y + Var.PLAY_HEIGHT / 2 - label.get_height() / 2))


def draw_grid(surface, grid):
    sx = Var.TOP_LEFT_X
    sy = Var.TOP_LEFT_Y
    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * Var.BLOCK_SIZE),
                         (sx + Var.PLAY_WIDTH, sy + i * Var.BLOCK_SIZE))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * Var.BLOCK_SIZE, sy),
                             (sx + j * Var.BLOCK_SIZE, sy + Var.PLAY_HEIGHT))


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = Var.TOP_LEFT_X + Var.PLAY_WIDTH + 50
    sy = Var.TOP_LEFT_Y + Var.PLAY_HEIGHT / 2 - 100

    pygame.draw.rect(surface, (255, 255, 255), (sx, sy - 10, 150, 150), 5)

    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '1':
                pygame.draw.rect(surface, shape.color,
                                 (sx + j * Var.BLOCK_SIZE, sy + i * Var.BLOCK_SIZE, Var.BLOCK_SIZE, Var.BLOCK_SIZE), 0)

    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (Var.TOP_LEFT_X + Var.PLAY_WIDTH / 2 - (label.get_width() / 2), Var.BLOCK_SIZE))

    # Current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))

    sx = Var.TOP_LEFT_X + Var.PLAY_WIDTH + 50
    sy = Var.TOP_LEFT_Y + Var.PLAY_HEIGHT / 2 - 100

    surface.blit(label, (sx + 20, sy + 160))
    # Last score
    label = font.render('High Score: ' + str(last_score), 1, (255, 255, 255))

    sx = Var.TOP_LEFT_X - 200
    sy = Var.TOP_LEFT_Y + 200

    surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (
            Var.TOP_LEFT_X + j * Var.BLOCK_SIZE, Var.TOP_LEFT_Y + i * Var.BLOCK_SIZE, Var.BLOCK_SIZE, Var.BLOCK_SIZE),
                             0)

    pygame.draw.rect(surface, (255, 0, 0), (Var.TOP_LEFT_X, Var.TOP_LEFT_Y, Var.PLAY_WIDTH, Var.PLAY_HEIGHT), 5)
    draw_grid(surface, grid)
    # pygame.display.update()
