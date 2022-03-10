from .piece import Piece

class Rook(Piece):

    """
    Class that represents a Rook.
    """

    def __init__(self, color, column, row, board):
        Piece.__init__(self, color, column, row, board)
        self.offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __str__(self):
        return f"""
        Rook. Coordinates: {self.column}{self.row}
        """