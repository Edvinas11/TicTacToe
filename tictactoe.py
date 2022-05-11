"""
Tic Tac Toe Player
"""

# imports
import math
import copy

X = "X"
O = "O"
EMPTY = None
move = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    count_EMPTY = 0

    # Check board and count X, O and EMPTY.
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)
        count_EMPTY += row.count(EMPTY)

    # If board has more X, then it is O turn. Otherwise, it is X turn.
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                possible_actions.add((row, column))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    column = action[1]

    if row not in [0, 1, 2] and column not in [0, 1, 2]:
        raise Exception("Not valid action.")

    # Make a copy of board
    board_copy = copy.deepcopy(board)
    # Make a change to a board
    board_copy[row][column] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]

    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]

    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    # Tie
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


# MINIMAX algorithm
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == "X":
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    for action in actions(board):
        x, player_action = min_value(result(board, action))
        if x > v:
            v = x
            move = action
        # If value equals 1, then return optimal move
        if v == 1:
            return v, move

    # Return optimal option
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    for action in actions(board):
        x, player_action = max_value(result(board, action))
        if x < v:
            v = x
            move = action
        # If value equals -1, then return optimal move
        if v == -1:
            return v, move

    # Return optimal option
    return v, move
