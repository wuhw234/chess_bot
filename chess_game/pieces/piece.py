
class Piece:

    """
    Represents a piece on the chess board.
    """

    def __init__(self, color, row, column, board):
        self.color = color
        self.column = column
        self.row = row
        self.board = board
        self.offsets = []

    def generate_legal_moves(self):
        possible_moves = []
        curr_row, curr_column = self.row, self.column

        for x_offset, y_offset in self.offsets:
            curr_row, curr_column = curr_row + y_offset, curr_column + x_offset
            while curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if self.board.is_occupied(curr_row, curr_column):
                    if self.board.get_piece_color(curr_row, curr_column) != self.color:
                        possible_moves.append((curr_row, curr_column))
                    break
                else:
                    possible_moves.append((curr_row, curr_column))      
                    curr_row, curr_column = curr_row + y_offset, curr_column + x_offset

            curr_row, curr_column = self.row, self.column
        
        return possible_moves

    def threatened_squares(self):
        possible_moves = []
        curr_row, curr_column = self.row, self.column

        for x_offset, y_offset in self.offsets:
            curr_row, curr_column = curr_row + y_offset, curr_column + x_offset
            while curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if self.board.is_occupied(curr_row, curr_column):
                    possible_moves.append((curr_row, curr_column))
                    break
                else:
                    possible_moves.append((curr_row, curr_column))      
                    curr_row, curr_column = curr_row + y_offset, curr_column + x_offset

            curr_row, curr_column = self.row, self.column
        
        return possible_moves

    def get_color(self):
        return self.color

    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column

    def set_row(self, new_row):
        self.row = new_row

    def set_column(self, new_column):
        self.column = new_column



    
