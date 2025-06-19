# src/ui_shop.py

import pygame
from lang import _

def tela_loja(screen, font, player):
    itens = [
        {"nome": _("shop_item_heal"), "preco": 3, "efeito": "cura"},
        {"nome": _("shop_item_maxhp"), "preco": 5, "efeito": "max_hp"},
        {"nome": _("shop_item_invuln"), "preco": 4, "efeito": "invuln"},
    ]
    selecionado = 0
    rodando = True
    mensagem = ""     # Mensagem exibida após compra/venda
    mensagem_tipo = "" # "ok" ou "erro"
    mensagem_timer = 0

    while rodando:
        screen.fill((30, 20, 10))
        # Título
        titulo = font.render(_("shop_title"), True, (255, 255, 0))
        screen.blit(titulo, (screen.get_width() // 2 - titulo.get_width() // 2, 40))
        # Quantidade de moedas
        texto_moedas = font.render(f"{_('coins')}: {player.coins}", True, (255, 215, 0))
        screen.blit(texto_moedas, (screen.get_width() // 2 - texto_moedas.get_width() // 2, 80))
        # Itens da loja
        for idx, item in enumerate(itens):
            cor = (255, 255, 255)
            if idx == selecionado:
                cor = (0, 255, 100)
            item_txt = font.render(f"{item['nome']} - {item['preco']} $", True, cor)
            screen.blit(item_txt, (screen.get_width() // 2 - item_txt.get_width() // 2, 140 + idx * 50))

        # Instruções
        instru = font.render(_("shop_controls"), True, (180, 180, 200))
        screen.blit(instru, (screen.get_width() // 2 - instru.get_width() // 2, 320))

        # Mensagem de feedback (compra/venda)
        if mensagem:
            cor = (0, 255, 120) if mensagem_tipo == "ok" else (255, 50, 50)
            aviso = font.render(mensagem, True, cor)
            screen.blit(aviso, (screen.get_width() // 2 - aviso.get_width() // 2, 370))

        pygame.display.flip()

        # Timer para mensagem sumir após ~1 segundo
        if mensagem_timer > 0:
            mensagem_timer -= 1
            if mensagem_timer == 0:
                mensagem = ""
                mensagem_tipo = ""

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
                            mensagem = _("shop_buy_ok_heal")
                        elif item["efeito"] == "max_hp":
                            player.max_hp += 1
                            player.hp = player.max_hp
                            mensagem = _("shop_buy_ok_maxhp")
                        elif item["efeito"] == "invuln":
                            player.invulnerable_timer = 100
                            mensagem = _("shop_buy_ok_invuln")
                        mensagem_tipo = "ok"
                    else:
                        mensagem = _("shop_buy_fail_coins")
                        mensagem_tipo = "erro"
                    mensagem_timer = 60  # 1 segundo se FPS=60

# Fim do arquivo
