import unittest
from pieces.queen import Queen
from board import Board

class TestSum(unittest.TestCase):

    def test_no_movement(self):
        board = Board()

        queen1 = Queen("W", 7, 0, board)
        queen2 = Queen("W", 6, 1, board)
        queen3 = Queen("W", 6, 0, board)
        queen4 = Queen("W", 7, 1, board)

        board.add_piece(queen1, 7, 0)
        board.add_piece(queen2, 6, 1)
        board.add_piece(queen3, 6, 0)
        board.add_piece(queen4, 7, 1)

        self.assertEqual(queen1.generate_legal_moves(), [], "Should be empty array")

    def test_capture(self):
        board = Board()

        queen1 = Queen("W", 7, 0, board)
        queen2 = Queen("B", 6, 1, board)
        queen3 = Queen("B", 6, 0, board)
        queen4 = Queen("W", 7, 1, board)

        board.add_piece(queen1, 7, 0)
        board.add_piece(queen2, 6, 1)
        board.add_piece(queen3, 6, 0)
        board.add_piece(queen4, 7, 1)

        self.assertEqual(queen1.generate_legal_moves(), [(6, 1), (6, 0)],
        "Should be [(6, 1), (6, 0)]")

    def test_horizontal(self):
        board = Board()

        queen1 = Queen("W", 7, 3, board)
        queen2 = Queen("W", 6, 3, board)
        queen3 = Queen("W", 6, 2, board)
        queen4 = Queen("W", 6, 4, board)

        board.add_piece(queen1, 7, 3)
        board.add_piece(queen2, 6, 3)
        board.add_piece(queen3, 6, 2)
        board.add_piece(queen4, 6, 4)
        
        self.assertEqual(queen1.generate_legal_moves(), 
        [(7, 4), (7, 5), (7, 6), (7, 7), (7, 2), (7, 1), (7, 0)],
        "Should be [(7, 4), (7, 5), (7, 6), (7, 7), (7, 2), (7, 1), (7, 0)]")

    def test_vertical_movement(self):
        board = Board()
        
        queen1 = Queen("W", 4, 0, board)
        queen2 = Queen("W", 5, 1, board)
        queen3 = Queen("W", 4, 1, board)
        queen4 = Queen("W", 3, 1, board)

        board.add_piece(queen1, 4, 0)
        board.add_piece(queen2, 5, 1)
        board.add_piece(queen3, 4, 1)
        board.add_piece(queen4, 3, 1)

        self.assertEqual(queen1.generate_legal_moves(), 
        [(5, 0), (6, 0), (7, 0), (3, 0), (2, 0), (1, 0), (0, 0)],
        "Should be [(5, 0), (6, 0), (7, 0), (3, 0), (2, 0), (1, 0), (0, 0)]")

    def test_diagonal_movement(self):
        board = Board()
        
        queen1 = Queen("W", 0, 0, board)
        queen2 = Queen("W", 6, 6, board)
        queen3 = Queen("W", 0, 1, board)
        queen4 = Queen("W", 1, 0, board)

        board.add_piece(queen1, 0, 0)
        board.add_piece(queen2, 6, 6)
        board.add_piece(queen3, 0, 1)
        board.add_piece(queen4, 1, 0)

        self.assertEqual(queen1.generate_legal_moves(), 
        [(1, 1,), (2, 2), (3, 3), (4, 4), (5, 5)],
        "Should be [(1, 1,), (2, 2), (3, 3), (4, 4), (5, 5)]")

if __name__ == '__main__':
    unittest.main()