from .piece import Piece

class Rook(Piece):

    """
    Class that represents a Rook.
    """

    def __init__(self, color, column, row):
        Piece.__init__(self, color, column, row)

    def __str__(self):
        return f"""
        Rook. Coordinates: {self.column}{self.row}
        """