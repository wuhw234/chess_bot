from .piece import Piece

class King(Piece):

    """
    Class that represents a king.
    """

    def __init__(self, color, column, row):
        Piece.__init__(self, color, column, row)

    def __str__(self):
        return f"""
        King. Coordinates: {self.column}{self.row}
        """