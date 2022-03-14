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
        self.turn = "W"
        self.board = Board()
        self.movelog = []

    def get_turn(self):
        return self.turn

    #TODO
    def log_move(self, piece, start_row, start_column, end_row, end_column):
        successful = self.board.make_move(piece, start_row, start_column, end_row, end_column)
        if successful:
            start_piece = piece
            end_square = self.board.get_square(end_row, end_column)
            if end_square:
                end_piece = end_square
            else:
                end_piece = None
            self.movelog.append([[start_piece, end_piece], 
                                [(start_row, start_column), (end_row, end_column)]])
            self.turn = "W" if self.turn == "B" else "B"

            return True
        return False


    def get_board(self):
        return self.board

    def is_checked(self):
        if self.turn == "W":
            return self.board.white_king.is_attacked()
        else:
            return self.board.black_king.is_attacked()

    def is_checkmated(self):
        if self.turn == "W":
            if self.is_checked() and not self.board.get_all_legal_moves("W"):
                return True
            return False
        else:
            if self.is_checked() and not self.board.get_all_legal_moves("B"):
                return True
            return False

    def is_stalemated(self, color):
        pass

    def __str__(self):
        pass

