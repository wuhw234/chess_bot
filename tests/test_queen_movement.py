import unittest
from pieces.queen import Queen
from board import Board

class TestSum(unittest.TestCase):

    def test_queen_no_movement(self):
        board = Board()
        queen1 = Queen("W", 7, 0, board)
        board.add_piece(queen1, 7, 0)

        queen2 = Queen("W", 6, 1, board)
        board.add_piece(queen2, 6, 1)

        queen3 = Queen("W", 6, 0, board)
        board.add_piece(queen3, 6, 0)

        queen4 = Queen("W", 7, 1, board)
        board.add_piece(queen4, 7, 1)

        self.assertEqual(queen1.generate_legal_moves(), [], "Should be empty array")

    def test_queen_capture(self):
        board = Board()

        queen1 = Queen("W", 7, 0, board)
        board.add_piece(queen1, 7, 0)

        queen2 = Queen("B", 6, 1, board)
        board.add_piece(queen2, 6, 1)

        queen3 = Queen("B", 6, 0, board)
        board.add_piece(queen3, 6, 0)

        queen4 = Queen("W", 7, 1, board)
        board.add_piece(queen4, 7, 1)

        self.assertEqual(queen1.generate_legal_moves(), [(6, 1), (6, 0)],
        "Should be [(6, 1), (6, 0)]")

    def test_horizontal(self):
        board = Board()

        queen1 = Queen("W", 7, 3, board)
        board.add_piece(queen1, 7, 3)

        queen2 = Queen("W", 6, 3, board)
        board.add_piece(queen2, 6, 3)

        queen3 = Queen("W", 6, 2, board)
        board.add_piece(queen3, 6, 2)

        queen4 = Queen("W", 6, 4, board)
        board.add_piece(queen4, 6, 4)

        self.assertEqual(queen1.generate_legal_moves(), 
        [(7, 4), (7, 5), (7, 6), (7, 7), (7, 2), (7, 1), (7, 0)],
        "Should be [(7, 4), (7, 5), (7, 6), (7, 7), (7, 2), (7, 1), (7, 0)]")


if __name__ == '__main__':
    unittest.main()