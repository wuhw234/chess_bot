from .piece import Piece

class Queen(Piece):

    """
    Class that represents a Queen.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.offsets = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    def __str__(self):
        return f"""
        Queen. Coordinates: [{self.row}][{self.column}]
        """
    
    def get_symbol(self):
        return self.color + "q"