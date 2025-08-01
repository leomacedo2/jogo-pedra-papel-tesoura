# Pedra, Papel e Tesoura - Versão Terminal 🎮✊📄✂️

Este é um jogo clássico de Pedra, Papel ou Tesoura desenvolvido em Python, com placar interativo, emojis, e um sistema de ranking salvo em planilha Excel. Foi criado para praticar lógica de programação, manipulação de arquivos, entrada/saída no terminal e uso de bibliotecas externas.

---

## 🎯 Objetivo

Ganhe do computador escolhendo sua jogada a cada rodada. O jogo mostra o placar, registra suas partidas e mantém um ranking de jogadores com vitórias, derrotas e empates.

---

## 🕹️ Como jogar

1. Digite seu nome no início do jogo.
2. Escolha entre:
   - `1` - ✊ Pedra
   - `2` - ✋ Papel
   - `3` - ✌️ Tesoura
   - `9` - ❌ Sair do jogo
3. Veja o resultado da rodada e o placar atualizado.
4. Ao sair do jogo, você pode optar por salvar o resultado e atualizar o ranking.

---

## 📂 Funcionalidades

- Interface terminal interativa e limpa
- Emojis para tornar o jogo mais visual
- Registro de partidas com data/hora
- Sistema de **placar parcial e final** exibindo o nome do jogador.
- Exibição de **mensagem de vitória, derrota ou empate** ao final da sessão.
- Geração automática de arquivo `registro_completo.xlsx` com:
  - **Aba 1:** Registro de todas as partidas
  - **Aba 2:** Ranking de jogadores (vitórias, derrotas e empates)

---

## 🧱 Tecnologias utilizadas

- Python 3.13+
- Biblioteca `openpyxl`
- Módulo `random` – para escolhas aleatórias do computador
- Módulo `os` – para comandos de limpeza de tela (`cls`/`clear`)

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/leomacedo2/jogo-pedra-papel-tesoura.git
cd jogo-pedra-papel-tesoura
```

### 2. Instale a dependência necessária

```bash
pip install openpyxl
```

Ou instale usando o arquivo de requisitos:

```bash
pip install -r requirements.txt
```

### 3. Execute o jogo

```bash
python PedraPapelTesoura.py
```

> Recomendado rodar em **VSCode**, **Prompt de Comando**, **PowerShell** ou terminal Linux/macOS para melhor experiência visual.
---

## 🧪 Exemplo de uso

- O jogador "Leo" joga 5 rodadas.
- Sai do jogo e opta por salvar a partida.
- O Excel `registro_completo.xlsx` é atualizado com as informações da partida e do ranking.

---

## 📊 Registro avançado em Excel
O jogo permite que o jogador salve os dados da sessão em um arquivo `.xlsx` com duas abas separadas, usando a biblioteca `openpyxl`:

Aba **"RegistroPartidas"**: histórico com data, nome do jogador e placar da sessão.

Aba **"RankingJogadores"**: acumulado de vitórias, derrotas e empates por jogador.

> O arquivo `registro_completo.xlsx` é gerado apenas com permissão do jogador e está incluído no `.gitignore` para manter o repositório limpo.

---

## 👤 Autor

[Leonardo Macedo](https://github.com/leomacedo2)

---

🎉 Obrigado por jogar!
