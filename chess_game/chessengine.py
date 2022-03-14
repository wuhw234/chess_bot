import pygame as p
from gamestate import GameState

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def load_images():
    pieces = ["Bb", "Bk", "Bn", "Bp", "Bq", "Br",
              "Wb", "Wk", "Wn", "Wp", "Wq", "Wr"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess_game/images/" + piece + ".png"),
                                         (SQUARE_SIZE, SQUARE_SIZE))

def main():
    p.init()
    game_state = GameState()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    load_images()

    board = game_state.get_board()
    selected_square = ()
    player_clicks = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE
                if selected_square == (row, col):
                    selected_square = ()
                    player_clicks = []
                else:
                    selected_square = (row, col)
                    #only add if the selected square contains a piece that matches current turn
                    if len(player_clicks) == 1 or (board.is_occupied(row, col) and 
                        board.get_piece_color(row, col) == game_state.get_turn()):
                        player_clicks.append(selected_square)
                        print(player_clicks)
                    
                if len(player_clicks) == 2:
                    start_row, start_column = player_clicks[0][0], player_clicks[0][1]
                    end_row, end_column = player_clicks[1][0], player_clicks[1][1]
                    piece = board.get_square(start_row, start_column)
                    game_state.log_move(piece, start_row, start_column, end_row, end_column)
                    curr_color = game_state.get_turn()
                    # if game_state.is_checkmated(curr_color):
                    #     print("wpgg")

                    selected_square = ()
                    player_clicks = []

        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, game_state):
    draw_board(screen)
    draw_pieces(screen, game_state.get_board())

def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(0, DIMENSION):
        for column in range(0, DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE,
                                              SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            if board.is_occupied(row, column):
                piece = board.get_square(row, column)
                symbol = piece.get_symbol()
                screen.blit(IMAGES[symbol], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE,
                                                   SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()


