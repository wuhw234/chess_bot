from .piece import Piece

class King(Piece):

    """
    Class that represents a king.
    """

    def __init__(self, color, row, column, board, rooks):
        Piece.__init__(self, color, row, column, board)
        self.offsets = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
        self.rooks = rooks

    def generate_legal_moves(self, king, prev_move):
        possible_moves = self.threatened_squares()
        opposite_color = "B" if self.color == "W" else "W"
        
        enemy_threatened_squares = self.board.get_threatened_squares(opposite_color)
        legal_moves = []
        for move in possible_moves:
            if move not in enemy_threatened_squares:
                legal_moves.append(move)

        self.castle(king, legal_moves, enemy_threatened_squares)

        return legal_moves

    def castle(self, king, legal_moves, enemy_threatened_squares):
        if not king.get_has_moved() and (self.row, self.column) not in enemy_threatened_squares:
            for rook in self.rooks:
                if rook.get_has_moved() or rook.is_killed():
                    continue
                rook_column = rook.get_column()
                king_column = king.get_column()
                can_castle = True

                #adapt for chess 960
                #queenside
                if king_column < rook_column:
                    for column in range(king_column + 1, king_column + 3):
                        if (self.row, column) in enemy_threatened_squares or \
                            self.board.is_occupied(self.row, column):
                            can_castle = False
                            break
                    if can_castle:
                        legal_moves.append((self.row, king_column + 2))
                #kingside
                else:
                    for column in range(king_column - 1, king_column - 3, -1):
                        if (self.row, column) in enemy_threatened_squares or \
                            self.board.is_occupied(self.row, column):
                            can_castle = False
                            break
                    if can_castle:
                        print((self.row, king_column - 2) in enemy_threatened_squares)
                        legal_moves.append((self.row, king_column - 2))

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

    def get_rooks(self):
        return self.rooks

    def __str__(self):
        return f"""
        King. Coordinates: [{self.row}][{self.column}]
        """
    
    def get_symbol(self):
        return self.color + "k"