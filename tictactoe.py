"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x, o = 0, 0
    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1
    # Initial State
    if x == 0 and o == 0:
        return X
    
    # Termination states
    if terminal(board):
        return 0

    # Normal States
    return O if x > o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                s.add((i, j))
    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    b = copy.deepcopy(board)
    
    # Catch Illegal Move
    if b[action[0]][action[1]] != EMPTY:
        raise Exception('Illegal Move')
    
    b[action[0]][action[1]] = player(board)
    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if not terminal(board):
        return None
    
    for i in range(3):
        if all(board[i][j] == X for j in range(3)) or \
            all(board[j][i] == X for j in range(3)) or \
            all(board[j][j] == X for j in range(3)) or \
            all(board[j][2-j] == X for j in range(3)):
            return X
        elif all(board[i][j] == O for j in range(3)) or \
            all(board[j][i] == O for j in range(3)) or \
            all(board[j][j] == O for j in range(3)) or \
            all(board[j][2-j] == O for j in range(3)):
            return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Cases where either X or O wins
    for i in range(3):
        if all(board[i][j] == X for j in range(3)) or \
            all(board[i][j] == O for j in range(3)) or \
            all(board[j][i] == X for j in range(3)) or \
            all(board[j][i] == O for j in range(3)) or \
            all(board[j][j] == X for j in range(3)) or \
            all(board[j][j] == O for j in range(3)) or \
            all(board[j][2-j] == X for j in range(3)) or \
            all(board[j][2-j] == O for j in range(3)):
            return True
    
    # Cases where its a tie
    c = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                c += 1
    if c == 9:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # player, actions, result, winner, terminal, utility
    # X plays max, O plays min

    # temp
    # if board == initial_state():
    #     return (0,1)

    # init variables
    scores = []
    p = player(board)
    a = list(actions(board))

    # check if board is terminal
    if terminal(board):
        return None
    
    # create minimax game tree
    for i in a:
        res = result(board, i) # res is board
        m = minimax(res) # m is action
        if m is None:
            scores.append(utility(res))
        else:
            scores.append(utility(res) + utility(result(res, m)))
    
    # returns best action
    if p == X and max(scores) > -1:
        return a[scores.index(max(scores))]
    else:
        return a[scores.index(min(scores))]