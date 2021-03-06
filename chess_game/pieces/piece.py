
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
        self.prev_squares = []
        self.killed = False

    def generate_legal_moves(self, king, prev_move):
        possible_moves = []
        curr_row, curr_column = self.row, self.column

        for x_offset, y_offset in self.offsets:
            curr_row, curr_column = curr_row + y_offset, curr_column + x_offset
            while curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if self.board.is_occupied(curr_row, curr_column):
                    if self.board.get_piece_color(curr_row, curr_column) != self.color:
                        possible_moves.append((self.row, self.column, curr_row, curr_column))
                    break
                else:
                    possible_moves.append((self.row, self.column, curr_row, curr_column))      
                    curr_row, curr_column = curr_row + y_offset, curr_column + x_offset

            curr_row, curr_column = self.row, self.column
        
        legal_moves = self.filter_checks_and_pins(king, possible_moves)
        return legal_moves

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

    def filter_checks_and_pins(self, king, moves):
        start_row, start_column = self.get_row(), self.get_column()
        legal_moves = []
        for start_r, start_c, end_row, end_column in moves:
            end_piece = self.board.get_square(end_row, end_column)
            self.board.add_piece(0, start_row, start_column)
            self.board.add_piece(self, end_row, end_column)
            self.set_row(end_row)
            self.set_column(end_column)

            if not king.is_attacked(): #undo the move
                legal_moves.append((start_row, start_column, end_row, end_column))
            self.board.add_piece(self, start_row, start_column)
            self.board.add_piece(end_piece, end_row, end_column)
            self.set_row(start_row)
            self.set_column(start_column)

        return legal_moves

    def get_color(self):
        return self.color

    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column

    def get_location(self):
        return (self.row, self.column)

    def set_row(self, new_row):
        self.row = new_row

    def set_column(self, new_column):
        self.column = new_column

    def set_location(self, new_row, new_column):
        self.row = new_row
        self.column = new_column

    def add_prev_location(self, row, column):
        self.prev_squares.append((row, column))

    def get_prev_location(self):
        if self.prev_squares:
            return self.prev_squares.pop()
        return False

    def undo_move(self):
        if not self.prev_squares:
            return False
        prev_row, prev_column = self.prev_squares.pop()
        self.row, self.column = prev_row, prev_column
        return True

    def get_has_moved(self):
        return True if self.prev_squares else False

    def set_killed(self, killed):
        self.killed = killed

    def is_killed(self):
        return self.killed



    
