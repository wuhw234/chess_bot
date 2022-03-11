from .piece import Piece

class King(Piece):

    """
    Class that represents a king.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.offsets = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

    def generate_possible_moves(self):
        #can't move to a threatened square by enemy
        #can't move to a occupied ally square
        #generate set of moves for all enemy pieces, generate set of possible moves for king
        #remove all possible moves that are being threatened
        possible_moves = []

        for x_offset, y_offset in self.offsets:
            curr_row, curr_column = self.row + y_offset, self.column + x_offset

            if curr_row < 0 or curr_row >= 8 or curr_column < 0 or curr_column >= 8:
                continue
            elif self.board[curr_row][curr_column]:
                possible_moves.append((curr_row, curr_column))
            else:
                possible_moves.append((curr_row, curr_column))
                curr_row, curr_column = curr_row + y_offset, curr_column + x_offset
        
        return possible_moves

    def generate_legal_moves(self):
        pass

    def get_threatened_squares(self):
        pass

    def is_attacked(self):
        pass

    def __str__(self):
        return f"""
        King. Coordinates: [{self.row}][{self.column}]
        """