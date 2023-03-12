import random

def jogar():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    while jogador not in opcoes:
        jogador = input("Opção inválida. Escolha pedra, papel ou tesoura: ").lower()

    print(f"Você escolheu {jogador} e o computador escolheu {computador}.")

    if jogador == computador:
        print("Empate!")
    elif jogador == "pedra" and computador == "tesoura":
        print("Você ganhou!")
    elif jogador == "papel" and computador == "pedra":
        print("Você ganhou!")
    elif jogador == "tesoura" and computador == "papel":
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

    jogarNovamente()

def jogarNovamente():
    jogar_novamente = input("Deseja jogar novamente? (sim ou não): ").lower()
    if jogar_novamente == "sim":
        jogar()
    elif jogar_novamente == "não":
        print("Obrigado por jogar!")
    else:
        jogarNovamente()

jogar()
