# src/shop.py

SHOP_ITEMS = [
    {
        "id": "max_hp",
        "name": {
            "pt": "Coração Extra",
            "en": "Extra Heart",
            "es": "Corazón Extra",
            "fr": "Cœur Supplémentaire"
        },
        "desc": {
            "pt": "Aumenta a vida máxima em 1",
            "en": "Increase max HP by 1",
            "es": "Aumenta la vida máxima en 1",
            "fr": "Augmente la vie max de 1"
        },
        "price": 3,
        "apply": lambda player: setattr(player, 'max_hp', player.max_hp + 1)
    },
    {
        "id": "heal",
        "name": {
            "pt": "Cura Total",
            "en": "Full Heal",
            "es": "Curación Completa",
            "fr": "Soin Total"
        },
        "desc": {
            "pt": "Recupera toda a vida",
            "en": "Restores all HP",
            "es": "Restaura toda la vida",
            "fr": "Restaure toute la vie"
        },
        "price": 2,
        "apply": lambda player: setattr(player, 'hp', player.max_hp)
    },
    # Adicione outros itens conforme quiser...
]

def get_item_name(item, lang):
    return item["name"].get(lang, item["name"]["pt"])

def get_item_desc(item, lang):
    return item["desc"].get(lang, item["desc"]["pt"])
