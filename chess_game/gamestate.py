from board import Board
from pieces.bishop import Bishop
from pieces.black_pawn import BlackPawn
from pieces.white_pawn import WhitePawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King

DIMENSION = 8

class GameState:

    def __init__(self):
        self.white_turn = True
        self.board = Board()
        self.movelog = []
        self.generate_standard()

    def generate_standard(self):
        white_rook_1, white_rook_2 = Rook("W", 0, 0, self.board), Rook("W", 0, 7, self.board)
        white_knight_1, white_knight_2 = Knight("W", 0, 1, self.board), Knight("W", 0, 6, self.board)
        white_bishop_1, white_bishop_2 = Bishop("W", 0, 2, self.board), Bishop("W", 0, 5, self.board)
        white_queen = Queen("W", 0, 4, self.board)
        white_king = King("W", 0, 3, self.board)

        white_pawns = [WhitePawn("W", 1, i, self.board) for i in range(0, DIMENSION)]
        white_pieces = [white_rook_1, white_rook_2, white_knight_1, white_knight_2,
                        white_bishop_1, white_bishop_2, white_queen, white_king]
        self.board.add_pieces(white_pieces)
        self.board.add_pieces(white_pawns)

        black_rook_1, black_rook_2 = Rook("B", 7, 0, self.board), Rook("B", 7, 7, self.board)
        black_knight_1, black_knight_2 = Knight("B", 7, 1, self.board), Knight("B", 7, 6, self.board)
        black_bishop_1, black_bishop_2 = Bishop("B", 7, 2, self.board), Bishop("B", 7, 5, self.board)
        black_queen = Queen("B", 7, 4, self.board)
        black_king = King("B", 7, 3, self.board)

        black_pawns = [BlackPawn("B", 6, i, self.board) for i in range(0, DIMENSION)]
        black_pieces = [black_rook_1, black_rook_2, black_knight_1, black_knight_2,
                        black_bishop_1, black_bishop_2, black_queen, black_king]
        self.board.add_pieces(black_pieces)
        self.board.add_pieces(black_pawns)

    def get_board(self):
        return self.board

