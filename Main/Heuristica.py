import random
import game


class BotHeuristic:
    def make_move(self, board, player):
        return self.best_move(board, player)

    def best_move(self, board, player):
        best_score = float("-inf")
        best_move = None
        for move in game.valid_moves(board):
            new_board = [row[:] for row in board]
            game.apply_move(new_board, move, player)
            score = self.evaluate_board(new_board, player)
            score += random.uniform(-0.1, 0.1)  # Añadir componente aleatorio
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def evaluate_board(self, board, player):
        winner = game.get_winner(board)
        if winner == player:
            return 1
        elif winner == 3 - player:
            return -1
        else:
            return 0
