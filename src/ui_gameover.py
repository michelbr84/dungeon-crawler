# src/ui_gameover.py

import pygame
from lang import _

def tela_game_over(screen, font, score, andar, highscore, novo_recorde, desafio, medalhas_obtidas):
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    screen.fill((10, 10, 10))
    msg = font_big.render(_("game_over"), True, (200, 50, 50))
    pont = font_small.render(f"{_('score')}: {score} | {_('floor')}: {andar}", True, (220, 220, 220))
    rec = font_small.render(f"{_('record')}: {highscore}", True, (255, 255, 0))
    sub = font_small.render(_("[R]estart [Q]uit"), True, (220, 220, 220))
    rect = msg.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
    pontrect = pont.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    recrect = rec.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 10))
    subrect = sub.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 70))
    screen.blit(msg, rect)
    screen.blit(pont, pontrect)
    screen.blit(rec, recrect)
    screen.blit(sub, subrect)
    if novo_recorde:
        nrec = font_small.render(_("new_highscore"), True, (0, 255, 0))
        nrecrect = nrec.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
        screen.blit(nrec, nrecrect)
    # Desafio (usa chave i18n)
    desafio_font = pygame.font.SysFont(None, 28)
    desafio_nome_key = desafio.get('nome', '')
    desafio_msg = f"{_('challenge')}: {_(desafio_nome_key)} - {(_('completed') if desafio.get('cumprido') else _('failed'))}"
    desafio_col = (0, 255, 0) if desafio.get("cumprido") else (255, 100, 100)
    desafio_txt = desafio_font.render(desafio_msg, True, desafio_col)
    desafio_rect = desafio_txt.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 110))
    screen.blit(desafio_txt, desafio_rect)
    # Medalhas (usa chave i18n)
    if medalhas_obtidas:
        medalha_titulo = desafio_font.render(_("medals") + ":", True, (255, 255, 0))
        mrect = medalha_titulo.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 145))
        screen.blit(medalha_titulo, mrect)
        y = screen.get_height() // 2 + 165
        for key in medalhas_obtidas:
            mkey = key if key.startswith("medal_") else "medal_" + key
            m_txt = desafio_font.render(_(mkey), True, (200, 200, 255))
            mrect = m_txt.get_rect(center=(screen.get_width() // 2, y))
            screen.blit(m_txt, mrect)
            y += 28
    pygame.display.flip()

    waiting = True
    action = None
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = "quit"
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    action = "restart"
                    waiting = False
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    action = "quit"
                    waiting = False
    return action
