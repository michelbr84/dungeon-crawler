# src/particle.py

import pygame
import random
import math

class Particle:
    def __init__(self, x, y, color):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 3)
        self.x = x
        self.y = y
        self.radius = random.randint(3, 6)
        self.color = color
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.life = random.randint(12, 18)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.radius = max(1, self.radius - 0.2)
        self.life -= 1

    def draw(self, surface):
        if self.life > 0:
            alpha = max(50, int(255 * (self.life / 18)))
            surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), (self.radius, self.radius), int(self.radius))
            surface.blit(surf, (self.x - self.radius, self.y - self.radius))
