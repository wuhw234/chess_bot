from .piece import Piece

class Queen(Piece):

    """
    Class that represents a Queen.
    """

    def __init__(self, color, column, row, board):
        Piece.__init__(self, color, column, row, board)
        self.offsets = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (0, -1)]

    def __str__(self):
        return f"""
        Queen. Coordinates: {self.column}{self.row}
        """