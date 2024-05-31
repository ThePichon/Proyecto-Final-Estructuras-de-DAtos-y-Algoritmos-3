# Querido Pichon, este es un ejemplo que hice de cómo funciona el juego
def initialize_board():
    return [[0] * 5 for _ in range(5)]


def is_game_over(board):
    winner = get_winner(board)
    if winner is not None:
        return True
    return all(cell != 0 for row in board for cell in row)


def apply_move(board, move, player):
    x, y, direction = move
    if direction == "R":
        temp = board[x][y]
        for i in range(y, 4):
            board[x][i] = board[x][i + 1]
        board[x][4] = player
    elif direction == "L":
        temp = board[x][y]
        for i in range(y, 0, -1):
            board[x][i] = board[x][i - 1]
        board[x][0] = player
    elif direction == "U":
        temp = board[x][y]
        for i in range(x, 0, -1):
            board[i][y] = board[i - 1][y]
        board[0][y] = player
    elif direction == "D":
        temp = board[x][y]
        for i in range(x, 4):
            board[i][y] = board[i + 1][y]
        board[4][y] = player
    board[x][y] = temp


def get_winner(board):
    for player in [1, 2]:
        for row in board:
            if all(cell == player for cell in row):
                return player
        for col in zip(*board):
            if all(cell == player for cell in col):
                return player
        if all(board[i][i] == player for i in range(5)) or all(
            board[i][4 - i] == player for i in range(5)
        ):
            return player
    return None


def valid_moves(board):
    moves = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                for direction in ["R", "L", "U", "D"]:
                    moves.append((i, j, direction))
    return moves


def is_valid_move(board, move, player):
    x, y, direction = move
    if not (0 <= x < 5 and 0 <= y < 5):
        return False
    if direction not in ["R", "L", "U", "D"]:
        return False
    return True
