# Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))


def game_board():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
    print("-------------")

def input_an_action (entering):
    while True:
        value = input ("Сделайте ход. Выберите ячейку: " +entering)  
        if not (value in "123456789"):
            print("Неверные ввод.Повторитет попытку")
            continue
        value = int(value)
        if str(board[value -1] in "XO"):
            print("УПС! Место занято. Повторите попытку")
            continue
        board[value -1] = entering
        break

#game_board()
