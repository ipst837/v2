from django.db import models
from . import support as sup
from . import ai_minimax as aim
from . import ai_greedy as aig
from . import ai_improved as aii
from . import ai_tic as ait
import copy


class GamesList(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name


class GameTicTacToe:
    def __init__(self, room_id):
        self.room_id = room_id
        self.board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        self.turn = 'X'
        self.valid = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.end = False
        self.ai = self.room_id % 2 == 1

    def initialize(self):
        self.board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        self.turn = 'X'
        self.valid = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.end = False
        self.ai = self.room_id % 2 == 1

    def is_game_over(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    return 'X'
                else:
                    return 'O'
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j]:
                if self.board[0][j] == 'X':
                    return 'X'
                else:
                    return 'O'
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                return 'X'
            else:
                return 'O'
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == 'X':
                return 'X'
            else:
                return 'O'
        if self.valid:
            return False
        else:
            return "Draw"

    def update(self, action):
        if not self.end:
            c = (action // 3, action % 3)
            if c in self.valid:
                self.valid.remove(c)
                self.board[c[0]][c[1]] = self.turn
                if self.turn == 'X':
                    self.turn = 'O'
                else:
                    self.turn = 'X'
                self.end = self.is_game_over()
                self.ai = True

    def play_ai_dumb(self):
        if not self.end:
            action = ait.dumb(list(self.valid))
            self.valid.remove(action)
            self.board[action[0]][action[1]] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.end = self.is_game_over()
        self.ai = False

    def play_ai_minimax(self):
        if not self.end:
            action = ait.minimax(self.board, list(self.valid), self.turn)
            self.valid.remove(action)
            self.board[action[0]][action[1]] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.end = self.is_game_over()
        self.ai = False


class GameOthello:
    def __init__(self, room_id):
        self.room_id = room_id
        self.depth_medium = 5
        self.depth_hard = 4
        self.rou = 0         # round
        self.board = sup.Board()  # initialize the game board
        self.memo = {self.rou: copy.deepcopy(self.board)}  # save previous states of the game
        self.v = {20: [28], 29: [28], 34: [35], 43: [35]}  # set of valid moves (initial state)
        self.end = False  # becomes color of the winner when the game ends
        self.ai = 0
        if (self.room_id % 4) >= 2:
            self.update(20)
            self.ai = 0

    def initialize(self):
        self.rou = 0  # round
        self.board = sup.Board()  # initialize the game board
        self.memo = {self.rou: copy.deepcopy(self.board)}  # save previous states of the game
        self.v = {20: [28], 29: [28], 34: [35], 43: [35]}  # set of valid moves (initial state)
        self.end = False  # becomes color of the winner when the game ends
        if (self.room_id % 4) >= 2:
            self.update(20)
        self.ai = 0

    def prepare_next_round(self):
        self.v = sup.valid(self.board.b, 129 - self.board.turn)
        if self.v:
            self.board.turn = 129 - self.board.turn
            self.memo[self.rou] = copy.deepcopy(self.board)
            self.ai = 1 - self.ai
        else:
            self.v = sup.valid(self.board.b, self.board.turn)
            self.memo[self.rou] = copy.deepcopy(self.board)
            if not self.v:
                if self.board.wn > self.board.bn:
                    self.end = "White"
                elif self.board.wn < self.board.bn:
                    self.end = "Black"
                else:
                    self.end = "Draw"
                self.ai = 0
                self.board.turn = 129 - self.board.turn

    def back(self):
        while self.rou > 0:
            self.rou -= 1
            if self.memo[self.rou].turn == self.board.turn:
                break
        self.board = copy.deepcopy(self.memo[self.rou])
        self.v = sup.valid(self.board.b, self.board.turn)

    def update(self, action):
        if not self.end:
            if action in self.v:
                self.board.flip(action, self.v[action])
                self.rou += 1
                self.prepare_next_round()

    def play_ai_greedy(self):
        if not self.end:
            z = aig.pick(self.board.b, self.board.wn, self.board.bn, self.board.turn, self.v, 0)
            self.board.flip(z, self.v[z])
            self.rou += 1
            self.prepare_next_round()

    def play_ai_minimax(self):
        if not self.end:
            z = aim.pick(self.board.b, self.board.wn, self.board.bn, self.board.turn, self.v, self.depth_medium)
            self.board.flip(z, self.v[z])
            self.rou += 1
            self.prepare_next_round()

    def play_ai_improved(self):
        if not self.end:
            z = aii.pick(self.board.b, self.board.wn, self.board.bn, self.board.turn, self.v, self.depth_hard)
            self.board.flip(z, self.v[z])
            self.rou += 1
            self.prepare_next_round()
