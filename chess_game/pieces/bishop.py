from .piece import Piece

class Bishop(Piece):

    """
    Class that represents a bishop.
    """

    def __init__(self, color, column, row):
        Piece.__init__(self, color, column, row)

    def __str__(self):
        return f"""
        Bishop. Coordinates: {self.column}{self.row}
        """