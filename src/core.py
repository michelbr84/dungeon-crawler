# src/core.py

from enemy import Enemy

def criar_inimigos(dungeon, andar):
    """
    Cria a lista de inimigos para o andar atual.
    Após o andar 5, começa a aparecer pelo menos 1 inimigo perseguidor ("chaser").
    """
    enemies = []
    total = 2 + andar
    if andar >= 5:
        num_chaser = max(1, total // 3)
    else:
        num_chaser = 0
    num_random = total - num_chaser
    for _ in range(num_chaser):
        enemies.append(Enemy(dungeon, enemy_type="chaser"))
    for _ in range(num_random):
        enemies.append(Enemy(dungeon, enemy_type="random"))
    return enemies

# Outras funções core podem vir aqui futuramente, por exemplo:
# - lógica de reset de andar
# - checagem de condições globais de jogo
# - gerenciamento de estatísticas, etc.
