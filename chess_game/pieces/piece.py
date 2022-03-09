
class Piece:

    """
    Represents a piece on the chess board.
    """

    def __init__(self, color, column, row):
        self.color = color
        self.column = column
        self.row = row

    def move(self, end):
        pass

    def capture(self, end):
        pass
    
    def can_move(self):
        pass

    def is_white(self):
        return self.color == True

    def get_square(self):
        return self.square




    
