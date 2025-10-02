from .game import TicTacToe

def ai_alpha_beta(board: TicTacToe, depth: int, alpha: int, beta: int, is_ai: bool):
    check_winner = board.check_winner()
    if check_winner == "X":      # Người thắng
        return -10 - depth
    elif check_winner == "O":    # AI thắng
        return 10 - depth
    elif check_winner == "Draw":
        return 0
    
    # Lượt AI (O) - MAX
    if is_ai:
        best_value = -float("inf")
        for pos in board.get_available_moves():
            # Xử lý pos -> (row, col)
            if isinstance(pos, tuple):   # nếu get_available_moves trả (row, col)
                row, col = pos
            else:                        # nếu trả index 0..8
                row, col = divmod(pos, 3)

            new_board = board.copy_board("O")
            new_board.make_move(row, col)
            new_board.switch_player()

            value = ai_alpha_beta(new_board, depth+1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if alpha >= beta:   # cắt tỉa
                break
        return best_value

    # Lượt Người (X) - MIN
    else:
        best_value = float("inf")
        for pos in board.get_available_moves():
            # Xử lý pos -> (row, col)
            if isinstance(pos, tuple):
                row, col = pos
            else:
                row, col = divmod(pos, 3)

            new_board = board.copy_board("X")
            new_board.make_move(row, col)
            new_board.switch_player()

            value = ai_alpha_beta(new_board, depth+1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:   # cắt tỉa
                break
        return best_value


class AIAlphaBeta:
    def __init__(self, board: TicTacToe):
        self.game = board.copy_board("O")

    def ai_agent(self) -> tuple:
        best_value = -float("inf")
        best_move = None

        for pos in self.game.get_available_moves():
            row, col = pos   # 👈 giải nén tuple
            new_board = self.game.copy_board("O")
            print(self.game.display())
            new_board.make_move(row, col)   
            new_board.switch_player()
            
            value = ai_alpha_beta(new_board, depth=0,
                                alpha=-float("inf"),
                                beta=float("inf"),
                                is_ai=False)
            
            if value > best_value:
                best_value = value
                best_move = pos

        return best_move

