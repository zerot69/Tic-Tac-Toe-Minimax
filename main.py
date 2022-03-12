# ===========================================
# - Title:  Tic Tac Toe Minimax
# - Author: @zerot69
# - Date:   12 Mar 2022
# ============================================


import random


def minimax(game_array, depth, is_maximizing):
    if check_winning_computer():
        return 10
    elif check_winning_player():
        return -10
    elif not check_winning_computer() and not check_winning_player() and check_drawing():
        return 0

    if is_maximizing:
        best_score = -1000
        for x in range(9):
            if game_array[x // 3][x % 3] == 0:
                game_array[x // 3][x % 3] = 1
                current_score = minimax(game_array, depth + 1, False) - depth
                game_array[x // 3][x % 3] = 0
                if current_score > best_score:
                    best_score = current_score
        return best_score
    else:
        best_score = +1000
        for x in range(9):
            if game_array[x // 3][x % 3] == 0:
                game_array[x // 3][x % 3] = -1
                current_score = minimax(game_array, depth + 1, True) - depth
                game_array[x // 3][x % 3] = 0
                if current_score < best_score:
                    best_score = current_score
        return best_score


def best_move():
    scores = [-1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000]
    moves = []
    for x in range(9):
        if gameArray[x // 3][x % 3] == 0:
            gameArray[x // 3][x % 3] = 1
            current_score = minimax(gameArray, 0, False)
            scores[x] = current_score
            gameArray[x // 3][x % 3] = 0
    for x in range(len(scores)):
        if scores[x] == int(max(scores)):
            moves.append(x)
    chosen_move = int(random.choice(moves))
    return chosen_move


def check_winning_computer():
    if gameArray[0][0] + gameArray[0][1] + gameArray[0][2] == 3:
        return True
    elif gameArray[0][0] + gameArray[1][0] + gameArray[2][0] == 3:
        return True
    elif gameArray[0][0] + gameArray[1][1] + gameArray[2][2] == 3:
        return True
    elif gameArray[0][1] + gameArray[1][1] + gameArray[2][1] == 3:
        return True
    elif gameArray[0][2] + gameArray[1][2] + gameArray[2][2] == 3:
        return True
    elif gameArray[0][2] + gameArray[1][1] + gameArray[2][0] == 3:
        return True
    elif gameArray[1][0] + gameArray[1][1] + gameArray[1][2] == 3:
        return True
    elif gameArray[2][0] + gameArray[2][1] + gameArray[2][2] == 3:
        return True
    else:
        return False


def check_winning_player():
    if gameArray[0][0] + gameArray[0][1] + gameArray[0][2] == -3:
        return True
    elif gameArray[0][0] + gameArray[1][0] + gameArray[2][0] == -3:
        return True
    elif gameArray[0][0] + gameArray[1][1] + gameArray[2][2] == -3:
        return True
    elif gameArray[0][1] + gameArray[1][1] + gameArray[2][1] == -3:
        return True
    elif gameArray[0][2] + gameArray[1][2] + gameArray[2][2] == -3:
        return True
    elif gameArray[0][2] + gameArray[1][1] + gameArray[2][0] == -3:
        return True
    elif gameArray[1][0] + gameArray[1][1] + gameArray[1][2] == -3:
        return True
    elif gameArray[2][0] + gameArray[2][1] + gameArray[2][2] == -3:
        return True
    else:
        return False


def check_drawing():
    for x in range(9):
        if gameArray[x // 3][x % 3] == 0:
            return False
    return True


def print_board():
    for x in range(9):

        if x == 0:
            print()

        if gameArray[x // 3][x % 3] == 1:
            print(" X ", end="")
        elif gameArray[x // 3][x % 3] == -1:
            print(" O ", end="")
        else:
            print("   ", end="")

        if x % 3 == 2 and x != 8:
            print("\n---+---+---")
        elif x != 8:
            print("|", end="")
        else:
            print()


print("Tic-tac-toe")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

moveCount = int(1)
userMove = int(0)
checkGameEnd = False
gameArray = [[0 for x in range(3)] for y in range(3)]

while not checkGameEnd:
    try:
        print("\nMove", moveCount, end=": ")

        if moveCount % 2 != 0:
            compMove = int(best_move())
            gameArray[compMove // 3][compMove % 3] = 1
            print("Computer's move:", compMove + 1)

            print_board()

            if check_winning_computer():
                print("\nComputer wins!")
                checkGameEnd = True
            elif check_drawing() and not check_winning_computer() and not check_winning_player():
                print("\nTied!")
                checkGameEnd = True

            moveCount += 1

        if checkGameEnd:
            break

        userMove = int(input("\nEnter your number (1-9): "))
        userMove -= 1
        if 0 <= userMove <= 8 and gameArray[userMove // 3][userMove % 3] == 0 and moveCount < 9:
            print("\nMove", moveCount, end=": ")
            print("Player's move:", userMove + 1, end="")
            gameArray[userMove // 3][userMove % 3] = -1
            checkGameEnd = check_winning_computer() or check_winning_player()
            moveCount += 1

            if check_winning_player():
                print_board()
                print("\nPlayer wins!")
                checkGameEnd = True
            elif check_drawing() and not check_winning_player() and not check_winning_computer():
                print_board()
                print("\nTied!")
                checkGameEnd = True

        else:
            print("Invalid input! Try again!")

    except ValueError:
        print("Invalid input! Try again!")
