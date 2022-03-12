from .piece import Piece

class BlackPawn(Piece):

    """
    Class that represents a black Pawn.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)

    def generate_legal_moves(self):
        possible_moves = []
        curr_row, curr_column = self.row, self.column
        self.offset = [(-1, 1), (-1, -1)]

    def threatened_squares(self):
        pass

    def promote(self):
        pass

    def __str__(self):
        return f"""
        Pawn. Coordinates: [{self.row}][{self.column}]
        """
    def get_symbol(self):
        return self.color + "p"