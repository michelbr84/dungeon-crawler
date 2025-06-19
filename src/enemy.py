# src/enemy.py

import random
from config import COLOR_ENEMY, TILE_SIZE

class Enemy:
    def __init__(self, dungeon, enemy_type="random"):
        while True:
            x = random.randint(0, len(dungeon.map[0]) - 1)
            y = random.randint(0, len(dungeon.map) - 1)
            if dungeon.map[y][x] == 1:
                self.x = x
                self.y = y
                self.type = enemy_type
                self.color = (80, 80, 200) if enemy_type == "random" else (220, 40, 40)  # azul padrão, vermelho perseguidor
                break

    def move(self, dungeon, player):
        if self.type == "random":
            dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0), (0,0)])
        elif self.type == "chaser":
            dx = 0
            dy = 0
            if player.x > self.x:
                dx = 1
            elif player.x < self.x:
                dx = -1
            if player.y > self.y:
                dy = 1
            elif player.y < self.y:
                dy = -1
            # Prioridade: tenta mover no eixo x, se não der, tenta y
            # Move só em um eixo por turno
            if dx != 0 and self.can_move(self.x + dx, self.y, dungeon):
                dy = 0
            elif dy != 0 and self.can_move(self.x, self.y + dy, dungeon):
                dx = 0
            else:
                dx, dy = 0, 0
        new_x = self.x + dx
        new_y = self.y + dy
        if self.can_move(new_x, new_y, dungeon):
            self.x = new_x
            self.y = new_y

    def can_move(self, x, y, dungeon):
        return (0 <= x < len(dungeon.map[0]) and 0 <= y < len(dungeon.map) and dungeon.map[y][x] in (1, 2))

    def draw(self, surface):
        import pygame
        rect = (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(surface, self.color, rect)
