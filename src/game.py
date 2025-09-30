# src/game.py

class TicTacToe:
    def __init__(self):
        """Khởi tạo bàn cờ 3x3 trống"""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # X luôn đi trước

    def reset(self):
        """Đặt lại bàn cờ mới"""        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display(self):
        """In bàn cờ (phục vụ CLI)"""
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row: int, col: int) -> bool:
        """
        Đặt quân của current_player vào ô (row, col).
        Trả về True nếu hợp lệ, False nếu không.
        """
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        """Đổi lượt"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self) -> str | None:
        """
        Kiểm tra thắng cuộc:
        - Trả về "X" hoặc "O" nếu có người thắng
        - Trả về "Draw" nếu hòa
        - Trả về None nếu chưa kết thúc
        """
        lines = []

        # Hàng ngang
        lines.extend(self.board)
        # Hàng dọc
        lines.extend([[self.board[r][c] for r in range(3)] for c in range(3)])
        # Đường chéo
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2 - i] for i in range(3)])

        for line in lines:
            if line.count(line[0]) == 3 and line[0] != " ":
                return line[0]

        # Kiểm tra hòa
        if all(cell != " " for row in self.board for cell in row):
            return "Draw"

        return None

    def get_available_moves(self) -> list[tuple[int, int]]:
        """Trả về danh sách các nước đi hợp lệ (ô trống)"""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]

