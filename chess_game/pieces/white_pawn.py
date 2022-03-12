from .piece import Piece

class WhitePawn(Piece):

    """
    Class that represents a white Pawn.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.capture_offset = [(1, 1), (1, -1)]
        self.offset = [(1, 0)]

    def generate_legal_moves(self):
        possible_moves = []
        curr_row, curr_column = self.row, self.column
        
        pass

    def threatened_squares(self):
        pass

    def promote(self):
        pass

    def __str__(self):
        return f"""
        Pawn. Coordinates: [{self.row}][{self.column}]
        """
    
    def get_symbol(self):
        return self.color + "p"