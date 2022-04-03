import random
import math

piece_values = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0

def get_random_move(moves):
    return random.choice(moves)
    
def get_best_move(moves, game_state, board, player_color):
    #CURRENT ALGORITHM: mega greedy with search depth of 1
    multiplier = -1 if player_color == "W" else 1
    max_score = -math.inf
    best_move = None
    for move in moves:
        start_row, start_column = move[0], move[1]
        end_row, end_column = move[2], move[3]
        piece = board.get_square(start_row, start_column)
        game_state.log_move(piece, start_row, start_column, end_row, end_column)
        score = multiplier * board.get_material()

        if score > max_score:
            best_move = move
            max_score = score

        game_state.undo_move()
    print(max_score)
    return best_move