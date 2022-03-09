from .piece import Piece

class Queen(Piece):

    """
    Class that represents a Queen.
    """

    def __init__(self, color, column, row):
        Piece.__init__(self, color, column, row)

    def __str__(self):
        return f"""
        Queen. Coordinates: {self.column}{self.row}
        """