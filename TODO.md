## ✅ Fase 1: Estrutura Inicial do Projeto

* Criar pastas: `/src`, `/assets`, `/levels`, `/saves` (se necessário)
* Criar arquivos iniciais: `main.py`, `config.py`
* Configurar constantes e tela do jogo (resolução, FPS, cores)
* Inicializar Pygame e a janela do jogo

---

## 🧱 Fase 2: Geração de Masmorra

* Criar `dungeon.py` para gerar o mapa procedural
* Implementar algoritmo de geração (Drunkard Walk, Cellular Automata etc.)
* Gerar sala inicial e saída conectada
* Garantir conectividade das salas
* Renderizar tiles (chão, parede, porta) com cores definidas

---

## 🕹️ Fase 3: Jogador

* Criar `player.py`
* Classe Player com posição, vida, moedas
* Implementar movimentação por grid (WASD/setas)
* Colisão com paredes
* Desenhar jogador no mapa
* Variáveis de progresso: vida, moedas acumulam entre andares

---

## 👾 Fase 4: Inimigos

* Criar `enemy.py`
* Classe Enemy com posição, comportamento (aleatório ou perseguidor)
* Movimento dos inimigos após ação do jogador
* Dano ao encostar no jogador (com efeito visual/som)
* Lógica: jogador move, depois inimigos

---

## 🎒 Fase 5: Itens

* Criar `item.py`
* Tipos: cura, tesouro (moeda), outros itens
* Spawn aleatório em tiles acessíveis
* Jogador coleta ao passar pelo tile
* Aumentar moeda ao pegar tesouro

---

## 🚪 Fase 6: Portas e Andares

* Criar tile de saída (porta)
* Gerar novo andar ao entrar na porta
* Resetar inimigos e itens a cada andar
* Manter moedas acumuladas

---

## 🏆 Fase 7: Desafios e Medalhas

* Criar sistema de desafios por andar (ex: zerar sem dano, pegar todos tesouros)
* Conferir e mostrar desafio no HUD
* Premiação: pontos extras e medalhas (colecionáveis no meta-jogo)
* Sistema de progresso e conquistas

---

## 🏬 Fase 8: Loja (SHOP)

* Implementar tela de loja acessível via tecla (ex: B)
* Permitir compra de upgrades: +cura, +vida máx, invulnerabilidade
* Exibir moedas do jogador (HUD e Loja)
* Mensagem ao pegar a primeira moeda: dica sobre a loja (tecla B)
* Bloqueio de compra sem moedas suficientes

---

## 💀 Fase 9: Fim de Jogo

* Detectar morte do jogador
* Tela de Game Over com score, andar atingido, recorde e medalhas
* Reinício pelo menu/tela inicial

---

## 🌍 Fase 10: Internacionalização (i18n)

* Criar `lang.py` com suporte a múltiplos idiomas (pt, en, es, fr)
* Interface multilíngue dinâmica (troca no menu)
* Traduzir textos fixos e dinâmicos do jogo

---

## 📊 Fase 11: Interface Gráfica (UI/UX)

* Criar `ui.py`
* HUD completo (vida, moedas, andar, score, recorde, desafio atual)
* Mensagens contextuais: vitória, derrota, dicas rápidas
* Tela de pausa (resume/quit)
* Tela de loja integrada e visualmente coerente
* Melhoria visual: fontes, cores, contraste, fontes compatíveis

---

## 🔧 Fase 12: Polimento, Testes e UX

* Refatorar código, modularizar funções
* Testar todas funcionalidades (andar, loja, desafios, etc)
* Mensagens para orientar usuário (ex: dica da loja ao pegar moeda)
* Ajustar balanceamento de dificuldade e recompensas
* Corrigir bugs de fontes, compatibilidade unicode, bordas de HUD

---

## 🚀 Expansões Futuras

* Novos tipos de inimigos com comportamento variado
* Armadilhas e power-ups variados
* Mais itens e upgrades na loja
* Armas, magias, buffs temporários
* NPCs, quests e diálogos
* Gráficos melhorados, animações e efeitos sonoros
* Sistema de saves e meta-progresso
* Rank online e desafios diários/semanais

---

**Observações de desenvolvimento atuais:**

* [ ] Corrigir problema de fonte unicode (substituir símbolos problemáticos por texto compatível).
* [ ] Adicionar dica automática sobre a loja ao pegar a primeira moeda.
* [ ] Melhorar mensagem de compra/venda na loja.
* [ ] Garantir moedas acumulam corretamente entre andares/game over.