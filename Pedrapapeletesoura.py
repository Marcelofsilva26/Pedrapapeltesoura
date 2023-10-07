print('Jogo pedra, papel e tesoura')
while True:
    player1 = input("Player 1 escolha pedra, papel ou tesoura (ou sair para encerrar o jogo): ")

    if player1 == "Sair" or player1 == "sair":
        print("O jogo foi encerrado.")
        break

    player2 = input("Player 2 escolha pedra, papel ou tesoura: ")

    if player1 == player2:
        print("Empate!")
    elif (player1 == "pedra" and player2 == "tesoura") or (player1 == "papel" and player2 == "pedra") or (player1 == "tesoura" and player2 == "papel"):
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")
