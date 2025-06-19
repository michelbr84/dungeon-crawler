# src/ui.py

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
        # Mensagem do botão B para abrir a loja
        loja_msg = font_small.render(_("shop_press_b"), True, (255, 230, 80))
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

def exibir_hud(screen, font, player, andar, score, highscore, desafio, desafio_status, medalha_nova=None):
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
        f"{_('challenge')}: {_(desafio_nome_key)}", True, (0, 255, 128) if desafio.get("cumprido") else (255, 255, 255)
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

# ----------------------------
# LOJA SIMPLES - SHOP SCREEN
# ----------------------------
def tela_loja(screen, font, player):
    itens = [
        {"nome": "Cura +1", "preco": 3, "efeito": "cura"},
        {"nome": "Vida Máx +1", "preco": 5, "efeito": "max_hp"},
        {"nome": "Invulnerável (10 turnos)", "preco": 4, "efeito": "invuln"},
    ]
    selecionado = 0
    rodando = True

    while rodando:
        screen.fill((30, 20, 10))
        titulo = font.render("LOJA", True, (255, 255, 0))
        screen.blit(titulo, (screen.get_width() // 2 - titulo.get_width() // 2, 40))
        texto_moedas = font.render(f"Moedas: {player.coins}", True, (255, 215, 0))
        screen.blit(texto_moedas, (screen.get_width() // 2 - texto_moedas.get_width() // 2, 80))
        for idx, item in enumerate(itens):
            cor = (255, 255, 255)
            if idx == selecionado:
                cor = (0, 255, 100)
            item_txt = font.render(f"{item['nome']} - {item['preco']} $", True, cor)
            screen.blit(item_txt, (screen.get_width() // 2 - item_txt.get_width() // 2, 140 + idx * 50))

        instru = font.render("Enter: comprar  |  Esc: sair  |  cima/baixo", True, (180, 180, 200))
        screen.blit(instru, (screen.get_width() // 2 - instru.get_width() // 2, 320))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selecionado > 0:
                    selecionado -= 1
                elif event.key == pygame.K_DOWN and selecionado < len(itens) - 1:
                    selecionado += 1
                elif event.key == pygame.K_ESCAPE:
                    rodando = False
                elif event.key == pygame.K_RETURN:
                    item = itens[selecionado]
                    if player.coins >= item["preco"]:
                        player.coins -= item["preco"]
                        if item["efeito"] == "cura":
                            player.hp = min(player.max_hp, player.hp + 1)
                        elif item["efeito"] == "max_hp":
                            player.max_hp += 1
                            player.hp = player.max_hp
                        elif item["efeito"] == "invuln":
                            player.invulnerable_timer = 100
                    else:
                        aviso = font.render("Sem moedas suficientes!", True, (255, 50, 50))
                        screen.blit(aviso, (screen.get_width() // 2 - aviso.get_width() // 2, 380))
                        pygame.display.flip()
                        pygame.time.delay(800)
# fim do arquivo
