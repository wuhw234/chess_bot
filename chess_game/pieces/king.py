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

        if not (self.row, self.column) in enemy_threatened_squares and not king.get_has_moved():
            self.castle(king, legal_moves, enemy_threatened_squares)

        return legal_moves

    def castle(self, king, legal_moves, enemy_threatened_squares):
        for rook in self.rooks:
            if rook.get_has_moved() or rook.is_killed():
                continue

            rook_row = rook.get_row()
            rook_column = rook.get_column()
            king_column = king.get_column()
            king_row = king.get_row()
            exceptions = [(rook_row, rook_column), (king_row, king_column)]
            can_castle = True

            #adapt for chess 960
            #queenside
            if king_column < rook_column:
                #make sure can't castle into check
                #check [?][5] and [?][4] for not being occupied - exception of occupied by
                #   king or correct rook
                #4 = rook, 5 = king
                if (self.row, 5) in enemy_threatened_squares:
                    continue
                if self.board.is_occupied(self.row, 4) and (self.row, 4) not in exceptions:
                    continue
                elif self.board.is_occupied(self.row, 5) and (self.row, 5) not in exceptions:
                    continue
                for column in range(king_column + 1, rook_column):
                    if self.board.is_occupied(self.row, column):
                        can_castle = False
                        break
                    elif column <= 5 and (king_row, column) in enemy_threatened_squares:
                        can_castle = False
                        break
                if can_castle:
                    legal_moves.append((self.row, rook_column))
                    for column in range(king_column + 2, rook_column):
                        legal_moves.append((self.row, column))
            #kingside
            else:
                #make sure can't castle into check
                # check [?][1] and [?][2] for not being occupied
                #2 = rook, 1 = king
                if (self.row, 1) in enemy_threatened_squares:
                    continue
                elif self.board.is_occupied(self.row, 1) and (self.row, 1) not in exceptions:
                    continue
                elif self.board.is_occupied(self.row, 2) and (self.row, 2) not in exceptions:
                    continue
                for column in range(king_column - 1, rook_column, -1):
                    if self.board.is_occupied(self.row, column):
                        can_castle = False
                        break
                    elif column >= 1 and (king_row, column) in enemy_threatened_squares:
                        can_castle = False
                        break
                if can_castle:
                    legal_moves.append((self.row, rook_column))
                    for column in range(king_column - 2, rook_column, -1):
                        legal_moves.append((self.row, column))

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