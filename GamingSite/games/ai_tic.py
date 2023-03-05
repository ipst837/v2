import random
import copy


def dumb(v):
    return random.choice(v)


def result(board, action, turn):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    q = copy.deepcopy(board)
    q[action[0]][action[1]] = turn
    return q


def minimax(board, valid, turn):
    """
    Returns the optimal action for the current player on the board.
    """
    count = len(valid)
    if count == 9:
        return 1, 1
    else:
        q = valid[0]
        if turn == 'X':
            z = -10
            for i in range(count):
                tmp = dfs(result(board, valid[i], turn), count - 1, valid[:i] + valid[i + 1:], 'O', z)
                if tmp > z:
                    z = tmp
                    q = valid[i]
        else:
            z = 10
            for i in range(count):
                tmp = dfs(result(board, valid[i], turn), count - 1, valid[:i] + valid[i + 1:], 'X', z)
                if tmp < z:
                    z = tmp
                    q = valid[i]
        return q


def terminal(board, c):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return c
            elif board[i][0] == 'O':
                return -c
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == 'X':
                return c
            elif board[0][j] == 'O':
                return -c
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 'X':
            return c
        elif board[1][1] == 'O':
            return -c

    if c:
        return 20
    else:
        return 0


def dfs(board, c, v, p, pruning):
    x = terminal(board, c)
    if x == 20:
        if p == 'X':
            z = -10
            for i in range(c):
                z = max(z, dfs(result(board, v[i], p), c - 1, v[:i] + v[i + 1:], 'O', z))
                if z > pruning:
                    break
            return z
        else:
            z = 10
            for i in range(c):
                z = min(z, dfs(result(board, v[i], p), c - 1, v[:i] + v[i + 1:], 'X', z))
                if z < pruning:
                    break
            return z
    else:
        return x
