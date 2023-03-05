def pick(b, wn, bn, p, v, depth):
    """
    find next move using minimax
    """
    z = -1
    if p == 64:
        s = -65
        for n in v:
            tmp = minimax(b, wn, bn, p, n, v[n], depth, s)
            if tmp > s:
                s = tmp
                z = n
    else:
        s = 65
        for n in v:
            tmp = minimax(b, wn, bn, p, n, v[n], depth, s)
            if tmp < s:
                s = tmp
                z = n
    return z


def minimax(b, wn, bn, prev_p, pos, flip, count, pruning):
    """
    minimax algorithm
    """
    b, wn, bn = nex(b, wn, bn, pos, flip, prev_p)
    if count == 0:
        return evaluate(b)
    else:
        next_v = valid(b, 129 - prev_p)
        if next_v:
            p = 129 - prev_p
        else:
            next_v = valid(b, prev_p)
            if next_v:
                p = prev_p
            else:
                p = -1

        if p == -1:
            return wn - bn
        elif p == 64:
            s = -65
            for n in next_v:
                s = max(s, minimax(b, wn, bn, p, n, next_v[n], count - 1, s))
                if prev_p == 65:
                    if s > pruning:
                        break
        else:
            s = 65
            for n in next_v:
                s = min(s, minimax(b, wn, bn, p, n, next_v[n], count - 1, s))
                if prev_p == 64:
                    if s < pruning:
                        break
        return s


def nex(b, wn, bn, c, f, p):
    """
    return the next state of the board
    """
    flipped = []
    fn = 0
    n = 0
    for i in range(8):
        tmp = []
        for j in range(8):
            if n == c:
                tmp.append(p)
            elif n in f:
                tmp.append(p)
                fn += 1
            else:
                tmp.append(b[i][j])
            n += 1
        flipped.append(tmp)
    if p == 64:
        wn += fn + 1
        bn -= fn
    else:
        wn -= fn
        bn += fn + 1
    return flipped, wn, bn


def valid(b, p):
    """
    find valid moves
    """
    v = {}
    for n in range(64):
        i, j = n // 8, n % 8
        if b[i][j] < 64:
            x = []
            d = 1
            tmp = []
            det = False
            while i + d < 8:
                if b[i + d][j] == 129 - p:
                    tmp.append(n + 8 * d)
                    d += 1
                else:
                    if b[i + d][j] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while i - d >= 0:
                if b[i - d][j] == 129 - p:
                    tmp.append(n - 8 * d)
                    d += 1
                else:
                    if b[i - d][j] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while j + d < 8:
                if b[i][j + d] == 129 - p:
                    tmp.append(n + d)
                    d += 1
                else:
                    if b[i][j + d] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while j - d >= 0:
                if b[i][j - d] == 129 - p:
                    tmp.append(n - d)
                    d += 1
                else:
                    if b[i][j - d] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while i + d < 8 and j + d < 8:
                if b[i + d][j + d] == 129 - p:
                    tmp.append(n + 9 * d)
                    d += 1
                else:
                    if b[i + d][j + d] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while i - d >= 0 and j - d >= 0:
                if b[i - d][j - d] == 129 - p:
                    tmp.append(n - 9 * d)
                    d += 1
                else:
                    if b[i - d][j - d] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while i + d < 8 and j - d >= 0:
                if b[i + d][j - d] == 129 - p:
                    tmp.append(n + 7 * d)
                    d += 1
                else:
                    if b[i + d][j - d] == p:
                        det = True
                    break
            if det:
                x += tmp

            d = 1
            tmp = []
            det = False
            while i - d >= 0 and j + d < 8:
                if b[i - d][j + d] == 129 - p:
                    tmp.append(n - 7 * d)
                    d += 1
                else:
                    if b[i - d][j + d] == p:
                        det = True
                    break
            if det:
                x += tmp

            if x:
                v[n] = x
    return v


def evaluate(b):

    score_board = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if b[i][j] == 64:
                score_board[i][j] += 1
            elif b[i][j] == 65:
                score_board[i][j] -= 1

    '''horizontal'''
    for i in range(8):
        if sum([b[i][j] > 63 for j in range(8)]) == 8:
            for j in range(8):
                if b[i][j] == 64:
                    score_board[i][j] += 1
                else:
                    score_board[i][j] -= 1
        else:
            if b[i][0] == 64:
                j = 0
                while j < 7:
                    if b[i][j] == 64:
                        score_board[i][j] += 1
                        j += 1
                    else:
                        break
            elif b[i][0] == 65:
                j = 0
                while j < 7:
                    if b[i][j] == 65:
                        score_board[i][j] -= 1
                        j += 1
                    else:
                        break

            if b[i][7] == 64:
                j = 7
                while j > 0:
                    if b[i][j] == 64:
                        score_board[i][j] += 1
                        j -= 1
                    else:
                        break
            elif b[i][7] == 65:
                j = 7
                while j > 0:
                    if b[i][j] == 65:
                        score_board[i][j] -= 1
                        j -= 1
                    else:
                        break

    '''vertical'''
    for j in range(8):
        if sum([b[i][j] > 63 for i in range(8)]) == 8:
            for i in range(8):
                if b[i][j] == 64:
                    score_board[i][j] += 1
                else:
                    score_board[i][j] -= 1
        else:
            if b[0][j] == 64:
                i = 0
                while i < 7:
                    if b[i][j] == 64:
                        score_board[i][j] += 1
                        i += 1
                    else:
                        break
            elif b[0][j] == 65:
                i = 0
                while i < 7:
                    if b[i][j] == 65:
                        score_board[i][j] -= 1
                        i += 1
                    else:
                        break

            if b[7][j] == 64:
                i = 7
                while i > 0:
                    if b[i][j] == 64:
                        score_board[i][j] += 1
                        i -= 1
                    else:
                        break
            elif b[7][j] == 65:
                i = 7
                while i > 0:
                    if b[i][j] == 65:
                        score_board[i][j] -= 1
                        i -= 1
                    else:
                        break

    '''diagonal (1)'''
    for i in range(8):
        if sum([b[i - j][j] > 63 for j in range(i + 1)]) == (i + 1):
            for j in range(i + 1):
                if b[i - j][j] == 64:
                    score_board[i - j][j] += 1
                else:
                    score_board[i - j][j] -= 1
        else:
            if b[i][0] == 64:
                j = 0
                while j < i:
                    if b[i - j][j] == 64:
                        score_board[i - j][j] += 1
                        j += 1
                    else:
                        break
            elif b[i][0] == 65:
                j = 0
                while j < i:
                    if b[i - j][j] == 65:
                        score_board[i - j][j] -= 1
                        j += 1
                    else:
                        break

            if b[0][i] == 64:
                j = i
                while j > 0:
                    if b[i - j][j] == 64:
                        score_board[i - j][j] += 1
                        j -= 1
                    else:
                        break
            elif b[0][i] == 65:
                j = i
                while j > 0:
                    if b[i - j][j] == 65:
                        score_board[i - j][j] -= 1
                        j -= 1
                    else:
                        break

    '''diagonal (2)'''
    for i in range(8):
        if sum([b[i + j][j] > 63 for j in range(8 - i)]) == 8 - i:
            for j in range(8 - i):
                if b[i + j][j] == 64:
                    score_board[i + j][j] += 1
                else:
                    score_board[i + j][j] -= 1
        else:
            if b[i][0] == 64:
                j = 0
                while j < 7 - i:
                    if b[i + j][j] == 64:
                        score_board[i + j][j] += 1
                        j += 1
                    else:
                        break
            elif b[i][0] == 65:
                j = 0
                while j < 7 - i:
                    if b[i + j][j] == 65:
                        score_board[i + j][j] -= 1
                        j += 1
                    else:
                        break

            if b[7][7 - i] == 64:
                j = 7 - i
                while j > 0:
                    if b[i + j][j] == 64:
                        score_board[i + j][j] += 1
                        j -= 1
                    else:
                        break
            elif b[7][7 - i] == 65:
                j = 7 - i
                while j > 0:
                    if b[i + j][j] == 65:
                        score_board[i + j][j] -= 1
                        j -= 1
                    else:
                        break

    '''diagonal (3)'''
    for j in range(1, 8):
        if sum([b[7 - i][i + j] > 63 for i in range(8 - j)]) == 8 - j:
            for i in range(8 - j):
                if b[7 - i][i + j] == 64:
                    score_board[7 - i][i + j] += 1
                else:
                    score_board[7 - i][i + j] -= 1
        else:
            if b[7][j] == 64:
                i = 0
                while i < 7 - j:
                    if b[7 - i][i + j] == 64:
                        score_board[7 - i][i + j] += 1
                        i += 1
                    else:
                        break
            elif b[7][j] == 65:
                i = 0
                while i < 7 - j:
                    if b[7 - i][i + j] == 65:
                        score_board[7 - i][i + j] -= 1
                        i += 1
                    else:
                        break

            if b[j][7] == 64:
                i = 7 - j
                while i > 0:
                    if b[7 - i][i + j] == 64:
                        score_board[7 - i][i + j] += 1
                        i -= 1
                    else:
                        break
            elif b[j][7] == 65:
                i = 7 - j
                while i > 0:
                    if b[7 - i][i + j] == 65:
                        score_board[7 - i][i + j] -= 1
                        i -= 1
                    else:
                        break

    '''diagonal (4)'''
    for j in range(1, 8):
        if sum([b[i][i + j] > 63 for i in range(8 - j)]) == 8 - j:
            for i in range(8 - j):
                if b[i][i + j] == 64:
                    score_board[i][i + j] += 1
                else:
                    score_board[i][i + j] -= 1
        else:
            if b[0][j] == 64:
                i = 0
                while i < 7 - j:
                    if b[i][i + j] == 64:
                        score_board[i][i + j] += 1
                        i += 1
                    else:
                        break
            elif b[0][j] == 65:
                i = 0
                while i < 7 - j:
                    if b[i][i + j] == 65:
                        score_board[i][i + j] -= 1
                        i += 1
                    else:
                        break

            if b[7 - j][7] == 64:
                i = 7 - j
                while i > 0:
                    if b[i][i + j] == 64:
                        score_board[i][i + j] += 1
                        i -= 1
                    else:
                        break
            elif b[7 - j][7] == 65:
                i = 7 - j
                while i > 0:
                    if b[i][i + j] == 65:
                        score_board[i][i + j] -= 1
                        i -= 1
                    else:
                        break

    score = 0
    for i in range(8):
        for j in range(8):
            if abs(score_board[i][j]) == 5:
                score += 6 * score_board[i][j]
            else:
                score += score_board[i][j]

    return score / 30
