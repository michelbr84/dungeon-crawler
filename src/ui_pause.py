# src/ui_pause.py

import pygame
from lang import _

def tela_pause(screen):
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    screen.fill((25, 25, 40))
    pause_msg = font_big.render(_("paused"), True, (200, 200, 255))
    instr1 = font_small.render(_("[R]eturn [Q]uit"), True, (220, 220, 220))
    instr2 = font_small.render(_("pause_key"), True, (180, 180, 255))
    rect = pause_msg.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 30))
    rect2 = instr1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
    rect3 = instr2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 70))
    screen.blit(pause_msg, rect)
    screen.blit(instr1, rect2)
    screen.blit(instr2, rect3)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r or event.key == pygame.K_ESCAPE:
                    return "resume"
                elif event.key == pygame.K_q:
                    return "quit"
