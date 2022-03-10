from pieces.bishop import Bishop

board = [[0] * 8 for i in range(0, 8)]
board[2][2] = 1
board[4][2] = 1
a = Bishop(0,3,3,board)
print(a.generate_legal_moves())