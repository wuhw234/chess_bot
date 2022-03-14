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
    def make_move(self, piece, start_row, start_column, end_row, end_column):
        successful = self.board.attempt_move(piece, start_row, start_column, end_row, end_column)
        
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


    def get_board(self):
        return self.board

    # def is_checked(self, color):
    #     if color == "W":
    #         return self.white_king.is_attacked()
    #     else:
    #         return self.black_king.is_attacked()

    # def is_checkmated(self, color):
    #     #criteria for checkmate: no legal moves for king to move, no legal way to take offending piece,
    #     #no legal way to block

    #     #generate all legal moves, see if anything can take the previous move's square

    #     if color == "W":
    #         if self.white_king.is_attacked() and not self.white_king.generate_legal_moves():
    #             return True
    #         return False
    #     else:
    #         if self.black_king.is_attacked() and not self.black_king.generate_legal_moves():
    #             return True
    #         return False

    def is_stalemated(self, color):
        pass

    def __str__(self):
        pass

