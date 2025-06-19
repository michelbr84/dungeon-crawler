# src/item.py

import random
from config import TILE_SIZE

ITEM_HEALTH = "health"
ITEM_TREASURE = "treasure"

ITEMS_DEFS = {
    ITEM_HEALTH: {
        "color": (0, 220, 0),     # Verde
        "amount": 1               # Quantidade de cura
    },
    ITEM_TREASURE: {
        "color": (255, 215, 0),   # Amarelo ouro
        "amount": 1               # Pontos
    }
}

class Item:
    def __init__(self, item_type, x, y):
        self.type = item_type
        self.x = x
        self.y = y
        self.color = ITEMS_DEFS[item_type]["color"]

    def draw(self, surface):
        import pygame
        center = (self.x * TILE_SIZE + TILE_SIZE//2, self.y * TILE_SIZE + TILE_SIZE//2)
        radius = TILE_SIZE // 3
        pygame.draw.circle(surface, self.color, center, radius)

def spawn_items(dungeon_map, quantity_health=1, quantity_treasure=2):
    items = []
    height = len(dungeon_map)
    width = len(dungeon_map[0])

    # Coleta todos os tiles de chão livres
    floor_positions = [(x, y) for y in range(height) for x in range(width) if dungeon_map[y][x] == 1]

    # Evita tentar spawnar mais itens que espaços livres
    random.shuffle(floor_positions)
    idx = 0

    # Itens de cura
    for _ in range(quantity_health):
        if idx < len(floor_positions):
            x, y = floor_positions[idx]
            items.append(Item(ITEM_HEALTH, x, y))
            idx += 1

    # Tesouros
    for _ in range(quantity_treasure):
        if idx < len(floor_positions):
            x, y = floor_positions[idx]
            items.append(Item(ITEM_TREASURE, x, y))
            idx += 1

    return items
