# Dungeon Roguelike

![badge-platform](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![badge-status](https://img.shields.io/badge/status-MVP-blueviolet)
![badge-license](https://img.shields.io/badge/license-MIT-green)

Jogo **Roguelike Dungeon Crawler** em Pygame, com gera��o procedural de masmorras, desafios din�micos, loja de upgrades, internacionaliza��o (4 idiomas) e sistema de medalhas. Minimalista, expans�vel e divertido!

---

## �ndice

- [Demonstra��o](#demonstra��o)
- [Funcionalidades](#funcionalidades)
- [Instala��o](#instala��o)
- [Uso](#uso)
- [Checklist de Progresso](#checklist-de-progresso)
- [Contribui��o](#contribui��o)
- [Licen�a](#licen�a)
- [Autores](#autores)
- [Agradecimentos](#agradecimentos)

---

## Demonstra��o

![Exemplo de gameplay](assets/images/gameplay.png)

---

## Funcionalidades

- **Gera��o Procedural** de masmorras com conectividade garantida
- **Player** com movimenta��o por grid e HUD completa
- **Inimigos** com IA b�sica (aleat�rio e perseguidor)
- **Itens** de cura e tesouro, com coleta din�mica
- **Loja (SHOP)** acess�vel por tecla `B` para upgrades
- **Desafios** �nicos a cada andar, medalhas colecion�veis e pontua��o
- **Interface multil�ngue:** Portugu�s, Ingl�s, Espanhol e Franc�s
- **Tela de pausa, game over, HUD contextual**
- **Sistema de som** para eventos importantes
- **Persist�ncia** de recorde (highscore)
- Expans�vel para armas, magias, saves, etc.

---

## Instala��o

1. **Clone o reposit�rio:**
   ```bash
   git clone https://github.com/michelbr/dungeon-roguelike.git
   cd dungeon-roguelike
````

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as depend�ncias:**

   ```bash
   pip install pygame
   ```

4. **(Opcional) Ajuste o caminho dos assets se necess�rio.**

---

## Uso

Execute o jogo com:

```bash
python main.py
```

* **Mover:** WASD ou Setas
* **Abrir loja:** B (aparece dica ao pegar a 1� moeda)
* **Pausar:** ESC
* **Recome�ar:** R (ap�s Game Over)
* **Trocar idioma:** L (na tela inicial)

O progresso de moedas, vida m�xima e medalhas � mantido entre andares.

---

## Checklist de Progresso

### MVP - Estrutura, Gameplay e N�cleo

* [x] Pastas: `/src`, `/assets`, `/levels`, `/saves`
* [x] Arquivos: `main.py`, `config.py`
* [x] Gera��o procedural (`dungeon.py`)
* [x] Jogador (`player.py`), HUD, moedas acumulam
* [x] Inimigos (`enemy.py`), IA simples e perseguidor
* [x] Itens (`item.py`), coleta, moedas, cura
* [x] Andares/portas, transi��o, manter progresso
* [x] Desafios e medalhas por andar
* [x] Loja acess�vel com upgrades (+vida, cura, invulner�vel)
* [x] Som e efeitos b�sicos

### UX, Polimento & Internacionaliza��o

* [x] i18n: pt, en, es, fr
* [x] HUD completa, dicas contextuais, tela de pausa/loja integradas
* [ ] Dica autom�tica da loja ao pegar a 1� moeda
* [ ] Garantir fontes compat�veis unicode
* [ ] Mensagem ap�s compra/venda na loja
* [ ] Corrigir bug de s�mbolos (exibir `$` seguro)
* [ ] Garantir moedas acumulam sempre entre andares/game over

### Expans�es Futuras

* [ ] Novos inimigos e armadilhas
* [ ] Mais upgrades e itens na loja
* [ ] Armas, magias, buffs
* [ ] NPCs, quests, di�logos
* [ ] Gr�ficos, anima��es, efeitos sonoros avan�ados
* [ ] Sistema de saves/meta-progresso
* [ ] Rank online, desafios di�rios/semanais

---

## Contribui��o

Contribui��es s�o bem-vindas!

1. Fa�a um fork deste reposit�rio
2. Crie sua branch (`git checkout -b minha-feature`)
3. Commit suas mudan�as (`git commit -am 'Nova feature'`)
4. Fa�a push para sua branch (`git push origin minha-feature`)
5. Abra um Pull Request

Confira as [issues](https://github.com/michelbr/dungeon-roguelike/issues) ou discuta melhorias conosco.

---

## Licen�a

Distribu�do sob a [Licen�a MIT](LICENSE).

---

## Autores

* [Seu Nome](https://github.com/michelbr) � dev principal
* Colabore voc� tamb�m! Envie sugest�es, tradu��es ou c�digo.

---

## Agradecimentos

* Comunidade Pygame
* Reposit�rios open-source de Roguelikes que inspiraram este projeto
* Quem testou, reportou bugs e sugeriu melhorias :)

---

*Dungeon Roguelike: um projeto educativo, divertido e open-source. Compartilhe, jogue, hackeie e evolua junto!*