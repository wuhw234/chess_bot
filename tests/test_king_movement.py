import unittest
from pieces.king import King
from pieces.rook import Rook
from board import Board

class TestSum(unittest.TestCase):
    
    def test_no_movement(self):
        board = Board()

        king = King("W", 0, 0, board)
        rook1 = Rook("B", 7, 1, board)
        rook2 = Rook("B", 1, 7, board)

        board.add_piece(king, 0, 0)
        board.add_piece(rook1, 7, 1)
        board.add_piece(rook2, 1, 7)

        self.assertEqual(king.generate_legal_moves(), [], "Should be empty array")

    def test_capture(self):
        board = Board()

        king = King("W", 0, 0, board)
        rook1 = Rook("B", 1, 1, board)

        board.add_piece(king, 0, 0)
        board.add_piece(rook1, 1, 1)

        self.assertEqual(king.generate_legal_moves(), [(1, 1)], "Should be [1, 1]")

    def test_full_range(self):
        board = Board()

        king = King("W", 1, 1, board)
        board.add_piece(king, 1, 1)

        self.assertEqual(king.generate_legal_moves(), 
                        [(2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0)],
                         "Should be [(2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0)]")


if __name__ == '__main__':
    unittest.main()