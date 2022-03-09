from .piece import Piece

class Knight(Piece):

    """
    Class that represents a Knight.
    """

    def __init__(self, color, column, row):
        Piece.__init__(self, color, column, row)

    def __str__(self):
        return f"""
        Knight. Coordinates: {self.column}{self.row}
        """