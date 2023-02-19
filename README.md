# Tic-Tac-Toe-Minimax
Tic-tac-toe in Python with Minimax Algorithm - Author: [@zerot69](http://github.com/zerot69)

![image](https://user-images.githubusercontent.com/55183414/217699771-f61c3f78-e8da-4cb9-ada4-6cd7cb504bcd.png)

## Tic-tac-toe game coding
The game state is stored in a 2D array `gameArray[][]` with the size of 3x3. The computer will be assigned as 1, and the player as -1. The `check_winning_computer()` function returns True when the sum of any winning line equals to 3, while the `check_winning_player()` function returns True when the sum of any winning line equals to -3.

The computer moves first and selects the best move using `compMove = int(best_move())` *(see below)*, and then registers the move in `gameArray[compMove // 3][compMove % 3] = 1`. The player can input their move by typing a number between 1 to 9, which is then registered on the board as `gameArray[userMove // 3][userMove % 3] = -1`.


## Minimax Algorithm: minimax() function
```
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
```

## Choosing the best move: best_move()
```
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
```
