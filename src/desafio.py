# src/desafio.py

from item import ITEM_HEALTH, ITEM_TREASURE

# Medals use keys; translation only happens on display!
MEDALHAS = {
    "pacifista": {"nome": "medal_pacifista", "desc": "desc_pacifista"},
    "colecionador": {"nome": "medal_colecionador", "desc": "desc_colecionador"},
    "sobrevivente": {"nome": "medal_sobrevivente", "desc": "desc_sobrevivente"},
    "velocista": {"nome": "medal_velocista", "desc": "desc_velocista"},
    "invencivel": {"nome": "medal_invencivel", "desc": "desc_invencivel"},
    "curador": {"nome": "medal_curador", "desc": "desc_curador"},
}

def make_desafios():
    """
    Gera a lista de desafios (missões) possíveis.
    Use keys, nunca texto direto!
    """
    return [
        {
            "nome": "challenge_pacifista",
            "cond_init": lambda: True,
            "cond_check": lambda d, player, **kw: player.hp == d["hp_ini"],
            "on_start": lambda d, player, **kw: d.update({"hp_ini": player.hp, "hit": False}),
            "bonus": 5,
            "medalha": "pacifista",
            "progresso": lambda d, p, **kw: ("hud_life_now", p.hp)
        },
        {
            "nome": "challenge_colecionador",
            "cond_init": lambda: True,
            "cond_check": lambda d, p, **kw: d["tesouros_iniciais"] == d["tesouros_coletados"] and d["tesouros_iniciais"] > 0,
            "on_start": lambda d, p, items, **kw: d.update({
                "tesouros_iniciais": sum(1 for item in items if item.type == ITEM_TREASURE),
                "tesouros_coletados": 0
            }),
            "bonus": 5,
            "medalha": "colecionador",
            "progresso": lambda d, p, **kw: ("hud_treasures", d["tesouros_coletados"], d["tesouros_iniciais"])
        },
        {
            "nome": "challenge_curador",
            "cond_init": lambda: True,
            "cond_check": lambda d, p, **kw: d.get("pegou_cura", False),
            "on_start": lambda d, p, **kw: d.update({"pegou_cura": False}),
            "bonus": 5,
            "medalha": "curador",
            "progresso": lambda d, p, **kw: "hud_heal_yes" if d.get("pegou_cura") else "hud_not_yet"
        },
        {
            "nome": "challenge_velocista",
            "cond_init": lambda: True,
            "cond_check": lambda d, p, **kw: d["movimentos"] <= 20,
            "on_start": lambda d, p, **kw: d.update({"movimentos": 0}),
            "bonus": 8,
            "medalha": "velocista",
            "progresso": lambda d, p, **kw: ("hud_moves", d["movimentos"])
        },
        {
            "nome": "challenge_chaser",
            "cond_init": lambda: True,
            "cond_check": lambda d, p, **kw: d.get("hit_chaser", False),
            "on_start": lambda d, p, **kw: d.update({"hit_chaser": False}),
            "bonus": 5,
            "medalha": None,
            "progresso": lambda d, p, **kw: "hud_chaser_done" if d.get("hit_chaser") else "hud_not_yet"
        }
    ]
