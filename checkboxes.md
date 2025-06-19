# checkboxes.md

## MVP - Estrutura, Gameplay e Núcleo

* [x] Criar pastas: `/src`, `/assets`, `/levels`, `/saves`
* [x] Criar arquivos iniciais: `main.py`, `config.py`
* [x] Configurar constantes, resolução, FPS e cores
* [x] Inicializar Pygame e janela do jogo

### Geração de Masmorra

* [x] Criar `dungeon.py` para mapa procedural
* [x] Algoritmo de geração procedural (Drunkard Walk/Cellular)
* [x] Sala inicial e saída conectada
* [x] Garantir conectividade das salas
* [x] Renderizar tiles: chão, parede, porta

### Jogador

* [x] Criar `player.py`
* [x] Classe Player: posição, vida, moedas
* [x] Movimentação por grid (WASD/setas)
* [x] Colisão com paredes
* [x] Desenhar jogador no mapa
* [x] Moedas acumulam entre andares

### Inimigos

* [x] Criar `enemy.py`
* [x] Classe Enemy com posição e comportamento
* [x] Movimento aleatório e perseguidor
* [x] Dano ao encostar no jogador (com som)
* [x] Turnos: jogador move, depois inimigos

### Itens

* [x] Criar `item.py`
* [x] Tipos de item: cura, tesouro (moeda)
* [x] Spawn aleatório em tiles acessíveis
* [x] Jogador coleta ao passar pelo tile
* [x] Aumentar moeda ao pegar tesouro

### Portas e Andares

* [x] Tile de saída (porta)
* [x] Novo andar ao entrar na porta
* [x] Resetar inimigos e itens a cada andar
* [x] Moedas continuam acumulando

### Desafios e Medalhas

* [x] Sistema de desafios por andar
* [x] Conferir e mostrar desafio no HUD
* [x] Premiação: pontos extras e medalhas colecionáveis

### Loja (SHOP)

* [x] Tela de loja acessível por tecla (B)
* [x] Compra de upgrades: +cura, +vida máx, invulnerável
* [x] Exibir moedas do jogador (HUD e Loja)
* [x] Mensagem/dica ao pegar a primeira moeda: "Use B para abrir loja"
* [x] Bloqueio de compra sem moedas suficientes

### Fim de Jogo

* [x] Detectar morte do jogador
* [x] Tela de Game Over (score, andar, recorde, medalhas)
* [x] Reinício via menu/tela inicial

---

## UX, Polimento & Internacionalização

### Internacionalização (i18n)

* [x] Criar `lang.py` (pt, en, es, fr)
* [x] Interface multilíngue dinâmica (troca no menu)
* [x] Traduzir textos fixos e dinâmicos

### Interface Gráfica (UI/UX)

* [x] Criar `ui.py`
* [x] HUD com vida, moedas, andar, score, recorde, desafio atual
* [x] Mensagens contextuais: vitória, derrota, dicas rápidas
* [x] Tela de pausa (resume/quit)
* [x] Tela de loja visualmente integrada
* [ ] Melhorar fontes (compatibilidade unicode em todos sistemas)
* [ ] Garantir contraste e clareza na HUD (bordas, cores)

### Polimento & Testes

* [x] Refatorar e modularizar código
* [x] Testar funcionalidades (andar, loja, desafios, etc)
* [ ] Corrigir bug de fonte unicode (símbolos)
* [x] Mensagem orientando sobre a loja ao pegar 1ª moeda
* [ ] Garantir moedas acumulam corretamente entre andares e Game Over

---

## Expansões Futuras

* [ ] Novos inimigos com comportamento variado
* [ ] Armadilhas e power-ups diversos
* [ ] Mais itens e upgrades na loja
* [ ] Armas, magias, buffs temporários
* [ ] NPCs, quests, diálogos
* [ ] Gráficos aprimorados, animações e efeitos sonoros
* [ ] Sistema de saves e meta-progresso
* [ ] Rank online e desafios diários/semanais

---

## 🔥 Tarefas Urgentes / Prioridade Atual

* [ ] Corrigir problema de fonte unicode (exibir \$ ou texto seguro)
* [x] Adicionar dica automática da loja ao pegar a primeira moeda
* [ ] Garantir moedas acumulam para próximos andares e não zeram ao passar de andar/Game Over
* [ ] Mensagem clara após compra/venda na Loja

- Seed, escolha de fase em forma de seed