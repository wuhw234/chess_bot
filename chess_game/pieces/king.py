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
        #glitch where king can take a defended piece
        end_squares = self.threatened_squares()
        possible_moves = [(self.row, self.column, square[0], square[1]) for square in end_squares]
        opposite_color = "B" if self.color == "W" else "W"
        
        enemy_threatened_squares = self.board.get_threatened_squares(opposite_color)
        legal_moves = self.filter_checks_and_pins(king, possible_moves)

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

            #adapted for chess 960
            #queenside
            if king_column < rook_column:
                #make sure can't castle into check
                #check [?][5] and [?][4] for not being occupied - exception of occupied by
                #   king or correct rook
                #4 = rook, 5 = king
                if (self.row, 5) in enemy_threatened_squares: #make sure can't castle into check
                    continue
                #make sure final squares for rook and king are not occupied by other pieces
                if self.board.is_occupied(self.row, 4) and (self.row, 4) not in exceptions:
                    continue
                elif self.board.is_occupied(self.row, 5) and (self.row, 5) not in exceptions:
                    continue
                #make sure no pieces are inbetween king and rook
                for column in range(king_column + 1, rook_column):
                    if self.board.is_occupied(self.row, column):
                        can_castle = False
                        break
                #make sure all squares king has to move over aren't attacked
                for column in range(king_column, 6):
                    if (king_row, column) in enemy_threatened_squares:
                        can_castle = False
                        break
                if can_castle:
                    legal_moves.append((self.row, self.column, self.row, rook_column))
                    for column in range(king_column + 2, rook_column):
                        legal_moves.append((self.row, self.column, self.row, column))
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
                for column in range(king_column, 0, -1):
                    if (king_row, column) in enemy_threatened_squares:
                        can_castle = False
                        break
                if can_castle:
                    legal_moves.append((self.row, self.column, self.row, rook_column))
                    for column in range(king_column - 2, rook_column, -1):
                        legal_moves.append((self.row, self.column, self.row, column))

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
        # opposite_color = "B" if self.color == "W" else "W"
        # threatened_squares = self.board.get_threatened_squares(opposite_color)

        # if (self.row, self.column) in threatened_squares:
        #     return True
        # return False
        straight_offsets = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        king_row, king_column = self.row, self.column
        for row_offset, column_offset in straight_offsets:
            curr_row, curr_column = king_row + row_offset, king_column + column_offset
            while curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                square = self.board.get_square(curr_row, curr_column)
                if square:
                    if square.get_color() == self.color:
                        break
                    else:
                        #if opposite color and its a piece that can attack vertically
                        if square.get_symbol()[1] in "krq":
                            return True
                        else:
                            break
                curr_row, curr_column = curr_row + row_offset, curr_column + column_offset
                
        diagonal_offsets = [(1, 1), (1, -1),(-1, 1), (-1, -1)]
        king_row, king_column = self.row, self.column
        for row_offset, column_offset in diagonal_offsets:
            curr_row, curr_column = king_row + row_offset, king_column + column_offset
            while curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                square = self.board.get_square(curr_row, curr_column)
                if square:
                    if square.get_color() == self.color:
                        break
                    else:
                        #if opposite color and its a piece that can attack vertically
                        if square.get_symbol()[1] == "p":
                            if self.color == "W":
                                if curr_row == king_row + 1 and abs(curr_column - king_column) == 1:
                                    return True
                                else:
                                    break
                            else:
                                if curr_row == king_row - 1 and abs(curr_column - king_column) == 1:
                                    return True
                                else:
                                    break

                        elif square.get_symbol()[1] in "kbq":
                            return True
                        else:
                            break
                curr_row, curr_column = curr_row + row_offset, curr_column + column_offset

        knight_offsets =  [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        king_row, king_column = self.row, self.column
        for row_offset, column_offset in knight_offsets:
            curr_row, curr_column = king_row + row_offset, king_column + column_offset
            if curr_row >= 0 and curr_row < 8 and curr_column >= 0 and curr_column < 8:
                square = self.board.get_square(curr_row, curr_column)
                if square:
                    if square.get_color() != self.color:
                        #if opposite color and its a knight
                        if square.get_symbol()[1] == "n":
                            return True
                        else:
                            break

        return False
    def get_rooks(self):
        return self.rooks

    def __str__(self):
        return f"""
        King. Coordinates: [{self.row}][{self.column}]
        """
    
    def get_symbol(self):
        return self.color + "k"