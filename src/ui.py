import pygame
import sys
from game import TicTacToe
from config import *


class TicTacToeUI:
    def __init__(self):
        # Khởi tạo pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')

        self.game = TicTacToe()
        self.game_over = False

        self.screen.fill(BG_COLOR)
        self.draw_lines()
        pygame.display.update()

    def draw_lines(self):
        """Vẽ lưới"""
        # Ngang
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        # Dọc
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        """Vẽ X/O theo trạng thái bàn cờ"""
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.game.board[row][col] == "O":
                    pygame.draw.circle(self.screen, CIRCLE_COLOR,
                                       (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                        int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.game.board[row][col] == "X":
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                     CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     CROSS_WIDTH)

    def handle_click(self, pos):
        """Xử lý click chuột"""
        if self.game_over:
            return

        mouseX, mouseY = pos
        clicked_row = mouseY // SQUARE_SIZE
        clicked_col = mouseX // SQUARE_SIZE

        if self.game.make_move(clicked_row, clicked_col):
            winner = self.game.check_winner()
            if winner:
                print("Kết quả:", winner)
                self.game_over = True
            else:
                self.game.switch_player()
            self.redraw()

    def redraw(self):
        """Vẽ lại màn hình"""
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        self.draw_figures()
        pygame.display.update()

    def run(self):
        """Vòng lặp chính"""
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    self.handle_click(event.pos)


# if __name__ == "__main__":
#     ui = TicTacToeUI()
#     ui.run()
