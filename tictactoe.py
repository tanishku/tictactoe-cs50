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
    if terminal(board):
        return None

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
    if terminal(board):
        return (1,1)
    
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
    #print(action)
    if b[action[0]][action[1]] != EMPTY:
        raise Exception('Illegal Move')
    elif (action[0] not in [0, 1, 2]) or (action[1] not in [0, 1, 2]):
        raise Exception('Illegal Move')
    
    b[action[0]][action[1]] = player(board)
    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # game is in progress
    if not terminal(board):
        return None
    
    for i in range(3):
        # if X won
        if all(board[i][j] == X for j in range(3)) or \
            all(board[j][i] == X for j in range(3)) or \
            all(board[j][j] == X for j in range(3)) or \
            all(board[j][2-j] == X for j in range(3)):
            return X
        # if O won
        elif all(board[i][j] == O for j in range(3)) or \
            all(board[j][i] == O for j in range(3)) or \
            all(board[j][j] == O for j in range(3)) or \
            all(board[j][2-j] == O for j in range(3)):
            return O
    
    # if game has terminated
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
    
    Available Functions:
    initial_state(): returns initial state
    player(board): returns which player plays next
    actions(board): returns all actions in (i, j) format
    result(board, action): returns resultant board
    winner: returns winner player | 
    terminal(board): tells if game has ended
    utility(board): 1 if X win, -1 if O won, 0 otherwise | assumes terminated

    returns None if terminal board
    
    X is the Maximizing player
    O is the Minimizing player
    """

    # Maximizing Player
    if player(board) == X:
        score = []
        for action in actions(board):
            res = result(board, action)
            u = utility(res)
            if terminal(res):
                if u == 1:
                    return action
                else:
                    score.append((u, action))
            else:
                u = uminimax(res)
                score.append((u, action))
        return max(score, key=lambda x: x[0])[1]
    # Minimizing Player
    elif player(board) == O:
        score = []
        for action in actions(board):
            res = result(board, action)
            u = utility(res)
            if terminal(res):
                if u == -1:
                    return action
                else:
                    score.append((u, action))
            else:
                u = uminimax(res)
                score.append((u, action))
        return min(score, key=lambda x: x[0])[1]
    else:
        return None


def uminimax(board):
    # Maximizing Player
    if player(board) == X:
        score = []
        for action in actions(board):
            res = result(board, action)
            if terminal(res):
                u = utility(res)
                if u == 1:
                    return u
                else:
                    score.append(u)
            else:
                u = uminimax(res)
                score.append(u)
        return max(score)
    # Minimizing Player
    elif player(board) == O:
        score = []
        for action in actions(board):
            res = result(board, action)
            if terminal(res):
                u = utility(res)
                if u == -1:
                    return u
                else:
                    score.append(u)
            else:
                u = uminimax(res)
                score.append(u)
        return min(score)
    else:
        return 0