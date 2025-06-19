# src/dungeon.py

import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE

MAP_WIDTH = SCREEN_WIDTH // TILE_SIZE
MAP_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

TILE_WALL = 0
TILE_FLOOR = 1
TILE_EXIT = 2  # Novo tipo de tile

class Dungeon:
    def __init__(self):
        self.map = [[TILE_WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.exit_pos = None  # Salva posição da porta de saída
        self.generate()

    def generate(self):
        # Drunkard Walk básico
        x, y = MAP_WIDTH // 2, MAP_HEIGHT // 2  # Ponto inicial
        self.map[y][x] = TILE_FLOOR
        floor_count = 1
        max_floor = (MAP_WIDTH * MAP_HEIGHT) // 3

        floor_positions = [(x, y)]  # Guarda todas as posições de chão

        while floor_count < max_floor:
            direction = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
            x = min(max(x + direction[0], 1), MAP_WIDTH - 2)
            y = min(max(y + direction[1], 1), MAP_HEIGHT - 2)
            if self.map[y][x] == TILE_WALL:
                self.map[y][x] = TILE_FLOOR
                floor_count += 1
                floor_positions.append((x, y))

        # Escolhe uma posição de chão distante para a porta de saída
        exit_x, exit_y = floor_positions[-1]  # Último tile criado
        self.map[exit_y][exit_x] = TILE_EXIT
        self.exit_pos = (exit_x, exit_y)

    def draw(self, surface, colors):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                rect = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if self.map[y][x] == TILE_WALL:
                    pygame.draw.rect(surface, colors['wall'], rect)
                elif self.map[y][x] == TILE_EXIT:
                    pygame.draw.rect(surface, colors['exit'], rect)
                else:
                    pygame.draw.rect(surface, colors['floor'], rect)
