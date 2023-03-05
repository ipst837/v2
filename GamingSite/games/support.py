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


class Board:
    """
    state of the game board
    """
    def __init__(self):
        self.b = [[8 * i + j for j in range(8)] for i in range(8)]                  # the game board
        self.b[3][3], self.b[4][4], self.b[3][4], self.b[4][3] = 64, 64, 65, 65     # initial state of the game board
        self.wn = 2     # number of white disks
        self.bn = 2     # number of black disks
        self.z = 28     # previous move (0 ~ 63)
        self.turn = 64  # 64 for white player's turn, 65 for black player's turn

    def flip(self, new_disk, flipped_disks):
        """
        place a new disk and flip disks accordingly
        """
        fn = 0
        self.b[new_disk // 8][new_disk % 8] = self.turn
        for fd in flipped_disks:
            self.b[fd // 8][fd % 8] = self.turn
            fn += 1
        if self.turn == 64:
            self.wn += fn + 1
            self.bn -= fn
        else:
            self.wn -= fn
            self.bn += fn + 1
        self.z = new_disk

