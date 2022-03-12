
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

    def move_piece(self, piece, start_row, start_column, row, column):
        if not self.is_occupied(start_row, start_column):
            return
        
        piece = self.board[start_row][start_column]
        legal_moves = piece.generate_legal_moves()

        if (row, column) not in legal_moves:
            return
            
        self.board[start_row][start_column] = 0
        self.board[row][column] = piece

    def get_threatened_squares(self, color):
        threatened_squares = set()
        for row in range(0, 8):
            for column in range(0, 8):
                if self.is_occupied(row, column) and self.get_piece_color(row, column) == color:
                    piece = self.board[row][column]
                    threatened = piece.threatened_squares()

                    for square in threatened:
                        threatened_squares.add(square)
        
        return threatened_squares

    def generate_random(self):
        pass

    def generate_standard():
        pass

    def __str__(self):
        return f"""
        {self.board}
        """
