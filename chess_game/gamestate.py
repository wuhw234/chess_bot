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
        #if memory becomes a problem, make it so that movelog only contains most recent

    def get_turn(self):
        return self.turn

    def reset(self, color, type):
        if type == 1:
            self.board.generate_standard()
        elif type == 2:
            self.board.generate_960()
        self.movelog = []
        self.turn = "W"

    def log_move(self, piece, start_row, start_column, end_row, end_column):
        prev_move = None if not self.movelog else self.movelog[-1]
        restore_piece = self.board.make_move(prev_move, piece, start_row, 
                                          start_column, end_row, end_column)
        if restore_piece:
            #end row and end column could be different depending on castling
            if piece.get_symbol()[1] == "k":
                end_row, end_column = piece.get_location()

            start_piece = piece
            end_square = self.board.get_square(end_row, end_column)
            if end_square:
                end_piece = end_square
            else:
                end_piece = None
            self.movelog.append([[start_piece, end_piece], 
                                [(start_row, start_column), (end_row, end_column)], 
                                restore_piece])
            self.turn = "W" if self.turn == "B" else "B"

            return True
        return False

    def undo_move():
        #have to consider that we have to undo whether pieces are moved or killed
        #have to identify previous move as castling
        #problem: we have to know whether to revert piece "has moved" to true or false
        #solution: maybe make a undo move function on piece itself storing its previous locations
        #castling: get rook, return to previous location, get king, return to previous location
        #en passant: get captured pawn, return to previous location
        #promotion: if previous move pawn and queen is returned, put start piece back, remove 1 ahead of it
        #standard: restore captured piece, restore current piece
        pass

    def get_prev_move(self):
        if not self.movelog:
            return None
        return self.movelog[-1]

    def get_board(self):
        return self.board

    def is_check(self):
        if self.turn == "W":
            return self.board.white_king.is_attacked()
        else:
            return self.board.black_king.is_attacked()

    def is_checkmate(self):
        prev_move = None if not self.movelog else self.movelog[-1]
        if self.turn == "W":
            if self.is_check() and not self.board.get_all_legal_moves(prev_move, "W"):
                return True
            return False
        else:
            if self.is_check() and not self.board.get_all_legal_moves(prev_move, "B"):
                return True
            return False

    def is_stalemate(self):
        prev_move = None if not self.movelog else self.movelog[-1]
        if self.turn == "W":
            if not self.is_check() and not self.board.get_all_legal_moves(prev_move, "W"):
                return True
            return False
        else:
            if not self.is_check() and not self.board.get_all_legal_moves(prev_move, "B"):
                return True
            return False

    def __str__(self):
        pass

