import unittest
from pieces.knight import Knight
from board import Board

class TestSum(unittest.TestCase):

    def test_no_movement(self):
        board = Board()

        knight1 = Knight("W", 0, 0, board)
        knight2 = Knight("W", 2, 1, board)
        knight3 = Knight("W", 1, 2, board)

        board.add_piece(knight1, 0, 0)
        board.add_piece(knight2, 2, 1)
        board.add_piece(knight3, 1, 2)

        self.assertEqual(knight1.generate_legal_moves(), [], "Should be empty array")

    def test_capture(self):
        board = Board()

        knight1 = Knight("W", 0, 0, board)
        knight2 = Knight("B", 2, 1, board)
        knight3 = Knight("W", 1, 2, board)

        board.add_piece(knight1, 0, 0)
        board.add_piece(knight2, 2, 1)
        board.add_piece(knight3, 1, 2)

        self.assertEqual(knight1.generate_legal_moves(), [(2, 1)], "Should be [(2, 1)]")
    
    def test_full_range(self):
        board = Board()

        knight1 = Knight("W", 2, 2, board)
        board.add_piece(knight1, 2, 2)

        (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)

        self.assertEqual(knight1.generate_legal_moves(),
                         [(4, 3), (4, 1), (0, 3), (0, 1), (3, 4), (1, 4), (3, 0), (1, 0)],
                         "Should be [(4, 3), (4, 1), (0, 3), (0, 1), (3, 4), (1, 4), (3, 0), (1, 0)]")

if __name__ == '__main__':
    unittest.main()