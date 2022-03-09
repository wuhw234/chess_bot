
class Board:

    """
    Board class that represents the current state of the board
    """

    def __init__(self):
        self.board = [[-1] * 8 for i in range(0, 8)]
        self.generate_pieces()

    def generate_pieces(self):
        pass

    def __str__(self):
        return f"""
        {self.board}
        """
