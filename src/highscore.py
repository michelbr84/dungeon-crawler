# src/highscore.py

import os

def load_highscore(filename="highscore.txt"):
    """Carrega o recorde do arquivo, retorna 0 se não existir ou erro."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return int(f.read())
        except Exception:
            return 0
    return 0

def save_highscore(score, filename="highscore.txt"):
    """Salva o recorde no arquivo."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(score))
    except Exception:
        pass
