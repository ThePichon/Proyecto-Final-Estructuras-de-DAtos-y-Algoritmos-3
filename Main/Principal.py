import pygame
import Juego
import Bot_Random
import Heurísitica
import Bot
import random


# Configuración de Pygame
def initialize_pygame():
    print("Inicializando Pygame...")
    pygame.init()
    SIZE = 5
    CELL_SIZE = 100
    WINDOW_SIZE = SIZE * CELL_SIZE
    LINE_COLOR = (0, 0, 0)
    PLAYER_COLORS = {
        1: (255, 0, 0),
        2: (0, 0, 255),
    }  # Asegura que el jugador 2 tenga un color visible

    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Quixo")
    print("Pygame inicializado correctamente.")
    return window, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS


def draw_board(window, board, SIZE, CELL_SIZE, LINE_COLOR, PLAYER_COLORS):
    window.fill((255, 255, 255))
    for x in range(SIZE):
        for y in range(SIZE):
            color = PLAYER_COLORS.get(board[x][y], (200, 200, 200))
            pygame.draw.rect(
                window, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(
                window,
                LINE_COLOR,
                (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                1,
            )
    pygame.display.update()
