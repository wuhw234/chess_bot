from board import Board

class GameState:

    def __init__(self):
        self.white_turn = True
        self.board = Board()
        self.movelog = []
