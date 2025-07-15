
# Pedra, Papel e Tesoura - Versão Terminal 🎮✊📄✂️

Este é um projeto simples em Python que simula o clássico jogo **Pedra, Papel e Tesoura** contra o computador, diretamente no terminal.

---

## 🎯 Funcionalidades

- Solicita **nome personalizado do jogador** no início da sessão.
- Menu interativo com opções numéricas:
  - `1` = Pedra
  - `2` = Papel
  - `3` = Tesoura
  - `9` = Sair do jogo
- O computador realiza uma jogada aleatória.
- Sistema de **placar parcial e final** exibindo o nome do jogador.
- Exibição de **mensagem de vitória, derrota ou empate** ao final da sessão.
- **Registro de partidas em arquivo `.txt`** opcional, com data, nome do jogador e placar.
- **Limpeza automática da tela** entre rodadas (somente em terminais reais).
- Interface leve e com emojis para deixar a experiência mais divertida.

---

## 🚀 Tecnologias usadas

- Python 3.x
- Módulo `random` – para escolhas aleatórias do computador
- Módulo `os` – para comandos de limpeza de tela (`cls`/`clear`)

---

## ▶️ Como executar

1. Clone o repositório ou baixe o arquivo:
   ```bash
   git clone https://github.com/leomacedo/desafios-python.git
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd desafios-python/PedraPapelTesoura
   ```
3. Execute o script no terminal:
   ```bash
   python PedraPapelTesoura.py
   ```

> Recomendado rodar em **VSCode**, **Prompt de Comando**, **PowerShell** ou terminal Linux/macOS para melhor experiência visual.

---

## 📁 Registro de Partidas

Ao final de cada sessão, o jogador pode optar por registrar a partida em um arquivo chamado `registro_partidas_.txt`, contendo:

> Esse arquivo **é ignorado no Git** por estar listado no `.gitignore`, mantendo o repositório limpo.

---

## 🧑‍💻 Autor

[Leonardo Macedo](https://github.com/leomacedo)  
📍 Aracaju, SE – Brasil

