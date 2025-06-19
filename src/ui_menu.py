# src/ui_menu.py

import pygame
from lang import _, set_lang, LANGS

def tela_inicial(screen, highscore):
    font_big = pygame.font.SysFont(None, 72)
    font_mid = pygame.font.SysFont(None, 42)
    font_small = pygame.font.SysFont(None, 32)
    idioma_idx = LANGS.index("pt")  # Começa em português

    def render_menu():
        screen.fill((15, 15, 25))
        title = font_big.render(_("title"), True, (255, 215, 0))
        rec = font_mid.render(f"{_('record')}: {highscore}", True, (255, 255, 0))
        controls = [
            _("controls"),
            _("move_keys"),
            _("restart_key"),
            _("quit_key"),
            _("pause_key"),
            f"{_('menu_lang')}: {LANGS[idioma_idx].upper()}  [{_('press_L_to_change')}]"
        ]
        y = screen.get_height() // 2 - 80
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, y)))
        y += 70
        screen.blit(rec, rec.get_rect(center=(screen.get_width() // 2, y)))
        y += 50
        for ctrl in controls:
            ctrl_txt = font_small.render(ctrl, True, (220, 220, 220))
            screen.blit(ctrl_txt, ctrl_txt.get_rect(center=(screen.get_width() // 2, y)))
            y += 35
        # Mensagem sobre a loja (tecla B), já traduzida
        loja_msg = font_small.render(_("shop_menu_hint"), True, (255, 230, 80))
        screen.blit(loja_msg, loja_msg.get_rect(center=(screen.get_width() // 2, y + 10)))
        instr = font_small.render(_("press_any_key"), True, (180, 180, 255))
        screen.blit(instr, instr.get_rect(center=(screen.get_width() // 2, screen.get_height() - 60)))
        pygame.display.flip()

    render_menu()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    idioma_idx = (idioma_idx + 1) % len(LANGS)
                    set_lang(LANGS[idioma_idx])
                    render_menu()
                else:
                    waiting = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
