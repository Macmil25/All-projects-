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


# --- Required Functions ---

def player(board):
    """
    Returns player who has the next turn on a board.
    X gets the first move.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # X always goes first. If X has more moves than O, it's O's turn.
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    (i, j) is the row and column index of an EMPTY cell.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid Action: Cell is already occupied or action is out of bounds.")

    # Create a deep copy of the board to ensure the original board is unmodified
    new_board = copy.deepcopy(board)
    current_player = player(board)

    # Perform the move
    i, j = action
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Returns X, O, or None.
    """

    # Helper to check for a winner (three in a line)
    def check_line(p1, p2, p3):
        if p1 == p2 == p3 and p1 != EMPTY:
            return p1
        return None

    # Check Horizontal and Vertical Wins
    for i in range(3):
        # Horizontal Check (row i)
        if (win := check_line(board[i][0], board[i][1], board[i][2])):
            return win
        # Vertical Check (column i)
        if (win := check_line(board[0][i], board[1][i], board[2][i])):
            return win

    # Check Diagonal Wins
    # 1. Top-Left to Bottom-Right
    if (win := check_line(board[0][0], board[1][1], board[2][2])):
        return win
    # 2. Top-Right to Bottom-Left
    if (win := check_line(board[0][2], board[1][1], board[2][0])):
        return win

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    Game is over if someone has won OR if all cells are filled (a tie).
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if there are any remaining empty cells
    for row in board:
        if EMPTY in row:
            return False  # Game is still in progress

    # If no winner and no empty cells, it's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise (tie).
    Assumes board is terminal.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:  # Tie
        return 0


# --- Minimax Helper Functions ---

def max_value(board):
    """
    Minimax component for the maximizing player (X).
    Returns (score, action) tuple.
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None

    # Iterate over all possible moves
    for action in actions(board):
        # The maximizing player wants the highest score returned by the minimizing player
        min_val, _ = min_value(result(board, action))

        if min_val > v:
            v = min_val
            best_action = action

        # Alpha-beta pruning (optional but efficient)
        # In the context of max_value, if we find a move that guarantees a score of 1, we can stop immediately
        if v == 1:
            return v, best_action

    return v, best_action


def min_value(board):
    """
    Minimax component for the minimizing player (O).
    Returns (score, action) tuple.
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None

    # Iterate over all possible moves
    for action in actions(board):
        # The minimizing player wants the lowest score returned by the maximizing player
        max_val, _ = max_value(result(board, action))

        if max_val < v:
            v = max_val
            best_action = action

        # Alpha-beta pruning (optional but efficient)
        # In the context of min_value, if we find a move that guarantees a score of -1, we can stop immediately
        if v == -1:
            return v, best_action

    return v, best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    # X is the maximizing player
    if current_player == X:
        # We only care about the action, discard the score
        _, optimal_action = max_value(board)
        return optimal_action

    # O is the minimizing player
    elif current_player == O:
        # We only care about the action, discard the score
        _, optimal_action = min_value(board)
        return optimal_action

    return None
    
    

