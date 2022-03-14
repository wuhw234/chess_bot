from .piece import Piece

class Bishop(Piece):

    """
    Class that represents a bishop.
    """

    def __init__(self, color, row, column, king, board):
        Piece.__init__(self, color, row, column, king, board)
        self.offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __str__(self):
        return f"""
        Bishop. Coordinates: [{self.row}][{self.column}]
        """

    def get_symbol(self):
        return self.color + "b"