from .piece import Piece

class King(Piece):

    """
    Class that represents a king.
    """

    def __init__(self, color, row, column, board):
        Piece.__init__(self, color, row, column, board)
        self.offsets = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

    def generate_legal_moves(self, king, prev_move):
        possible_moves = self.threatened_squares()
        opposite_color = "B" if self.color == "W" else "W"
        
        enemy_threatened_squares = self.board.get_threatened_squares(opposite_color)
        legal_moves = []
        for move in possible_moves:
            if move not in enemy_threatened_squares:
                legal_moves.append(move)
                

        return legal_moves

    def threatened_squares(self):
        possible_moves = []

        for row_offset, col_offset in self.offsets:
            curr_row, curr_column = self.row + row_offset, self.column + col_offset

            if curr_row < 0 or curr_row >= 8 or curr_column < 0 or curr_column >= 8:
                continue
            elif self.board.is_occupied(curr_row, curr_column):
                if self.board.get_piece_color(curr_row, curr_column) != self.color:
                    possible_moves.append((curr_row, curr_column))
            else:
                possible_moves.append((curr_row, curr_column))

        return possible_moves

    def is_attacked(self):
        opposite_color = "B" if self.color == "W" else "W"
        threatened_squares = self.board.get_threatened_squares(opposite_color)

        if (self.row, self.column) in threatened_squares:
            return True
        return False

    def __str__(self):
        return f"""
        King. Coordinates: [{self.row}][{self.column}]
        """
    
    def get_symbol(self):
        return self.color + "k"