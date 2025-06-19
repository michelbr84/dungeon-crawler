# src/ui_hud.py

import pygame
from lang import _

def exibir_hud(screen, font, player, andar, score, highscore, desafio, desafio_status, medalha_nova=None):
    # HUD fixa à esquerda
    hp_text = font.render(f"{_('life')}: {player.hp}", True, (255, 255, 255))
    andar_text = font.render(f"{_('floor')}: {andar}", True, (255, 255, 0))
    score_text = font.render(f"{_('score')}: {score}", True, (255, 215, 0))
    hs_text = font.render(f"{_('record')}: {highscore}", True, (255, 255, 0))
    coin_text = font.render(f"$ {getattr(player, 'coins', 0)}", True, (255, 215, 0))

    screen.blit(hp_text, (10, 10))
    screen.blit(andar_text, (10, 50))
    screen.blit(score_text, (10, 90))
    screen.blit(hs_text, (10, 130))
    screen.blit(coin_text, (10, 170))

    # Desafio centralizado na parte inferior (usa chave i18n)
    font_small = pygame.font.SysFont(None, 30)
    desafio_nome_key = desafio.get('nome', '')
    desafio_text = font_small.render(
        f"{_('challenge')}: {_(desafio_nome_key)}", True,
        (0, 255, 128) if desafio.get("cumprido") else (255, 255, 255)
    )
    progresso_text = font_small.render(str(desafio_status) if desafio_status else "", True, (200, 200, 200))
    w, h = screen.get_size()
    desafio_rect = desafio_text.get_rect(center=(w // 2, h - 60))
    progresso_rect = progresso_text.get_rect(center=(w // 2, h - 30))
    screen.blit(desafio_text, desafio_rect)
    screen.blit(progresso_text, progresso_rect)

    # Notificação de medalha nova (se houver)
    if medalha_nova:
        font_big = pygame.font.SysFont(None, 48)
        txt = font_big.render(_("medal_achieved"), True, (255, 215, 0))
        rect = txt.get_rect(center=(w // 2, h // 2 - 100))
        screen.blit(txt, rect)
        nome = font_big.render(str(medalha_nova), True, (255, 255, 255))
        nrect = nome.get_rect(center=(w // 2, h // 2 - 60))
        screen.blit(nome, nrect)
