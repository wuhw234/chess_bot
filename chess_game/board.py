from pieces.bishop import Bishop
from pieces.black_pawn import BlackPawn
from pieces.white_pawn import WhitePawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King

import random

DIMENSION = 8

class Board:

    """
    Board class that represents the current state of the board
    """

    def __init__(self):
        self.board = [[0] * DIMENSION for i in range(0, DIMENSION)]
        self.generate_standard()

    def add_piece(self, piece, row, column):
        self.board[row][column] = piece
        if piece:
            piece.set_location(row, column)
    
    def add_pieces(self, pieces):
        for piece in pieces:
            row, column = piece.get_row(), piece.get_column()
            self.board[row][column] = piece

    def is_occupied(self, row, column):
        return self.board[row][column] != 0

    def get_piece_color(self, row, column):
        try:
            return self.board[row][column].get_color()
        except:
            print("Square is not occupied!")
    
    def get_square(self, row, column):
        return self.board[row][column]

    # def evaluate(self):
    #     piece_values = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
    #     score = 0
    #     for i in range(0, DIMENSION):
    #         for j in range(0, DIMENSION):
    #             if self.board[i][j]:
    #                 symbol = self.board[i][j].get_symbol()
    #                 if symbol[0] == "W":
    #                     score += piece_values[symbol[1]]
    #                 else:
    #                     score -= piece_values[symbol[1]]

    #     return score

    def make_move(self, prev_move, piece, start_row, start_column, end_row, end_column):
        #check for invalid moves
        
        if not self.is_occupied(start_row, start_column) or not piece:
            return False
        
        king = self.white_king if piece.get_color() == "W" else self.black_king
        legal_moves = piece.generate_legal_moves(king, prev_move)

        symbol = piece.get_symbol()
        end_piece = self.get_square(end_row, end_column)
        if (start_row, start_column, end_row, end_column) not in legal_moves:
            return False

        #valid moves _____________________________________________________________________

        #account for en passant here: if pawn moved off original column and there's no piece
        #at destination, then remove pawn above it

        elif not self.is_occupied(end_row, end_column) and piece.get_symbol()[1] == "p" and \
            start_column != end_column:
            if piece.get_symbol()[0] == "W":
                enemy_pawn = self.get_square(end_row - 1, end_column)
                self.add_piece(0, end_row - 1, end_column)

                self.add_piece(0, start_row, start_column)
                piece.add_prev_location(piece.get_row(), piece.get_column())
                self.add_piece(piece, end_row, end_column)
            else:
                enemy_pawn = self.get_square(end_row + 1, end_column)
                self.add_piece(0, end_row + 1, end_column)

                self.add_piece(0, start_row, start_column)
                piece.add_prev_location(piece.get_row(), piece.get_column())
                self.add_piece(piece, end_row, end_column)
            return enemy_pawn

        #account for pawn promotion here
        #make it so that you move the pawn forward one square and then undo the move
        elif piece.get_symbol() == "Bp" and end_row == 0:
            self.add_piece(0, start_row, start_column)
            piece.add_prev_location(start_row, start_column)
            self.add_piece(piece, end_row, end_column)

            new_queen = Queen("B", end_row, end_column, self)
            self.add_piece(new_queen, end_row, end_column)

            return piece
        elif piece.get_symbol() == "Wp" and end_row == 7:
            self.add_piece(0, start_row, start_column)
            piece.add_prev_location(start_row, start_column)
            self.add_piece(piece, end_row, end_column)

            new_queen = Queen("W", end_row, end_column, self)
            self.add_piece(new_queen, end_row, end_column)

            return piece

        #acount for castling (adapt for 960)
        elif symbol[1] == "k" and (abs(end_column - start_column) > 1 or 
            (end_piece and end_piece.get_symbol()[0] == symbol[0])):
            king_rook, queen_rook = piece.get_rooks()[0], piece.get_rooks()[1]
            #kingside
            if end_column < start_column:
                self.add_piece(0, king_rook.get_row(), king_rook.get_column())
                self.add_piece(0, piece.get_row(), piece.get_column())

                piece.add_prev_location(piece.get_row(), piece.get_column())
                self.add_piece(piece, end_row, 1)

                king_rook.add_prev_location(king_rook.get_row(), king_rook.get_column())
                self.add_piece(king_rook, end_row, 2)

                return king_rook
            #queenside
            else:
                self.add_piece(0, queen_rook.get_row(), queen_rook.get_column())
                self.add_piece(0, piece.get_row(), piece.get_column())

                piece.add_prev_location(piece.get_row(), piece.get_column())
                self.add_piece(piece, end_row, 5)

                queen_rook.add_prev_location(queen_rook.get_row(), queen_rook.get_column())
                self.add_piece(queen_rook, end_row, 4)

                return queen_rook
        else:
            self.add_piece(0, piece.get_row(), piece.get_column())
            piece.add_prev_location(piece.get_row(), piece.get_column())
            self.add_piece(piece, end_row, end_column)
            return 1

    def get_king(self, color):
        if color == "W":
            return self.white_king
        else:
            return self.black_king

    def get_threatened_squares(self, color):
        threatened_squares = set()
        for row in range(0, DIMENSION):
            for column in range(0, DIMENSION):
                if self.is_occupied(row, column) and self.get_piece_color(row, column) == color:
                    piece = self.board[row][column]
                    threatened = piece.threatened_squares()
                    for square in threatened:
                        threatened_squares.add(square)
        
        return threatened_squares

    # def get_piece_moves(self, row, column, prev_move, color):
    #     if not self.board[row][column]:
    #         return []
        
    #     king = self.white_king if color == "W" else self.black_king
    #     piece = self.board[row][column]
    #     return piece.generate_legal_moves(king, prev_move)


    def get_all_legal_moves(self, prev_move, color):
        legal_moves = []
        king = self.white_king if color == "W" else self.black_king
        for i in range(0, DIMENSION):
            for j in range(0, DIMENSION):
                piece = self.get_square(i, j) 
                if piece and piece.get_color() == color:
                    legal_moves.extend(piece.generate_legal_moves(king, prev_move))
        return legal_moves

    def generate_standard(self):
        self.board = [[0] * DIMENSION for i in range(0, DIMENSION)]
        white_rook_1, white_rook_2 = Rook("W", 0, 0, self), Rook("W", 0, 7, self)
        white_king = King("W", 0, 3, self, [white_rook_1, white_rook_2])
        white_knight_1, white_knight_2 = Knight("W", 0, 1, self), Knight("W", 0, 6, self)
        white_bishop_1, white_bishop_2 = Bishop("W", 0, 2, self), Bishop("W", 0, 5, self)
        white_queen = Queen("W", 0, 4, self)

        white_pawns = [WhitePawn("W", 1, i, self) for i in range(0, DIMENSION)]
        white_pieces = [white_rook_1, white_rook_2, white_knight_1, white_knight_2,
                        white_bishop_1, white_bishop_2, white_queen, white_king]
        self.add_pieces(white_pieces)
        self.add_pieces(white_pawns)

        black_rook_1, black_rook_2 = Rook("B", 7, 0, self), Rook("B", 7, 7, self)
        black_king = King("B", 7, 3, self, [black_rook_1, black_rook_2])
        black_knight_1, black_knight_2 = Knight("B", 7, 1, self), Knight("B", 7, 6, self)
        black_bishop_1, black_bishop_2 = Bishop("B", 7, 2, self), Bishop("B", 7, 5, self)
        black_queen = Queen("B", 7, 4, self)

        black_pawns = [BlackPawn("B", 6, i, self) for i in range(0, DIMENSION)]
        black_pieces = [black_rook_1, black_rook_2, black_knight_1, black_knight_2,
                        black_bishop_1, black_bishop_2, black_queen, black_king]
        self.add_pieces(black_pieces)
        self.add_pieces(black_pawns)

        self.white_king = white_king
        self.black_king = black_king

    def generate_960(self):
        #TODO: make this more efficient
        self.board = [[0] * DIMENSION for i in range(0, DIMENSION)]
        #generate coordinates
        king_column = random.randint(1, 6)
        rook_1_column = random.randint(0, king_column - 1)
        rook_2_column = random.randint(king_column + 1, 7)
        available = set(i for i in range(0, 8))
        available.remove(king_column)
        available.remove(rook_1_column)
        available.remove(rook_2_column)

        bishop_1_column = self.random_but_exclude(0, 7, available)
        available.remove(bishop_1_column)
        #if bishop 1 is even, exclude even. else exclude odd
        opposite = 2 if bishop_1_column % 2 == 0 else 1
        bishop_2_column = self.random_but_exclude(0, 7, available, opposite)
        available.remove(bishop_2_column)

        knight_1_column = self.random_but_exclude(0, 7, available)
        available.remove(knight_1_column)
        knight_2_column = self.random_but_exclude(0, 7, available)
        available.remove(knight_2_column)
        queen_column = self.random_but_exclude(0, 7, available)
        available.remove(queen_column)

        #generate board
        white_rook_1, white_rook_2 = Rook("W", 0, rook_1_column, self), Rook("W", 0, rook_2_column, self)
        white_king = King("W", 0, king_column, self, [white_rook_1, white_rook_2])
        white_knight_1, white_knight_2 = Knight("W", 0, knight_1_column, self), Knight("W", 0, knight_2_column, self)
        white_bishop_1, white_bishop_2 = Bishop("W", 0, bishop_1_column, self), Bishop("W", 0, bishop_2_column, self)
        white_queen = Queen("W", 0, queen_column, self)

        white_pawns = [WhitePawn("W", 1, i, self) for i in range(0, DIMENSION)]
        white_pieces = [white_rook_1, white_rook_2, white_knight_1, white_knight_2,
                        white_bishop_1, white_bishop_2, white_queen, white_king]
        self.add_pieces(white_pieces)
        self.add_pieces(white_pawns)

        black_rook_1, black_rook_2 = Rook("B", 7, rook_1_column, self), Rook("B", 7, rook_2_column, self)
        black_king = King("B", 7, king_column, self, [black_rook_1, black_rook_2])
        black_knight_1, black_knight_2 = Knight("B", 7, knight_1_column, self), Knight("B", 7, knight_2_column, self)
        black_bishop_1, black_bishop_2 = Bishop("B", 7, bishop_1_column, self), Bishop("B", 7, bishop_2_column, self)
        black_queen = Queen("B", 7, queen_column, self)

        black_pawns = [BlackPawn("B", 6, i, self) for i in range(0, DIMENSION)]
        black_pieces = [black_rook_1, black_rook_2, black_knight_1, black_knight_2,
                        black_bishop_1, black_bishop_2, black_queen, black_king]
        self.add_pieces(black_pieces)
        self.add_pieces(black_pawns)

        self.white_king = white_king
        self.black_king = black_king
        
    #even == 0: don't care even == 1, exclude odd numbers  even == 2 exclude even numbers
    def random_but_exclude(self, low, high, available, even = 0):
        while True:
            number = random.randint(low, high)
            if ((even == 1 and number % 2 == 0) or (even == 2 and number % 2 != 0) or \
                (not even)) and number in available:
                break

        return number


    def __str__(self):
        string_board = ""
        for i in range(0, DIMENSION):
            row = ""
            for j in range(0, DIMENSION):
                if self.board[i][j]:
                    piece = self.board[i][j]
                    row += piece.get_symbol()
                    row += " "
                else:
                    row += "0  "
            row += "\n"
            string_board += row
        
        return string_board
