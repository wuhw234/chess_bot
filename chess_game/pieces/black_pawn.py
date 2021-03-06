from .piece import Piece

class BlackPawn(Piece):

    """
    Class that represents a black Pawn.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.offsets = [(-1, 0)]
        self.capture_offsets = [(-1, 1), (-1, -1)]

    def generate_legal_moves(self, king, prev_move):
        possible_moves = []
        curr_row, curr_column = self.row, self.column

        for row_offset, column_offset in self.capture_offsets:
            curr_row, curr_column = self.row + row_offset, self.column + column_offset
            if curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if self.board.is_occupied(curr_row, curr_column) and \
                    self.board.get_piece_color(curr_row, curr_column) == "W":
                    possible_moves.append((self.row, self.column, curr_row, curr_column))

        for row_offset, column_offset in self.offsets:
            curr_row, curr_column = self.row + row_offset, self.column + column_offset
            if curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                if not self.board.is_occupied(curr_row, curr_column):
                    possible_moves.append((self.row, self.column, curr_row, curr_column))
        
        if self.row == 6 and not self.board.is_occupied(self.row - 1, self.column) and \
            not self.board.is_occupied(self.row - 2, self.column):
            possible_moves.append((self.row, self.column, self.row - 2, self.column))

        if prev_move: #en passant
            pieces = prev_move[0]
            start_row, start_column = prev_move[1][0][0], prev_move[1][0][1]
            end_row, end_column = prev_move[1][1][0], prev_move[1][1][1]
            if abs(end_row - start_row) == 2 and pieces[0].get_symbol() == "Wp" and \
                end_row == self.row and abs(end_column - self.column) == 1:
                possible_moves.append((self.row, self.column, end_row - 1, end_column))
            
        legal_moves = self.filter_checks_and_pins(king, possible_moves)
        return legal_moves
        

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
        Black Pawn. Coordinates: [{self.row}][{self.column}]
        """
    def get_symbol(self):
        return self.color + "p"