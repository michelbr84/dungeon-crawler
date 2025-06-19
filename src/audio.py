# src/audio.py

import pygame

pygame.mixer.init()
sound_powerup = pygame.mixer.Sound("assets/sounds/powerup.mp3")
sound_coin = pygame.mixer.Sound("assets/sounds/coin.mp3")
sound_hit = pygame.mixer.Sound("assets/sounds/hit.mp3")
sound_door = pygame.mixer.Sound("assets/sounds/door.mp3")
sound_gameover = pygame.mixer.Sound("assets/sounds/game-over.mp3")

def play_powerup():
    """Toca o som de powerup (cura)."""
    sound_powerup.play()

def play_coin():
    """Toca o som de moeda (tesouro)."""
    sound_coin.play()

def play_hit():
    """Toca o som de dano."""
    sound_hit.play()

def play_door():
    """Toca o som da porta (novo andar)."""
    sound_door.play()

def play_gameover():
    """Toca o som de game over."""
    sound_gameover.play()
