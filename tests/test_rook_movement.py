import unittest
from pieces.rook import Rook
from board import Board

class TestSum(unittest.TestCase):
    def test_no_movement(self):
        board = Board()

        rook1 = Rook("W", 0, 0, board)
        rook2 = Rook("W", 1, 0, board)
        rook3 = Rook("W", 0, 1, board)

        board.add_piece(rook1, 0, 0)
        board.add_piece(rook2, 1, 0)
        board.add_piece(rook3, 0, 1)

        self.assertEqual(rook1.generate_legal_moves(), [], "Should be empty array")
    
    def test_capture(self):
        board = Board()

        rook1 = Rook("W", 0, 0, board)
        rook2 = Rook("B", 2, 0, board)
        rook3 = Rook("W", 0, 1, board)

        board.add_piece(rook1, 0, 0)
        board.add_piece(rook2, 2, 0)
        board.add_piece(rook3, 0, 1)

        self.assertEqual(rook1.generate_legal_moves(), [(1, 0), (2, 0)], 
                        "Should be [(1, 0), (2, 0)]")

    def test_vertical(self):
        board = Board()

        rook1 = Rook("W", 4, 0, board)
        rook2 = Rook("W", 4, 1, board)

        board.add_piece(rook1, 4, 0)
        board.add_piece(rook2, 4, 1)

        self.assertEqual(rook1.generate_legal_moves(),
                        [(5, 0), (6, 0), (7, 0), (3, 0), (2, 0), (1, 0), (0, 0)], 
                        "Should be [(5, 0), (6, 0), (7, 0), (3, 0), (2, 0), (1, 0), (0, 0)]")

    def test_horizontal(self):
        board = Board()

        rook1 = Rook("W", 0, 4, board)
        rook2 = Rook("W", 1, 4, board)

        board.add_piece(rook1, 0, 4)
        board.add_piece(rook2, 1, 4)

        self.assertEqual(rook1.generate_legal_moves(),
                        [(0, 5), (0, 6), (0, 7), (0, 3), (0, 2), (0, 1), (0, 0)], 
                        "Should be [(0, 5), (0, 6), (0, 7), (0, 3), (0, 2), (0, 1), (0, 0)]")

if __name__ == '__main__':
    unittest.main()