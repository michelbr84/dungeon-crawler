# src/player.py

from config import COLOR_PLAYER, TILE_SIZE

class Player:
    def __init__(self, dungeon):
        for y, row in enumerate(dungeon.map):
            for x, tile in enumerate(row):
                if tile == 1:  # TILE_FLOOR
                    self.max_hp = 3  # Vida máxima inicial
                    self.hp = self.max_hp
                    self.x = x
                    self.y = y
                    self.color = COLOR_PLAYER
                    self.invulnerable_timer = 0
                    self.coins = 0  # Agora o jogador tem moedas!
                    return

    def move(self, dx, dy, dungeon):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < len(dungeon.map[0]) and 0 <= new_y < len(dungeon.map):
            # Agora o jogador pode andar no chão OU na porta de saída
            if dungeon.map[new_y][new_x] in (1, 2):  # 1: TILE_FLOOR, 2: TILE_EXIT
                self.x = new_x
                self.y = new_y

    def draw(self, surface):
        import pygame
        rect = (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        # Se estiver invulnerável, pisca (só desenha metade dos frames)
        if self.invulnerable_timer == 0 or (self.invulnerable_timer // 3) % 2 == 0:
            color = self.color
        else:
            color = (255, 255, 0)  # Amarelo para piscar
        pygame.draw.rect(surface, color, rect)
