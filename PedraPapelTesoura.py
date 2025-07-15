import random  # Biblioteca para gerar escolhas aleatórias do computador
import os      # Biblioteca para limpar a tela no terminal (cross-platform)
from datetime import datetime  # Biblioteca para capturar data e hora atuais

# Dicionário com as opções do jogo
opcoes = {
    1: "✊ Pedra",
    2: "✋ Papel",
    3: "✌️  Tesoura"
}

# Variáveis para armazenar a pontuação
placar_jogador = 0
placar_computador = 0

# Função para limpar a tela (Windows ou Linux/Mac)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para registrar a partida no arquivo .txt
def registrar_partida(nome, pontos_jogador, pontos_computador):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formata a data e hora atuais
    # Abre o arquivo em modo append ("a") e escreve o registro no final
    with open("registro_partidas_.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"🔹 {data} - Jogador: {nome} | Placar: {nome} {pontos_jogador} x {pontos_computador} Computador\n")

# Solicita o nome do jogador
nome_jogador = input("Digite seu nome para começar: ")

# Função que exibe o placar (parcial ou final, dependendo do argumento)
def exibir_placar(tipo):
    print(f"\nPlacar {tipo}:")
    print(f"{nome_jogador}: {placar_jogador} | Computador: {placar_computador}")

# Loop principal do jogo
while True:
    limpar_tela()  # Limpa a tela a cada rodada

    # Exibe o menu de jogadas
    print("\nEscolha sua jogada:")
    print("1 - ✊ Pedra")
    print("2 - ✋ Papel")
    print("3 - ✌️  Tesoura")
    print("9 - ❌ Sair do jogo")

    # Mostra o placar parcial antes da rodada
    exibir_placar("parcial")

    # Valida a entrada do jogador
    while True:
        jogador = input("\nDigite o número da sua jogada: ")
        if jogador in ["1", "2", "3", "9"]:
            jogador = int(jogador)
            break
        else:
            print("❌ Jogada inválida. Tente novamente.")

    # Se o jogador quiser sair (9), exibe o placar final
    if jogador == 9:
        print(f"\nObrigado por jogar {nome_jogador}! Até a próxima 👋")
        exibir_placar("final")

        # Exibe quem venceu a sessão
        if placar_jogador == placar_computador:
            print("\nO jogo terminou empatado!")
        elif placar_jogador > placar_computador:
            print("\nParabéns! Você ganhou!")
        else:
            print("\nVocê perdeu! Melhor sorte na próxima!")

        # Pergunta se deseja salvar o resultado em arquivo
        salvar = input("\nDeseja salvar esta partida no registro? (s/n): ").lower()
        if salvar == "s":
            registrar_partida(nome_jogador, placar_jogador, placar_computador)
            print("✅ Partida registrada com sucesso!")
        else:
            print("📁 Registro não salvo.")
        break  # Sai do loop principal

    # Computador faz uma jogada aleatória
    computador = random.choice([1, 2, 3])

    # Exibe as escolhas
    print(f"\n{nome_jogador} escolheu: {opcoes[jogador]}")
    print(f"O computador escolheu: {opcoes[computador]}")

    # Lógica de vitória, empate ou derrota
    if jogador == computador:
        print("\n🤝 Deu empate!")
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        print(f"\n🏆 {nome_jogador} vence!")
        placar_jogador += 1
    else:
        print("\n💻 Computador vence!")
        placar_computador += 1

    # Aguarda o jogador pressionar Enter para continuar
    input("\nPressione Enter para continuar...")
