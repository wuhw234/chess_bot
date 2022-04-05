from tracemalloc import start
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
        self.score = 0
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
        piece_values = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
        prev_move = None if not self.movelog else self.movelog[-1]
        start_piece = piece
        end_square = self.board.get_square(end_row, end_column)
        if end_square:
            end_piece = end_square
        else:
            end_piece = 0
        restore_piece = self.board.make_move(prev_move, piece, start_row, 
                                          start_column, end_row, end_column)
        if restore_piece:
            multiplier = 1 if self.turn == "W" else -1
            if restore_piece == 1:
                pass
            elif restore_piece.get_symbol()[1] == "p":
                self.score += multiplier * 1 
            elif restore_piece.get_symbol()[1] == "q":
                self.score += multiplier * 8
            if end_square: #capture enemy pieces
                color = end_square.get_color()[0]
                if color != self.turn:
                    symbol = end_square.get_symbol()[1]
                    piece_value = piece_values[symbol]
                    self.score += multiplier * piece_value
            #end row and end column could be different depending on castling
            if piece.get_symbol()[1] == "k":
                end_row, end_column = piece.get_location()
            self.movelog.append([[start_piece, end_piece], 
                                [(start_row, start_column), (end_row, end_column)], 
                                restore_piece])
            self.turn = "W" if self.turn == "B" else "B"

            return True
        return False

    def undo_move(self):
        #castling: get rook, return to previous location, get king, return to previous location
        #en passant: get captured pawn, return to previous location
        #promotion: if previous move pawn and queen is returned, put start piece back, remove 1 ahead of it
        #standard: restore captured piece, restore current piece
        #make sure to undo move in prev_moves array
        if not self.movelog:
            return False

        self.turn = "W" if self.turn == "B" else "B"
        multiplier = 1 if self.turn == "W" else -1
        piece_values = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
        prev_move = self.movelog.pop()
        start_piece, end_piece = prev_move[0]
        start_row, start_column = prev_move[1][0]
        end_row, end_column = prev_move[1][1]
        restore_piece = prev_move[2]

        #standard
        if restore_piece == 1:
            pass

        #castling
        elif restore_piece.get_symbol()[1] == "r":
            self.board.add_piece(0, end_row, end_column)
            prev_row, prev_column = restore_piece.get_row(), restore_piece.get_column()
            self.board.add_piece(0, prev_row, prev_column)

            self.board.add_piece(start_piece, start_row, start_column)
            rook_row, rook_column = restore_piece.get_prev_location()
            self.board.add_piece(restore_piece, rook_row, rook_column)
            start_piece.get_prev_location()

            return True

        #en passant and promotion
        elif restore_piece.get_symbol()[1] == "p":
            if end_row == 7 or end_row == 0:
                self.score -= multiplier * 8
                pawn_row, pawn_column = restore_piece.get_prev_location()
                self.board.add_piece(0, end_row, end_column)
                self.board.add_piece(restore_piece, pawn_row, pawn_column)
                self.board.add_piece(end_piece, end_row, end_column)
                if end_piece:
                    value = multiplier * piece_values[end_piece.get_symbol()[1]]
                    self.score -= value
                return True
            #en passant
            else:
                self.score -= multiplier * 1
                self.board.add_piece(restore_piece, restore_piece.get_row(), restore_piece.get_column())
        
        self.board.add_piece(start_piece, start_row, start_column)
        self.board.add_piece(end_piece, end_row, end_column)
        if end_piece:
            value = multiplier * piece_values[end_piece.get_symbol()[1]]
            self.score -= value

        start_piece.get_prev_location()

        return True

    def get_prev_move(self):
        if not self.movelog:
            return None
        return self.movelog[-1]

    def get_board(self):
        return self.board

    def evaluate(self):
        return self.score

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

