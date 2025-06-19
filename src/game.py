# src/game.py

import pygame
import sys
import os
import random

from config import SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, COLOR_BG, COLOR_WALL, COLOR_FLOOR, COLOR_EXIT, TILE_SIZE
from dungeon import Dungeon
from player import Player
from enemy import Enemy
from item import spawn_items, ITEM_HEALTH, ITEM_TREASURE
from ui_menu import tela_inicial
from ui_gameover import tela_game_over
from ui_hud import exibir_hud
from ui_pause import tela_pause
from ui_shop import tela_loja
from desafio import make_desafios, MEDALHAS
from particle import Particle
from lang import _

pygame.mixer.init()
sound_powerup = pygame.mixer.Sound("assets/sounds/powerup.mp3")
sound_coin = pygame.mixer.Sound("assets/sounds/coin.mp3")
sound_hit = pygame.mixer.Sound("assets/sounds/hit.mp3")
sound_door = pygame.mixer.Sound("assets/sounds/door.mp3")
sound_gameover = pygame.mixer.Sound("assets/sounds/game-over.mp3")

COLORS = {
    'wall': COLOR_WALL,
    'floor': COLOR_FLOOR,
    'exit': COLOR_EXIT
}

def load_highscore(filename="highscore.txt"):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                value = int(f.read())
                return value
        except:
            return 0
    return 0

def save_highscore(score, filename="highscore.txt"):
    try:
        with open(filename, "w") as f:
            f.write(str(score))
    except:
        pass

def criar_inimigos(dungeon, andar):
    enemies = []
    total = 2 + andar
    if andar >= 5:
        num_chaser = max(1, total // 3)
    else:
        num_chaser = 0
    num_random = total - num_chaser
    for i in range(num_chaser):
        enemies.append(Enemy(dungeon, enemy_type="chaser"))
    for i in range(num_random):
        enemies.append(Enemy(dungeon, enemy_type="random"))
    return enemies

class Game:
    def __init__(self):
        self.screen = None
        self.font = None
        self.clock = None
        self.highscore = load_highscore()
        self.medalhas_obtidas = set()
        self.medalha_nova = None
        self.medalha_nova_timer = 0
        self.shop_msg_timer = 0  # timer da mensagem automática da loja

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(_(WINDOW_TITLE))
        self.font = pygame.font.SysFont(None, 36)
        self.clock = pygame.time.Clock()
        tela_inicial(self.screen, self.highscore)
        self.medalhas_obtidas = set()
        while True:
            self.loop_jogo()

    def loop_jogo(self):
        andar = 1
        score = 0
        self.medalha_nova = None
        self.medalha_nova_timer = 0
        self.shop_msg_timer = 0
        dungeon = Dungeon()
        player = Player(dungeon)
        player.coins = 0
        enemies = criar_inimigos(dungeon, andar)
        items = spawn_items(dungeon.map, quantity_health=1, quantity_treasure=2)
        enemy_move_timer = 0

        desafios = make_desafios()
        desafio = random.choice(desafios)
        desafio["cumprido"] = False
        if "on_start" in desafio:
            desafio["on_start"](desafio, player, items=items)
        movimentos = 0
        andar_sem_dano = True
        cura_pegas = 0
        andares_sem_perder_vida = 0

        particles = []
        running = True
        paused = False
        mostrou_msg_shop = False  # mostra a mensagem só uma vez por partida

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    moved = False
                    if event.key in [pygame.K_w, pygame.K_UP]:
                        player.move(0, -1, dungeon)
                        moved = True
                    elif event.key in [pygame.K_s, pygame.K_DOWN]:
                        player.move(0, 1, dungeon)
                        moved = True
                    elif event.key in [pygame.K_a, pygame.K_LEFT]:
                        player.move(-1, 0, dungeon)
                        moved = True
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        player.move(1, 0, dungeon)
                        moved = True
                    elif event.key == pygame.K_ESCAPE:
                        paused = True
                    elif event.key == pygame.K_b:
                        tela_loja(self.screen, self.font, player)
                    if moved and "movimentos" in desafio:
                        desafio["movimentos"] += 1

            while paused:
                action = tela_pause(self.screen)
                if action == "quit":
                    pygame.quit()
                    sys.exit()
                paused = False
                break

            if player.invulnerable_timer > 0:
                player.invulnerable_timer -= 1

            enemy_move_timer += 1
            if enemy_move_timer >= 10:
                for enemy in enemies:
                    enemy.move(dungeon, player)
                enemy_move_timer = 0

            enemies_restantes = []
            chaser_hit = False
            for enemy in enemies:
                if enemy.x == player.x and enemy.y == player.y:
                    if player.invulnerable_timer == 0:
                        player.hp -= 1
                        andar_sem_dano = False
                        sound_hit.play()
                        player.invulnerable_timer = 30
                        if enemy.type == "chaser":
                            desafio["hit_chaser"] = True
                        if enemy.type == "chaser" and not chaser_hit:
                            chaser_hit = True
                        if player.hp <= 0:
                            sound_gameover.play()
                            running = False
                    if not (enemy.type == "chaser" and chaser_hit):
                        enemies_restantes.append(enemy)
                else:
                    enemies_restantes.append(enemy)
            enemies = enemies_restantes

            items_restantes = []
            for item in items:
                if item.x == player.x and item.y == player.y:
                    if item.type == ITEM_HEALTH:
                        player.hp = min(player.hp + 1, getattr(player, "max_hp", 3))
                        sound_powerup.play()
                        for i in range(16):
                            px = player.x * TILE_SIZE + TILE_SIZE // 2
                            py = player.y * TILE_SIZE + TILE_SIZE // 2
                            cor = (255, 255, 150)
                            particles.append(Particle(px, py, cor))
                        if "pegou_cura" in desafio:
                            desafio["pegou_cura"] = True
                        cura_pegas += 1
                    elif item.type == ITEM_TREASURE:
                        score += 1
                        if not hasattr(player, "coins"):
                            player.coins = 0
                        player.coins += 1
                        sound_coin.play()
                        for i in range(16):
                            px = player.x * TILE_SIZE + TILE_SIZE // 2
                            py = player.y * TILE_SIZE + TILE_SIZE // 2
                            cor = (255, 220, 80)
                            particles.append(Particle(px, py, cor))
                        if "tesouros_coletados" in desafio:
                            desafio["tesouros_coletados"] += 1

                        # Mensagem automática sobre a loja ao pegar a primeira moeda
                        if player.coins == 1 and not mostrou_msg_shop:
                            self.shop_msg_timer = 120  # ~2 segundos (se FPS=60)
                            mostrou_msg_shop = True

                else:
                    items_restantes.append(item)
            items = items_restantes

            for p in particles[:]:
                p.update()
                p.draw(self.screen)
                if p.life <= 0:
                    particles.remove(p)

            # Quando o jogador chega ao tile de saída
            if dungeon.map[player.y][player.x] == 2:
                if not desafio["cumprido"]:
                    if desafio["cond_check"](desafio, player):
                        desafio["cumprido"] = True
                        score += desafio["bonus"]
                        medalha_key = desafio.get("medalha")
                        if medalha_key and medalha_key in MEDALHAS:
                            self.medalhas_obtidas.add(medalha_key)
                            self.medalha_nova = _(MEDALHAS[medalha_key]["nome"])
                            self.medalha_nova_timer = 120
                        else:
                            self.medalha_nova = ""
                if andar_sem_dano:
                    andares_sem_perder_vida += 1
                    if andares_sem_perder_vida >= 3:
                        self.medalhas_obtidas.add("sobrevivente")
                        self.medalha_nova = _(MEDALHAS["sobrevivente"]["nome"])
                        self.medalha_nova_timer = 120
                else:
                    andares_sem_perder_vida = 0
                if andar == 10 and player.hp > 0:
                    self.medalhas_obtidas.add("invencivel")
                    self.medalha_nova = _(MEDALHAS["invencivel"]["nome"])
                    self.medalha_nova_timer = 120
                if cura_pegas >= 3:
                    self.medalhas_obtidas.add("curador")
                    self.medalha_nova = _(MEDALHAS["curador"]["nome"])
                    self.medalha_nova_timer = 120
                sound_door.play()
                andar += 1

                # Mantém moedas, upgrades e vida
                coins_antigas = getattr(player, "coins", 0)
                max_hp_antigo = getattr(player, "max_hp", 3)
                hp_antigo = min(getattr(player, "hp", 3), max_hp_antigo)

                dungeon = Dungeon()
                player = Player(dungeon)
                player.coins = coins_antigas
                player.max_hp = max_hp_antigo
                player.hp = hp_antigo

                enemies = criar_inimigos(dungeon, andar)
                items = spawn_items(dungeon.map, quantity_health=1, quantity_treasure=2 + andar // 2)
                enemy_move_timer = 0
                desafios = make_desafios()
                desafio = random.choice(desafios)
                desafio["cumprido"] = False
                if "on_start" in desafio:
                    desafio["on_start"](desafio, player, items=items)
                movimentos = 0
                andar_sem_dano = True
                cura_pegas = 0
                continue

            if self.medalha_nova_timer > 0:
                self.medalha_nova_timer -= 1
                if self.medalha_nova_timer == 0:
                    self.medalha_nova = None

            # Exibe mensagem sobre a loja ao pegar a primeira moeda
            self.screen.fill(COLOR_BG)
            dungeon.draw(self.screen, COLORS)
            for item in items:
                item.draw(self.screen)
            for enemy in enemies:
                enemy.draw(self.screen)
            player.draw(self.screen)

            try:
                desafio_status = desafio["progresso"](desafio, player)
                if isinstance(desafio_status, str):
                    desafio_status = _(desafio_status)
            except Exception:
                desafio_status = ""

            exibir_hud(
                self.screen, self.font, player, andar, score, self.highscore,
                desafio, desafio_status, self.medalha_nova
            )

            # Desenha a mensagem da loja se necessário
            if self.shop_msg_timer > 0:
                font_msg = pygame.font.SysFont(None, 38)
                msg = font_msg.render(_( "shop_first_coin" ), True, (255, 255, 80))
                rect = msg.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 80))
                self.screen.blit(msg, rect)
                self.shop_msg_timer -= 1

            pygame.display.flip()
            self.clock.tick(FPS)

        novo_recorde = False
        if score > self.highscore:
            self.highscore = score
            save_highscore(self.highscore)
            novo_recorde = True
        action = tela_game_over(
            self.screen, self.font, score, andar, self.highscore,
            novo_recorde, desafio,
            [_(MEDALHAS[key]["nome"]) for key in self.medalhas_obtidas if key in MEDALHAS]
        )
        if action == "quit":
            pygame.quit()
            sys.exit()
        tela_inicial(self.screen, self.highscore)
