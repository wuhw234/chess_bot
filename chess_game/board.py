
class Board:

    """
    Board class that represents the current state of the board
    """

    def __init__(self):
        self.board = [[0] * 8 for i in range(0, 8)]

    def add_piece(self, piece, row, column):
        self.board[row][column] = piece

    def is_occupied(self, row, column):
        return self.board[row][column] != 0

    def get_piece_color(self, row, column):
        try:
            return self.board[row][column].get_color()
        except:
            print("Square is not occupied!")

    def move_piece(self, piece, row, column):
        self.board[row][column] = piece

    def generate_random(self):
        pass

    def generate_standard():
        pass

    def __str__(self):
        return f"""
        {self.board}
        """
