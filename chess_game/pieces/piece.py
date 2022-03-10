
class Piece:

    """
    Represents a piece on the chess board.
    """

    def __init__(self, color, column, row, board):
        self.color = color
        self.column = column
        self.row = row
        self.board = board
        self.offsets = []

    def generate_legal_moves(self):
        possible_moves = []
        possible_captures = []
        curr_row, curr_column = self.row, self.column

        for x_offset, y_offset in self.offsets:
            curr_row, curr_column = curr_row + y_offset, curr_column + x_offset
            while curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if self.board[curr_row][curr_column]:
                    possible_captures.append((curr_row, curr_column))
                    break
                else:
                    possible_moves.append((curr_row, curr_column))
                    curr_row, curr_column = curr_row + y_offset, curr_column + x_offset

            curr_row, curr_column = self.row, self.column
        
        return (possible_moves, possible_captures)

    def move(self, new_column, new_row):
        self.column = new_column
        self.row = new_row
    
    def can_move(self):
        pass

    def is_white(self):
        return self.color == True




    
