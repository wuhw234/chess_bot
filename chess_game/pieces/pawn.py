from .piece import Piece

class Pawn(Piece):

    """
    Class that represents a Pawn.
    """

    def __init__(self, color, column, row, board):
        Piece.__init__(self, color, column, row, board)

    def generate_legal_moves(self):
        pass

    def promote(self):
        pass

    def __str__(self):
        return f"""
        Pawn. Coordinates: {self.column}{self.row}
        """