from .piece import Piece

class Knight(Piece):

    """
    Class that represents a Knight.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    def generate_legal_moves(self):
        possible_moves = []

        for row_offset, col_offset in self.offsets:
            curr_row, curr_column = self.row + row_offset, self.column + col_offset

            if curr_row < 0 or curr_row >= 8 or curr_column < 0 or curr_column >= 8:
                continue
            elif self.board.is_occupied(curr_row, curr_column):
                if self.board.get_piece_color(curr_row, curr_column) != self.color:
                    possible_moves.append((curr_row, curr_column))
            else:
                possible_moves.append((curr_row, curr_column))
        
        return possible_moves
        
    def __str__(self):
        return f"""
        Knight. Coordinates: [{self.row}][{self.column}]
        """