# Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))


def game_board():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
    print("-------------")

game_board()
