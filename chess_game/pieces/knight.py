from .piece import Piece

class Knight(Piece):

    """
    Class that represents a Knight.
    """

    def __init__(self, color, column, row, board):
        Piece.__init__(self, color, column, row, board)
        self.offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    def generate_legal_moves(self):
        possible_moves = []
        possible_captures = []

        for x_offset, y_offset in self.offsets:
            curr_row, curr_column = self.row + y_offset, self.column + x_offset

            if curr_row < 0 or curr_row >= 8 or curr_column < 0 or curr_column >= 8:
                continue
            elif self.board[curr_row][curr_column]:
                possible_captures.append((curr_row, curr_column))
            else:
                possible_moves.append((curr_row, curr_column))
                curr_row, curr_column = curr_row + y_offset, curr_column + x_offset
        
        return (possible_moves, possible_captures)

    def __str__(self):
        return f"""
        Knight. Coordinates: {self.column}{self.row}
        """