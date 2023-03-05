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
        return wn - bn
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
