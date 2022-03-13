from pieces.bishop import Bishop
from pieces.black_pawn import BlackPawn
from pieces.white_pawn import WhitePawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King

DIMENSION = 8

class Board:

    """
    Board class that represents the current state of the board
    """

    def __init__(self):
        self.board = [[0] * DIMENSION for i in range(0, DIMENSION)]

    def add_piece(self, piece, row, column):
        self.board[row][column] = piece
    
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

    def move_piece(self, piece, start_row, start_column, row, column):
        print(piece, start_row, start_column, row, column)
        if not self.is_occupied(start_row, start_column) or not piece:
            return
        
        piece = self.board[start_row][start_column]
        legal_moves = piece.generate_legal_moves()

        if (row, column) not in legal_moves:
            return
            
        self.board[start_row][start_column] = 0
        self.board[row][column] = piece
        piece.set_row(row)
        piece.set_column(column)

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

    # def generate_random(self):
    #     pass

    # def generate_standard(self):
    #     white_rook_1, white_rook_2 = Rook("W", 0, 0, self.board), Rook("W", 0, 7, self.board)
    #     white_knight_1, white_knight_2 = Knight("W", 0, 1, self.board), Knight("W", 0, 6, self.board)
    #     white_bishop_1, white_bishop_2 = Bishop("W", 0, 2, self.board), Bishop("W", 0, 5, self.board)
    #     white_queen = Queen("W", 0, 4, self.board)
    #     white_king = King("W", 0, 3, self.board)

    #     white_pawns = [WhitePawn("W", 1, i, self.board) for i in range(0, DIMENSION)]
    #     white_pieces = [white_rook_1, white_rook_2, white_knight_1, white_knight_2,
    #                     white_bishop_1, white_bishop_2, white_queen, white_king]
    #     self.add_pieces(white_pieces)
    #     self.add_pieces(white_pawns)

    #     black_rook_1, black_rook_2 = Rook("B", 7, 0, self.board), Rook("B", 7, 7, self.board)
    #     black_knight_1, black_knight_2 = Knight("B", 7, 1, self.board), Knight("B", 7, 6, self.board)
    #     black_bishop_1, black_bishop_2 = Bishop("B", 7, 2, self.board), Bishop("B", 7, 5, self.board)
    #     black_queen = Queen("B", 7, 4, self.board)
    #     black_king = King("B", 7, 3, self.board)

    #     black_pawns = [BlackPawn("B", 6, i, self.board) for i in range(0, DIMENSION)]
    #     black_pieces = [black_rook_1, black_rook_2, black_knight_1, black_knight_2,
    #                     black_bishop_1, black_bishop_2, black_queen, black_king]
    #     self.add_pieces(black_pieces)
    #     self.add_pieces(black_pawns)

    def __str__(self):
        board_representation = [[0] * DIMENSION for i in range(0, DIMENSION)]
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
