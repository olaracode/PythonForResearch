# write your code here
import numpy as np
import matplotlib.pyplot as plt
import random


def create_board():
    board = np.zeros((3, 3))
    return board


def place(board, player, position):
    x, y = position[0], position[1]
    if board[x][y] == 0:
        board[x][y] = player
    else:
        place(board, player, position)
    # print(board)


def posibilities(board):
    pos = np.where(board == 0)
    # pos = np.asarray(board == 0)
    return pos

def random_place(board, player):
    pos = posibilities(board)
    x = len(pos[0])
    if x != 0:
        y = random.choice(range(x))
        place = pos[0][y]
        place2 = pos[1][y]
        # print(place)
        board[place, place2] = player
    else:
        return False

def row_win(board,player):
    x = [0, 1, 2]
    for i in x:
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        else:
            if x == 2:
                return False


def col_win(board, player):
    x = [0, 1, 2]
    for i in x:
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        else:
            if i == 2:
                return False


def diag_win(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if winner != 0:
            continue
        r = row_win(board, player)
        c = col_win(board, player)
        d = diag_win(board, player)
        if r is True or c is True or d is True:
            winner = player
        else:
            continue
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    x = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(x, player)
            winner = evaluate(x)
            if winner != 0:
                break
    print(x)
    return winner
    # x = create_board()
    # winner = 0
    # while winner == 0:
    #     if random_place(x, 1) is False:
    #         winner = 3
    #     else:
    #         random_place(x, 1)
    #         eval = evaluate(x)
    #         if eval == 1:
    #             winner = 1
    #
    #     if random_place(x, 2) is False:
    #         winner = 3
    #     else:
    #         random_place(x, 2)
    #         eval2 = evaluate(x)
    #         if eval2 == 2:
    #             winner = 2
    # # print(x)
    # print(x)
    # return evaluate(x)



def strategic_play_game():
    x = create_board()
    winner = 0
    x[1][1] = 1
    while winner == 0:
        for player in [2, 1]:
            random_place(x, player)
            winner = evaluate(x)
            if winner != 0:
                break
    return winner


# board = create_board()
# board[0, 2], board[1, 1], board[2, 0] = 1, 1, 1
# print(evaluate(board))
#
# print(board)
# print(evaluate(board))



results = []
results2 = []
y = 1000
i = 0
random.seed(1)
while i <= y:
    i += 1
    results.append(play_game())
print("normal", results)
print(1, results.count(1))
print(2, results.count(2))

i = 0
random.seed(1)
while i <= y:
    i += 1
    results2.append(strategic_play_game())


print("rigged", results2)

print(results2.count(1))
print(results2.count(2))