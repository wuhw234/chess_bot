from .piece import Piece

class Pawn(Piece):

    """
    Class that represents a Pawn.
    """

    def __init__(self, color, column, row):
        Piece.__init__(self, color, column, row)

    def __str__(self):
        return f"""
        Pawn. Coordinates: {self.column}{self.row}
        """