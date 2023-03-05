def pick(b, wn, bn, p, v, dummy):
    s = -65
    z = -1
    for n in v:
        tmp = greedy(b, wn, bn, n, v[n], p)
        if tmp > s:
            s = tmp
            z = n
    return z


def greedy(b, wn, bn, c, f, p):
    b, wn, bn = nex(b, wn, bn, c, f, p)
    if p == 64:
        return wn - bn
    else:
        return bn - wn


def nex(b, wn, bn, c, f, p):
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
