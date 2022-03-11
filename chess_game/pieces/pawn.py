from .piece import Piece

class Pawn(Piece):

    """
    Class that represents a Pawn.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)

    def generate_legal_moves(self):
        #if black, can move down 2 on the 7th rank
        #if white, can move up two on the 2nd rank (change this to fit array indexing)
        #if on the 7th or second rank, can promote to another piece
        #can capture diagonally
        pass

    def promote(self):
        pass

    def __str__(self):
        return f"""
        Pawn. Coordinates: [{self.row}][{self.column}]
        """