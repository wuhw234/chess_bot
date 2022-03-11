import unittest
from pieces.bishop import Bishop
from board import Board

class TestSum(unittest.TestCase):

    def test_bishop_no_movement(self):
        board = Board()
        bishop1 = Bishop("W", 7, 0, board)
        board.add_piece(bishop1, 7, 0)

        bishop2 = Bishop("W", 6, 1, board)
        board.add_piece(bishop2, 6, 1)

        self.assertEqual(bishop1.generate_legal_moves(), [], "Should be empty array")

    def test_bishop_capture(self):
        board = Board()
        bishop1 = Bishop("W", 7, 0, board)
        board.add_piece(bishop1, 7, 0)

        bishop2 = Bishop("B", 6, 1, board)
        board.add_piece(bishop2, 6, 1)

        self.assertEqual(bishop1.generate_legal_moves(), [(6, 1)], "Should be [(6, 1)]")
    
    def test_bishop_capture_and_move(self):
        board = Board()
        bishop1 = Bishop("W", 6, 1, board)
        board.add_piece(bishop1, 6, 1)

        bishop2 = Bishop("B", 7, 0, board)
        board.add_piece(bishop2, 7, 0)

        bishop3 = Bishop("W", 5, 2, board)
        board.add_piece(bishop3, 5, 2)

        bishop4 = Bishop("W", 5, 0, board)
        board.add_piece(bishop4, 5, 0)

        bishop5 = Bishop("W", 7, 2, board)
        board.add_piece(bishop5, 7, 2)

        self.assertEqual(bishop1.generate_legal_moves(), [(7, 0)], "Should be [(7, 0)]")

    def test_full_diagonal(self):
        board = Board()
        bishop1 = Bishop("W", 7, 7, board)
        board.add_piece(bishop1, 7, 7)

        self.assertEqual(bishop1.generate_legal_moves(), 
        [(6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1,), (0, 0)], 
        "Should be [(6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1,), (0, 0)]")

if __name__ == '__main__':
    unittest.main()