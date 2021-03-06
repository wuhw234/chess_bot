import random
import math

DEPTH = 2
piece_values = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
next_move = None

def get_random_move(moves):
    return random.choice(moves)
    
def get_best_move(moves, game_state, board, turn):
    random.shuffle(moves)
    negamax(moves, game_state, board, turn, DEPTH)
    # negamax_alphabeta(moves, game_state, board, turn, DEPTH, -math.inf, math.inf)
    return next_move

def negamax_alphabeta(moves, game_state, board, turn, depth, alpha, beta):
    global next_move
    #always assumes opponent plays the best move
    multiplier = 1 if turn == "W" else -1
    if depth == 0:
        return multiplier * evaluate(game_state)

    max_score = -math.inf
    for move in moves:
        start_row, start_column = move[0], move[1]
        end_row, end_column = move[2], move[3]
        piece = board.get_square(start_row, start_column)
        game_state.log_move(piece, start_row, start_column, end_row, end_column)

        prev_move = game_state.get_prev_move()
        color = game_state.get_turn()
        legal_moves = board.get_all_legal_moves(prev_move, color)
        score = -negamax_alphabeta(legal_moves, game_state, board, color, depth-1, -beta, -alpha)
        if score >= max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move

        game_state.undo_move()
        if max_score > alpha: #pruning
            alpha = max_score
        if alpha >= beta:
            break

    return max_score

def negamax(moves, game_state, board, turn, depth):
    global next_move
    #always assumes opponent plays the best move
    multiplier = 1 if turn == "W" else -1
    if depth == 0:
        return multiplier * evaluate(game_state)

    max_score = -math.inf
    for move in moves:
        start_row, start_column = move[0], move[1]
        end_row, end_column = move[2], move[3]
        piece = board.get_square(start_row, start_column)
        game_state.log_move(piece, start_row, start_column, end_row, end_column)

        prev_move = game_state.get_prev_move()
        color = game_state.get_turn()
        legal_moves = board.get_all_legal_moves(prev_move, color)
        score = -negamax(legal_moves, game_state, board, color, depth-1)

        if score >= max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move

        game_state.undo_move()

    return max_score


def minimax(moves, game_state, board, turn, depth):
    global next_move
    #always assumes opponent plays the best move
    if depth == 0:
        return evaluate(game_state)

    if turn == "W":
        max_score = -math.inf
        for move in moves:
            start_row, start_column = move[0], move[1]
            end_row, end_column = move[2], move[3]
            piece = board.get_square(start_row, start_column)
            game_state.log_move(piece, start_row, start_column, end_row, end_column)

            prev_move = game_state.get_prev_move()
            color = game_state.get_turn()
            legal_moves = board.get_all_legal_moves(prev_move, color)
            score = minimax(legal_moves, game_state, board, color, depth-1)

            if score >= max_score:
                max_score = score
                if depth == DEPTH:
                    next_move = move

            game_state.undo_move()

        return max_score
    
    else:
        min_score = math.inf
        for move in moves:
            start_row, start_column = move[0], move[1]
            end_row, end_column = move[2], move[3]
            piece = board.get_square(start_row, start_column)
            game_state.log_move(piece, start_row, start_column, end_row, end_column)

            prev_move = game_state.get_prev_move()
            color = game_state.get_turn()
            legal_moves = board.get_all_legal_moves(prev_move, color)
            score = minimax(legal_moves, game_state, board, color, depth-1)

            if score <= min_score:
                min_score = score
                if depth == DEPTH:
                    next_move = move

            game_state.undo_move()

        return min_score

def evaluate(game_state):
    multiplier = -1 if game_state.get_turn() == "W" else 1
    if game_state.is_checkmate():
        return multiplier * math.inf
    elif game_state.is_stalemate():
        return 0
    else:
        score = game_state.evaluate()
        return score
    # color = game_state.get_turn()
    # multiplier = -1 if color == "W" else 1
    # if game_state.is_checkmate():
    #     return multiplier * math.inf
    # elif game_state.is_stalemate():
    #     return 0
    # else:
    #     piece_values = {"k": 0, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
    #     score = 0
    #     for i in range(0, 8):
    #         for j in range(0, 8):
    #             square = board.get_square(i, j)
    #             if square:
    #                 symbol = square.get_symbol()
    #                 if symbol[0] == "W":
    #                     score += piece_values[symbol[1]]
    #                 else:
    #                     score -= piece_values[symbol[1]]

    #     return score