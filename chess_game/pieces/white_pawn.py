from .piece import Piece

class WhitePawn(Piece):

    """
    Class that represents a white Pawn.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.capture_offsets = [(1, 1), (1, -1)]
        self.offsets = [(1, 0)]

    def generate_legal_moves(self):
        possible_moves = []
        curr_row, curr_column = self.row, self.column

        for row_offset, column_offset in self.capture_offsets:
            curr_row, curr_column = self.row + row_offset, self.column + column_offset
            if curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if self.board.is_occupied(curr_row, curr_column) and \
                    self.board.get_piece_color(curr_row, curr_column) == "B":
                    possible_moves.append((curr_row, curr_column))
                    
        for row_offset, column_offset in self.offsets:
            curr_row, curr_column = self.row + row_offset, self.column + column_offset
            if curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if not self.board.is_occupied(curr_row, curr_column):
                    possible_moves.append((curr_row, curr_column))

        if self.row == 1 and not self.board.is_occupied(self.row + 1, self.column) and \
            not self.board.is_occupied(self.row + 2, self.column):
            possible_moves.append((self.row + 2, self.column))
        
        return possible_moves
        

    def threatened_squares(self):
        possible_moves = []
        curr_row, curr_column = self.row, self.column

        for row_offset, column_offset in self.capture_offsets:
            curr_row, curr_column = self.row + row_offset, self.column + column_offset
            if curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                possible_moves.append((curr_row, curr_column))
        return possible_moves

    def promote(self):
        pass

    def __str__(self):
        return f"""
        White Pawn. Coordinates: [{self.row}][{self.column}]
        """
    
    def get_symbol(self):
        return self.color + "p"